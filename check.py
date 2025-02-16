import pandas as pd
import joblib
import numpy as np
import re
from collections import Counter

# --- TẢI MÔ HÌNH ---
model = joblib.load("logistic_regression_model.pkl")

# --- ĐỌC DANH SÁCH TỪ KHÓA ---
df = pd.read_csv("emails.csv")  # Đọc dữ liệu gốc
tu_khoa = df.columns[:-1].tolist()  # Lấy danh sách từ khóa (bỏ cột nhãn)

def xu_ly_email(email_van_ban):
    """Chuyển email dạng văn bản thành vector số (giống dữ liệu huấn luyện)"""
    # Chuẩn hóa văn bản: Chuyển thành chữ thường, xóa ký tự đặc biệt
    email_van_ban = email_van_ban.lower()
    email_van_ban = re.sub(r'[^a-z\s]', '', email_van_ban)  # Chỉ giữ chữ cái và khoảng trắng
    
    # Đếm số lần xuất hiện của từng từ
    tu_dem = Counter(email_van_ban.split())
    
    # Tạo vector đặc trưng
    vector_email = [tu_dem[tu] if tu in tu_dem else 0 for tu in tu_khoa]
    
    # Trả về DataFrame với đúng tên cột
    return pd.DataFrame([vector_email], columns=tu_khoa)

# --- Nhập email từ bàn phím ---
email_nhap = input("✉️ Nhập nội dung email cần kiểm tra: ")

# Xử lý email
df_email = xu_ly_email(email_nhap)

# Dự đoán
du_doan = model.predict(df_email)

# In kết quả
print("📧 Email này là SPAM!" if du_doan[0] == 1 else "📩 Email này KHÔNG phải spam.")
