GLOBAL_USER = "gynmp_shmil"
GLOBAL_PASS = "xvVoAcoA"
GLOBAL_IP = "117.0.205.144"
GLOCAL_PORT = "15611"
import tls_client
import json
import time
from datetime import datetime
import re
import os
class TempMail:
    def __init__(self, bearer_token: str = None) -> None:
        # Cấu hình proxy
        PROXY = {
            "http": f"http://{GLOBAL_USER}:{GLOBAL_PASS}@{GLOBAL_IP}:{GLOCAL_PORT}",
            "https": f"http://{GLOBAL_USER}:{GLOBAL_PASS}@{GLOBAL_IP}:{GLOCAL_PORT}"
        }

        # Khởi tạo session tls-client
        self.session = tls_client.Session(
            client_identifier="chrome_108",
            random_tls_extension_order=True
        )
        
        # Áp dụng proxy cho session
        self.session.proxies = PROXY  # Sử dụng proxies thay vì proxy
        
        # Cấu hình headers
        self.session.headers = {
            "accept": "*/*",
            "accept-language": "vi-VN,vi;q=0.9",
            "content-type": "application/json",
            "origin": "https://temp-mail.org",
            "referer": "https://temp-mail.org/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        }
        
        self.base_url = 'https://web2.temp-mail.org'
        
        if bearer_token:
            self.session.headers['authorization'] = f'Bearer {bearer_token}'

    def get_mail(self):
        status = self.session.get(f'{self.base_url}').status_code
        try:
            if status == 200:
                response = self.session.post(f'{self.base_url}/mailbox')
                data = response.json()
                
                # Kiểm tra lỗi Too Many Request
                if "errorName" in data and data["errorName"] == "TooManyRequestsException":
                    print("Đạt giới hạn GET mail trên 1 IP")
                    return None, False 
                
                self.session.headers['authorization'] = f'Bearer {data["token"]}'
                return data["token"], data["mailbox"]
        except:
            return 'Email creation error.', False
    
    def fetch_inbox(self) -> json:
        response = self.session.get(f'{self.base_url}/messages').json()
        return response
    
    def get_message_content(self, message_id: str):
        response = self.session.get(f'{self.base_url}/messages/{message_id}').json()
        return response["bodyHtml"]

if __name__ == "__main__":
    # Khởi tạo client
    email_client = TempMail()
    
    try:
        # print("Đang tạo email...")
        token, email = email_client.get_mail()
        
        if not email or email == "Email creation error.":
            # print("Không thể tạo email")
            exit()
            
        print(f"Email:{email}",flush=True)
        # print(f"Token: {token}")
        
        
        while True:
            messages = email_client.fetch_inbox()
            if messages.get("messages") and len(messages["messages"]) > 0:
                for msg in messages["messages"]:
                    content = email_client.get_message_content(msg["_id"])
                    print(f"\nFrom: {msg.get('from', 'Unknown')}")
                    print(f"Subject: {msg.get('subject', 'No subject')}")
                    if msg.get('subject') == "Your PayPal verification code":
                        regex_pattern = r'(Your verification code is |Verification code: )(\d{6})'
                        match = re.search(regex_pattern, content)
                        if match:
                            verification_code = match.group(2)
                            print(f"MXN:{verification_code}",flush=True)
            time.sleep(5)
            
    except KeyboardInterrupt:
        a = 2
    except Exception as e:
        b = 1