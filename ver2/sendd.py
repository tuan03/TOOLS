import requests
from datetime import datetime

url = "http://deliveriq.click/api/append"  # Thay bằng domain thực tế nếu cần

data = {
    "ten": "Trung",
    "thoigian": datetime.now().strftime("%H:%M_%d/%m/%Y"),  # Ví dụ: 14:35_13/05/2025
    "email": "an123@example.com",
    "pass": "abc123xyz"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("✅ Đã gửi thành công!")
else:
    print(f"❌ Lỗi: {response.status_code} - {response.text}")
