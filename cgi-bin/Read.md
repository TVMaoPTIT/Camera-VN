Tập lệnh cgi để mặc định trong /usr/lib/cgi-bin

CGI là gì?
  Common Gateway Interface hoặc CGI là một tập hợp các chuẩn mà định nghĩa cách thông tin được trao đổi giữa Web Server và một Custom Script.
CGI Specification hiện tại được duy trì bởi NCSA và NCSA định nghĩa CGI như sau: Common Gateway Interface hoặc CGI là một chuẩn cho các chương trình kết nối dị mạng ngoại vi (external gateway programs) tới Interface với thông tin từ Server như HTTP Server.
Để hiểu khái niệm về CGI, chúng ta xem những gì xảy ra khi chúng ta nhấn vào một hyperlink để tới một Webpage hoặc URL cụ thể.

Trình duyệt của bạn liên hệ HTTP Web Server và yêu cầu một URL, ví dụ: filename.
Web Server sẽ parse URL đó và sẽ tìm kiếm filename. Nếu nó tìm thấy file đã yêu cầu, thì Web Server gửi file đó trở lại trình duyệt, nếu không thì, nó gửi một thông báo lỗi chỉ rằng bạn đã yêu cầu một wrong file.
Trình duyệt Web nhận phản hồi từ Web Server và hiển thị file đã nhận được hoặc thông báo lỗi dựa trên phản hồi đã nhận.
Tuy nhiên, nó là có thể để thiết lập HTTP Server theo cách mà bất cứ khi nào một file trong một thư mục cụ thể được yêu cầu, thì file đó không được gửi trở lại; thay cho việc nó được thực thi như là một chương trình và output được tạo từ chương trình đã gửi tới trình duyệt để hiển thị.

Common Gateway Interface hoặc CGI là một giao thức chuẩn cho các ứng dụng (được gọi là CGI program hoặc CGI script) khả năng tương tác với Web Server và với Client. Những CGI program này có thể được viết bằng Python, PERL, Shell, C hoặc C++ …

Cấu hình Web Server
Trước khi bạn tiếp tục với lập trình CGI, đảm bảo rằng Web Server của bạn hỗ trợ CGI và nó được định cấu hình để xử lý CGI Program. Tất cả CGI program để được thực thi bởi HTTP Server được giữ trong một thư mục được định cấu hình trước. Thư mục này được gọi là CGI directory, và theo qui ước, nó được đặt tên là /var/www/cgi-bin. Theo qui ước, CGI file có đuôi là .cgi, vì thế chúng là có thể thực thi trong C++.
