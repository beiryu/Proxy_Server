# Computer Networks Project: Proxy Server Implementation

## Overview
This project implements a proxy server with manual configuration, HTTP website display, and blocked website access control.

## Features
- Manual proxy configuration for Firefox
- HTTP website display
- Access control for blocked websites

## Setup
1. Configure Firefox to use port 8888 and HTTP proxy
2. Run the proxy server
3. Access HTTP websites through the proxy

## Usage
- HTTP websites accessible through the proxy are listed in `http.text`
- Blocked websites are defined in `blacklist.conf`
- Accessing a blocked website will display a 403 Forbidden error

## Code Structure

### `main()`
- Manages request queue
- Creates and connects socket to specified port and host
- Initiates request handling thread

### `analyzeHeader(header, clientAddr)`
- Parses header to extract method, URL, and version
- Analyzes URL to determine HTTP and Port positions

### `Handle(connect, clientAddr)`
- Processes client requests
- Checks URL against blacklist
- Establishes connection with actual webserver
- Forwards client request to server
- Receives server response and sends it to client

## Why Use a Proxy Server?

1. **Internet Usage Control**: 
   - Monitor and restrict employee/child internet access
   - Block specific websites
   - Log web requests

2. **Bandwidth Saving and Speed Improvement**:
   - Cache frequently accessed web pages

3. **Privacy Enhancement**:
   - Mask IP address and identification information
   - Provide more private browsing experience

4. **Security Improvement**:
   - Encrypt web requests
   - Protect against malicious websites
   - Enable secure remote access through VPN integration

5. **Access to Blocked Resources**:
   - Bypass content restrictions
   - Access geo-restricted content

## Installation

[Add installation instructions here]

## Configuration

[Add configuration details here]

## Contributing

[Add contribution guidelines here]

## License

[Add license information here]
