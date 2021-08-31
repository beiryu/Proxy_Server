# Đồ án môn học: Mạng Máy Tính
### Manual proxy configuration
  Cấu hình Firefox đến port 8888 và HTTP proxy
### Build Proxy Server
### Show HTTP Website
  - file "http.text" chứa những file http có thể truy cập
  - Sau khi nhận dữ liệu từ server thì hiển thị cho client
### Access to blocked website
  - Websites bị cấm được lưu trong "blacklist.conf"
  - Khi truy cập thì show error, 403 - Forbidden: You don't have permission to access

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

# Why should we use Proxy Server
  - Để kiểm soát việc sử dụng Internet của nhân viên và trẻ em: Tổ chức và phụ huynh thiết lập máy chủ proxy để kiểm soát và giám sát nhân viên hoặc trẻ em sử dụng Internet. Hầu hết các tổ chức không muốn nhân viên của họ xem các trang web cụ thể trong thời gian làm việc và họ có thể cấu hình máy chủ proxy để từ chối truy cập vào trang web cụ thể, điều hướng bạn bằng một ghi chú yêu cầu bạn không xem các trang web này trên mạng công ty. Họ có thể giám sát và ghi lại tất cả các yêu cầu web, do đó mặc dù không chặn trang web nhưng họ vẫn biết thời gian bạn dành cho những việc làm khác ngoài công việc.
  -	Tiết kiệm băng thông và cải thiện tốc độ: Các tổ chức cũng có thể nhận được hiệu suất mạng tổng thể tốt hơn khi sử dụng máy chủ proxy. Các máy chủ proxy có thể lưu vào bộ nhớ cache (lưu một bản sao trang web cục bộ) các trang web hay truy cập.
  -	Bảo mật riêng tư: Cá nhân và tổ chức cũng sử dụng máy chủ proxy để duyệt Internet riêng tư hơn. Một số máy chủ proxy sẽ thay đổi địa chỉ IP và thông tin nhận dạng khác. Điều này có nghĩa là máy chủ đích không biết ai thực sự đã thực hiện yêu cầu ban đầu, giúp giữ thông tin cá nhân và thói quen duyệt web của bạn riêng tư hơn.
  -	Cải thiện bảo mật: Bạn có thể cấu hình máy chủ proxy để mã hóa yêu cầu web để không ai có thể đọc được giao dịch của bạn. Ngoài ra, người dùng cũng có thể tránh các trang web độc hại thông qua máy chủ proxy. Các tổ chức có thể kết nối máy chủ proxy của họ với Mạng riêng ảo (VPN), do đó người dùng từ xa có thể truy cập Internet thông qua proxy của công ty. VPN kết nối trực tiếp đến mạng công ty để có thể kiểm soát và xác minh người dùng của họ có quyền truy cập vào các tài nguyên họ cần (email, dữ liệu nội bộ) đồng thời cũng cung cấp kết nối an toàn cho người dùng để bảo vệ dữ liệu công ty.
  -	Truy cập vào các tài nguyên bị chặn: Máy chủ proxy cho phép người dùng phá vỡ các hạn chế nội dung do công ty hoặc một số tổ chức áp đặt. Nếu truy cập vào trang web bị chặn, bạn có thể đăng nhập vào máy chủ proxy ở nơi khác và xem từ đó. Máy chủ proxy khiến bạn giống như ở Mỹ nhưng thực ra bạn đang ở Việt Nam.








