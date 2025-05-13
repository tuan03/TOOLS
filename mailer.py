
import json
import time
from datetime import datetime
import re
import os
import random
import string
import requests
domains = [
    "@hunght1890.com"
    "@simpace.edu.vn",
    "@mail.hunght1890.com",
    "@hoanganh.mx",
    "@itemjunction.net",
    "@oggymail.net",
    "@bapnumail.com",
    "@lakebamail.com",
    "@denmarumail.com",
    "@kataranmail.com",
    "@kenturemail.com",
    "@sanpekomail.com",
    "@santaramail.com",
    "@quanlytinhgon.vn",
    "@harborheights.education"
    ]
def tao_chuoi_ngau_nhien(do_dai=10):
    ky_tu = string.ascii_lowercase + string.digits  # 'abcdefghijklmnopqrstuvwxyz0123456789'
    chuoi = ''.join(random.choices(ky_tu, k=do_dai))
    return chuoi


def get_random_email():
    # Tạo một chuỗi ngẫu nhiên cho email
    return tao_chuoi_ngau_nhien(do_dai=3)+"_"+tao_chuoi_ngau_nhien()+random.choice(domains)

def get_mail(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()  # Chuyển đổi nội dung sang JSON
            return data
        except ValueError:
            print("Dữ liệu không ở định dạng JSON hợp lệ.")
    else:
        return []


if __name__ == "__main__":
    try:
        email = get_random_email()
        url = f"http://hunght1890.com/{email}"
        
        print(f"Email:{email}",flush=True)
        wait_MXH = True
        while wait_MXH:
            mail_box = get_mail(url)
            for msg in mail_box:
                content = msg.get("body", "")
                print(f"\nFrom: {msg.get('from', 'Unknown')}")
                print(f"Subject: {msg.get('subject', 'No subject')}")
                print(f"Content: {content}")
                if msg.get('subject') == "Your PayPal verification code":
                    regex_pattern = r'(Your verification code is |Verification code: )(\d{6})'
                    match = re.search(regex_pattern, content)
                    if match:
                        verification_code = match.group(2)
                        print(f"MXN:{verification_code}",flush=True)
                        wait_MXH = False
                        
        time.sleep(2)
            
    except KeyboardInterrupt:
        a = 2
    except Exception as e:
        b = 1


