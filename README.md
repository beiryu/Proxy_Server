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
  def main():
  + Chờ xử lý hàng đợi
  + Tạo Socket
  + Kết nối Socket đến port and host
  + Tạo luồng xử lý yêu cầu
  def analyzeHeader(header, clientAddr):
  + Phân tích header để tìm method, url, ver
  + Phân tích url để tìm HTTP position và Port position.









