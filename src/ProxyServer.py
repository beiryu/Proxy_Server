import _thread
import socket


# Buffer_Max Size Receive
buffer = 100000
# Read File Conf
BLOCKED = []
BLACKLIST = "blacklist.conf"
FILE = open(BLACKLIST, "rb")
data = ""
while True:
    line = FILE.read()
    if not len(line):
        break
    data += line.decode()
FILE.close()
BLOCKED = data.splitlines()


# Main
def main():
    # Pending Connections Queue
    BACKLOG = 100
    host = ''
    port = 8888
    print("~Set ip: ", host)
    print("~Set port: ", port)
    print("Proxy Server running..")
    try:
        # Build A Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Associate The Socket To Host, Port
        s.bind((host, port))
        s.listen(BACKLOG)
        print(f'Listening at port:{port} ..')
    except socket.error:
        print("Could not open socket")
        if s:
            s.close()
            return
    # Get The Connection
    while True:
        connect, clientAddr = s.accept()
        # Create A Thread To Handle Request
        _thread.start_new_thread(Handle, (connect, clientAddr))
    s.close()


# Print Information
def printout(type, method, url, ver, clientAddr):
    print(clientAddr)
    print(" ", type, method, "][", url, "][", ver)


# Find Webserver And Port
def analyzeHeader(header, clientAddr):
    method = header.split(' ')[0]
    url = header.split(' ')[1]
    ver = header.split(' ')[2]
    printout("[Request: ", method, url, ver, clientAddr)
    # Find http Position
    httpPos = url.find("://")
    if (httpPos == -1):
        temp = url
    else:
        temp = url[(httpPos+3):]
    # Find port Position
    portPos = temp.find(":")
    webserverPos = temp.find("/")
    if webserverPos == -1:
        webserverPos = len(temp)
    webserver = ""
    port = -1
    if (portPos == -1 or webserverPos < portPos):
        port = 80
        webserver = temp[:webserverPos]
    else:
        port = int((temp[(portPos+1):])[:webserverPos-portPos-1])
        webserver = temp[:portPos]
    return webserver, port


def Handle(connect, clientAddr):
    # Get Client Request
    request = connect.recv(buffer)
    header = request.decode("utf-8").split('\n')[0]
    try:
        url = header.split(' ')[1]
    except:
        return
    # Check Url In The Blacklist
    for i in range(0, len(BLOCKED)):
        if BLOCKED[i] in url:
            print(clientAddr)
            print("[BLOCKED SITE] ", url, header.split(' ')[2])
            # Send Error: 403-Forbbiden To Client
            message = 'HTTP/1.1 403 Forbidden\r\n\r\n<html><head></head><body><header><title>'+url + \
                '</title></header>\n\n<h1>403-Forbidden</h1>\n<p>You dont have permission to access</p></body></html>\n'
            connect.send(message.encode())
            connect.close()
            return
    # Analyze Client Request
    webserver, port = analyzeHeader(header, clientAddr)
    # Build A Socket Connect To The Real WebServer
    print(webserver, port)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        # Send Client Request To The Server
        s.send(request)
        while True:
            # Receive Response From The Server Through Socket
            data = s.recv(buffer)
            # Send The Real Server Response To The Client
            if (len(data) > 0):
                connect.send(data)
            else:
                break
        s.close()
        connect.close()
    except socket.error:
        if s:
            s.close()
        if connect:
            connect.close()
        print("Reset")
        return


if __name__ == '__main__':
    main()
