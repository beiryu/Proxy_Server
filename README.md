# Đồ án môn học: Mạng Máy Tính
### Manual proxy configuration
  Cấu hình Firefox đến port 8888 và HTTP proxy
### Build Proxy Server
### Show HTTP Website
  - "file http.text" chứa những file http có thể truy cập
  - Sau khi nhận dữ liệu từ server thì hiển thị cho client
### Access to blocked website
  Show ERROR:
   - 403 - Forbidden: You don't have permission to access

# Explain source code
### def main():
  + Chờ xử lý hàng đợi
  + Tạo Socket
  + Kết nối Socket đến port and host
  + Tạo luồng xử lý yêu cầu
### def analyzeHeader(header, clientAddr):
  + Phân tích header để tìm method, url, ver
  + Phân tích url để tìm HTTP position và Port position.
### def Handle(connect, clientAddr):
  + Từ connect lấy ra request của Client
  + Kiểm tra Url có trong Blacklist hay không.
  + Gọi hàm Analyze Client Request (def analyzeHeader(header, clientAddr)) để lấy ra 2 giá trị webserver và port
  + Tạo một Socket kết nối tới webserver thật
  + Gửi một Client Request đến server đó.
  + Nhận Response từ server thông qua Socket.
  + Gửi phản hồi đó đến Client.

### Đinh Nguyên Khánh 








