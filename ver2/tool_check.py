GLOBAL_DATA = './data.csv'
GLOBAL_PROFILE = "D:/TOOLS_KT/1_Paypal/Create_Paypal/Create_Paypal/Create_Paypal/profile"
import os
import shutil
import csv
from datetime import datetime

# Bước 1: Đọc email từ file CSV
def read_emails_from_csv(filepath):
    emails = set()
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            email = row[0].strip()
            if email:
                emails.add(email)
    return emails

# Bước 2: Tạo thư mục sao chép
def copy_profile_folder(src_path, dest_base_path='./temp'):
    timestamp = datetime.now().strftime('%d_%m_%y-%Hh%M')
    dest_path = os.path.join(dest_base_path, f'profile_{timestamp}')
    shutil.copytree(src_path, dest_path)
    return dest_path

# Bước 3: Xóa thư mục con không hợp lệ
def clean_profile_folder(profile_path, valid_emails):
    for folder_name in os.listdir(profile_path):
        folder_path = os.path.join(profile_path, folder_name)
        if os.path.isdir(folder_path) and folder_name not in valid_emails:
            print(f"Deleting: {folder_path}")
            shutil.rmtree(folder_path)

# --- Main ---
def main():
    csv_file = GLOBAL_DATA
    original_profile_path = GLOBAL_PROFILE

    # Bước 1
    valid_emails = read_emails_from_csv(csv_file)
    print(f"Đã đọc {len(valid_emails)} email hợp lệ từ file CSV.")

    # Bước 2
    copied_profile_path = copy_profile_folder(original_profile_path)
    print(f"Đã sao chép hồ sơ từ {original_profile_path} đến {copied_profile_path}.")

    # Bước 3
    print("Đang xóa các thư mục không hợp lệ...")
    clean_profile_folder(original_profile_path, valid_emails)
    print(f"Đã xóa các thư mục không hợp lệ trong {original_profile_path}.")

    print(f"Hoàn tất. Hồ sơ đã được lưu tại: {copied_profile_path}")

if __name__ == '__main__':
    main()
