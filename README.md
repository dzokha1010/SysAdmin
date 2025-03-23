# SysAdmin Laboratory
## Install Git
- Step 1: Tải và cài đặt Git: https://git-scm.com/downloads
- Step 2: Đăng ký tài khoản trên github.com
- Step 3: Gửi địa chỉ mail đăng ký github.com cho giảng viên để được mời làm cộng tác viên trên kho SysAdmin
- Step 4: Truy cập kho SysAdmin để theo dõi nộp bài thực hành: https://github.com/dzokha1010/SysAdmin
## Clone and Push to SysAdmin
- Step 1: Mở Command Prompt hoặc CMD trên Windows
- Step 2: Thực hiện câu lệnh clone SysAdmin
  ```
  git clone https://github.com/dzokha1010/SysAdmin.git
  ```
- Step 2: Di chuyển vào thư mục SysAdmin
  ```
  cd SysAdmin
  ```
- Step 3: Tạo tập tin Word đặt tên là MSSV lưu trong thư mục SysAdmin, tập tin này sẻ lưu trữ kết quả mỗi buổi thực hành.
- Step 4: Chụp hình kết quả thực hành từng bài tập và dán vào tập tin Word
- Step 5: Nộp tập tin Word sau buổi thực hành lên kho SysAdmin bằng các câu lệnh
  ```
  git add .  
  git commit -m "<ghi chú>"  
  git push -u origin <name_branch>
  ```
- Lưu ý: Nên tạo Token thay thế mật khẩu để thuận tiện mỗi khi thực hiện câu lệnh Push
  - Link để tạo Token: https://github.com/settings/tokens
## Lab1 - Installing Windows Server 2022
- Hướng dẫn thực hành: [Github](https://github.com/dzokha1010/Documents/blob/main/System_Administration_Maintenance/Lab1_Install_Windows_Server.md)
- Lab1 thực hành 02 buổi 10 tiết
- Vắng buổi 1 (MSSV): 5, 7, 14, 20, 28, 44, 45, 66, 76, 78
- Văng buổi 2 (MSSV): 5, 14, 20, 28, 33, 42, 44, 45, 71, 76, 78
## Lab2 - Optimizing Windows Server 2022
- Hướng dẫn thực hành:
- Lab2 thực hành 01 buổi 5 tiết
- Vắng buổi 3 (MSSV): 05, 09, 20, 42, 44, 45, 68, 71, 76, 78
## Lab3 - Implementing services for Windows Server 2022
- Hướng dẫn thực hành:
- Lab3 thực hành 03 buổi 15 tiết
- Có mặt buổi 4: 15, 17, 18, 21, 73

  
