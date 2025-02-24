# SysAdmin Laboratory
## Install Git
- Step 1: Tải và cài đặt Git: https://git-scm.com/downloads
- Step 2: Đăng ký tài khoản trên github.com
- Step 3: Gửi địa chỉ mail đăng ký github.com cho giảng viên để được mời làm cộng tác viên trên kho SysAdmin
- Step 4: Truy cập kho SysAdmin để theo dõi nộp bài thực hành: https://github.com/dzokha1010/SysAdmin
## Lab1 - Installing Windows Server 2022
- Hướng dẫn thực hành: [Github](https://github.com/dzokha1010/Documents/blob/main/System_Administration_Maintenance/Lab1_Install_Windows_Server.md)
- Lab1 thực hành 02 buổi 10 tiết
- Vắng buổi 1 (MSSV): 5, 7, 14, 20, 28, 35, 44, 45, 46, 66, 76, 78
- Có mặt buổi 2: 01,10, 11, 13, 15, 16,17, 18, 19, 21, 22, 24, 26, 31, , 36, 37, 38, 39, , 47, 49, 50, , 56, 58, 59, 62, 64, 66, 67, 69, 70, 73,74,75
## Nộp bài thực hành lên Github.com trên kho SysAdmin
- Bước 1. Download và cài đặt Git: https://git-scm.com/downloads
- Bước 2. Đăng ký tài khoản trên github.com
- Bước 3. Gửi địa chỉ mail đăng ký github.com cho giảng viên để add tài khoản vào kho SysAdmin
- Bước 4. clone kho SysAdmin về máy tính cá nhân:
  1. Mở Command Prompt hoặc CMD trên Windows
  2. thực hiện câu lệnh: git clone https://github.com/dzokha1010/SysAdmin.git
  3. Di chuyển vào thư mục SysAdmin: cd SysAdmin
- Bước 5. Tạo File Word đặt tên là mã số sinh viên lưu trong thư mục SysAdmin, File này để lưu kết qủa sau mỗi buổi thực hành
- Bước 6. Thực hiện câu lệnh lưu File Word lên kho SysAdmin lưu trên Github.com

  ```
  git add .  

  git commit -m "<ghi chú>"  

  git push -u origin <name_branch>
  ```

  Đồng bộ từ Github về máy tính: git pull

  ## Tạo Token thay thể mật khẩu mỗi khi push lên kho
  Truy cập link để tạo Token: https://github.com/settings/tokens
  
