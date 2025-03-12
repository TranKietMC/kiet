import pandas as pd

# Đọc dữ liệu từ file CSV
file_path = "TCB_2018_2020.csv"  # Đảm bảo file nằm trong cùng thư mục
df = pd.read_csv(file_path)

# (1) Xuất toàn bộ dữ liệu
print("\n--- (1) TOÀN BỘ DỮ LIỆU ---")
print(df)

# (2) Lọc dữ liệu có Close < x và Close > y
x = float(input("\nNhập giá trị x (Close < x): "))
y = float(input("Nhập giá trị y (Close > y): "))
filtered_close = df[(df["Close"] < x) | (df["Close"] > y)]
print("\n--- (2) DỮ LIỆU LỌC THEO CLOSE ---")
print(filtered_close)

# (3) Trích lọc dữ liệu chỉ lấy Date, High, Low với Low từ x tới y
x_low = float(input("\nNhập giá trị x (Low >= x): "))
y_low = float(input("Nhập giá trị y (Low <= y): "))
filtered_low = df[(df["Low"] >= x_low) & (df["Low"] <= y_low)][["Date", "High", "Low"]]
print("\n--- (3) DỮ LIỆU LỌC THEO LOW ---")
print(filtered_low)

# (4) Nhập vào một ngày, xuất thông tin chi tiết của ngày giao dịch này
specific_date = input("\nNhập ngày cần tìm (YYYY-MM-DD): ")
filtered_date = df[df["Date"] == specific_date]
print("\n--- (4) DỮ LIỆU CHO NGÀY CỤ THỂ ---")
print(filtered_date if not filtered_date.empty else "Không tìm thấy dữ liệu cho ngày này.")

# (5) Nhập vào một danh sách ngày, lọc dữ liệu theo danh sách này
date_list = input("\nNhập danh sách ngày cần tìm (cách nhau bằng dấu phẩy, YYYY-MM-DD): ").split(",")
date_list = [date.strip() for date in date_list]
filtered_dates_list = df[df["Date"].isin(date_list)]
print("\n--- (5) DỮ LIỆU THEO DANH SÁCH NGÀY ---")
print(filtered_dates_list if not filtered_dates_list.empty else "Không tìm thấy dữ liệu cho các ngày này.")
