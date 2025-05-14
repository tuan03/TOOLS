from dotenv import load_dotenv
import os
load_dotenv()
GLOBAL_API_LINK = os.getenv("GLOBAL_API_LINK")
GLOBAL_PASSWORD = os.getenv("GLOBAL_PASSWORD")
PATH_PROFILE = os.getenv("PATH_PROFILE")
if not GLOBAL_API_LINK or not GLOBAL_PASSWORD or not PATH_PROFILE:
    print("Vui lòng kiểm tra lại thông tin trong file .env",flush=True)
    exit()
from pywinauto.application import Application
from pywinauto import findwindows
import time
import sys
import random
import string
import os
import shutil
from pywinauto.findwindows import ElementNotFoundError
import subprocess
import threading
import re
import requests
from pywinauto.keyboard import send_keys
from datetime import datetime
import pyautogui
import csv
from rand_info import generate_cccd

from myact import find_and_interact_with_control, go_to_url, fill_text_field,scroll_to_bottom, click_create_acc

# Biến lưu giá trị
last_email = None
last_mxn = None
lock_email = threading.Lock()
url = GLOBAL_API_LINK

import random


# Kết nối tới ứng dụng WebBrowser.exe
def connect_to_application():
    try:
        app = Application(backend="uia").connect(path="WebBrowser.exe", timeout=10)
        return app.top_window()  # Trả về cửa sổ chính
    except findwindows.ElementNotFoundError:
        print("Không tìm thấy ứng dụng WebBrowser.exe. Vui lòng đảm bảo ứng dụng đang chạy.",flush=True)
        exit(1)

def delete_folder(folder_name):
    base_path = PATH_PROFILE
    target_path = os.path.join(base_path, folder_name)
    try:
        if os.path.exists(target_path) and os.path.isdir(target_path):
            shutil.rmtree(target_path)
            print(f"Đã xóa thư mục: {target_path}",flush=True)
        else:
            print(f"Thư mục không tồn tại: {target_path}",flush=True)
    except PermissionError:
        print(f"Không thể xóa thư mục {target_path} vì nó đang được sử dụng.",flush=True)

def check_security_challenge(window,email):
    try:
        element = window.child_window(
            title="Security Challenge",
            control_type="Text"
        )
        element.wrapper_object()  # Nếu không tồn tại sẽ raise lỗi
        print("Phát hiện Security Challenge",flush=True)
        click_create_acc(window,auto_id="btn_restart", control_type="Button")
        time.sleep(2)
        delete_folder(email) # xóa profile
        return True
    except ElementNotFoundError:
        print("Không có Security Challenge",flush=True)
        return False
import time
def verify_email(window):
    global last_mxn
    start_time = time.time()
    timeout = 60  # giây
    while True:
        with lock_email:
            if last_mxn:
                break
        if time.time() - start_time > timeout:
            raise TimeoutError("Hết thời gian chờ: last_mxn vẫn là False sau 30 giây.")
        time.sleep(0.1)  # tránh dùng 100% CPU
    for (i, digit) in enumerate(last_mxn):
        try:
            auto_id = f"ci-email-confirmation-input-{i}"
            spinner = window.child_window(auto_id=auto_id, control_type="Spinner")
            spinner.set_focus()
            spinner.type_keys(digit, with_spaces=True)
            print(f"Đã nhập số {digit} vào ô thứ {i+1}",flush=True)
        except ElementNotFoundError:
            print(f"Không tìm thấy ô nhập mã thứ {i+1}",flush=True)
    time.sleep(3)
    with lock_email:
        last_mxn = None
def check_verfiemail_challen(window,email):
    try:
        element = window.child_window(
            title="Confirm your email", auto_id="paypalAccountData_emailVerificationModalHeading", control_type="Text"
        )
        element.wrapper_object()  # Nếu không tồn tại sẽ raise lỗi
        print("Phát hiện Email Challenge",flush=True)
        verify_email(window)
        return True
    except ElementNotFoundError:
        print("Không có Email Challenge",flush=True)
        return False


def runn(email, password):
    window = connect_to_application()

    global stop_mouse_thread
    global event_mouse_exit
    stop_mouse_thread = False
    event_mouse_exit = False
    panel = window.child_window(title="panelControl6", auto_id="panelControl6", control_type="Pane")
    panel.set_focus()
    email = email
    password = password
    cccd, tinh, gioi_tinh, nam_sinh, tinh_zipcode , address, town, family, middle, given, sdt = generate_cccd()

    # Bước 1: Xóa và nhập "test2@gmail.com" vào ô Profile name
    try:
        fill_text_field(window, auto_id="txt_profile", text=email)
        fill_text_field(window, auto_id="textEdit6", text=password)

        click_create_acc(window)
        time.sleep(5)  # Đợi 3 giây để tải trang
        #######################3
        go_to_url(window,"https://paypal.com/welcome/signup?locale.x=en_VN")

        time.sleep(3)  # Đợi 3 giây để tải trang

        find_and_interact_with_control(window, "Button", "paypalAccountData_submit", "click")

        find_and_interact_with_control(window, "Edit", "paypalAccountData_email", "type", text=email)

        find_and_interact_with_control(window, "Button", "paypalAccountData_submit", "click")
        time.sleep(3)  # Đợi 3 giây để tải trang
        if check_security_challenge(window,email) == True:
            print("Bị bắt xác thực",flush=True)
            return

        find_and_interact_with_control(window, "Edit", "paypalAccountData_phone", "type", text=sdt)
        time.sleep(1)
        find_and_interact_with_control(window, "Button", "paypalAccountData_submit", "click")
        time.sleep(3)  # Đợi 3 giây để tải trang


        find_and_interact_with_control(window, "Edit", "paypalAccountData_password", "type", text=password)
        find_and_interact_with_control(window, "Button", "paypalAccountData_submit", "click")
        time.sleep(random.uniform(1, 2)) 


        find_and_interact_with_control(window, "Edit", "paypalAccountData_lastName", "type", text=family)
        find_and_interact_with_control(window, "Edit", "paypalAccountData_middleName", "type", text=middle)
        find_and_interact_with_control(window, "Edit", "paypalAccountData_firstName", "type", text=given)

        find_and_interact_with_control(window, "Button", "paypalAccountData_emailPassword", "click")

        find_and_interact_with_control(window, "Button", "paypalAccountData_emailPassword", "click")
        time.sleep(3)  # Đợi 3 giây để tải trang


        find_and_interact_with_control(window, "Edit", "paypalAccountData_identificationNum", "type", text=cccd)
        fill_text_field(window, auto_id="paypalAccountData_dob", text=nam_sinh)

        find_and_interact_with_control(window, "Button", "paypalAccountData_emailPassword", "click")
        time.sleep(3)  # Đợi 3 giây để tải trang

        find_and_interact_with_control(window, "Edit", "paypalAccountData_address1_0", "type", text=address)
        find_and_interact_with_control(window, "Edit", "paypalAccountData_city_0", "type", text=town)
        find_and_interact_with_control(window, "Edit", "paypalAccountData_zip_0", "type", text=tinh_zipcode)

        scroll_to_bottom(window, max_attempts=15)

        find_and_interact_with_control(window, "CheckBox", "paypalAccountData_termsAgree", "click")
        find_and_interact_with_control(window, "CheckBox", "paypalAccountData_marketingOptIn", "click")


        
        find_and_interact_with_control(window, "Button", "dropdownMenuButton_paypalAccountData_state_0", "click")
        find_and_interact_with_control(window, "ListItem", f"smenu_item_{tinh}", "click")

        find_and_interact_with_control(window, "Button", "paypalAccountData_emailPassword", "click")
        time.sleep(6)
        go_to_url(window,"https://paypal.com")

        try:
            # Thử tìm Hyperlink
            hyperlink = window.child_window(
                title_re="^Submit info to access your funds.*",
                control_type="Hyperlink"
            )
            hyperlink.wrapper_object()  # Nếu không có sẽ raise lỗi

            print("Tài khoản lỗi",flush=True)

            click_create_acc(window,auto_id="btn_restart", control_type="Button")
            time.sleep(6)
            delete_folder(email) # xóa profile
            

        except ElementNotFoundError:
            try:
                # Thử tìm Hyperlink
                hyperlink = window.child_window(
                    title="We're permanently limiting your account. You can no longer use PayPal as we've decided to permanently limit your account after a review.",
                    control_type="Hyperlink"
                )
                hyperlink.wrapper_object()  # Nếu không có sẽ raise lỗi
                print("Tài khoản lỗi limit",flush=True)
                click_create_acc(window,auto_id="btn_restart", control_type="Button")
                time.sleep(6)
                delete_folder(email) # xóa profile
            except ElementNotFoundError:
                print("Tài khoản thành công",flush=True)
                time.sleep(2)
                find_and_interact_with_control(window, "Hyperlink", "header-settings", "click")
                time.sleep(4)
                find_and_interact_with_control(window, "Button", "interstitial-button-1", "click")
                time.sleep(3)

                verify_email(window)
                print("KEY GEN MAIL: __BANCHDKAKLSAKLDKMCNJSNXJS_;MAIL{"+email+"};{"+password+"}",flush=True)
                
                time.sleep(5)
                click_create_acc(window,auto_id="btn_restart", control_type="Button")
                time.sleep(5)


    except Exception as e:
        print(f"Lỗi trong quá trình thực hiện: {e}",flush=True)
        click_create_acc(window,auto_id="btn_restart", control_type="Button")
        time.sleep(5)
        delete_folder(email) # xóa profile
    finally:
        print("Kết thúc Một lần",flush=True)
        # Xử lý lỗi nếu cần thiết


def reset_server():
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get("status") == "success":
            info = data.get("info", {})
            print("✅ Đổi IP thành công:",flush=True)
            print("✅ Vui lòng đợi 10s...",flush=True)
            time.sleep(10)
            return True

        elif data.get("status") == "error":
            error_msg = data.get("error", "")
            print("⚠️ Lỗi:", error_msg,flush=True)

            # Trích số giây cần chờ
            match = re.search(r'(\d+)\s*giây', error_msg)
            if match:
                wait_seconds = int(match.group(1)) + 3
                print(f"⏳ Chờ {wait_seconds} giây trước khi thử lại...",flush=True)
                # time.sleep(wait_seconds)
                for i in range(wait_seconds, 0, -1):
                    print(f"⏳ Còn {i} giây...", end='\r', flush=True)
                    time.sleep(1)
                print(flush=True)
                return False
            else:
                print("Không xác định thời gian chờ.",flush=True)
                return False
        else:
            print("❓ Phản hồi không xác định:", data,flush=True)
            return False

    except requests.RequestException as e:
        print("❌ Request lỗi:", e,flush=True)
        return False
    except ValueError:
        print("❌ Không phải JSON hợp lệ.",flush=True)
        return False
# Regex
email_pattern = re.compile(r"^Email:\s*(.+)$")
mxn_pattern = re.compile(r"^MXN:\s*(.+)$")



# Tắt buffer stdout tiến trình con
env = os.environ.copy()
env["PYTHONUNBUFFERED"] = "1"

# Biến lưu tiến trình & thread hiện tại
current_process = None
current_thread = None

def reader_thread_fn(process):
    global last_email, last_mxn
    try:
        for line in process.stdout:
            line = line.strip()
            if not line:
                continue

            with lock_email:
                if m := email_pattern.match(line):
                    last_email = m.group(1)
                    print(f"[Thread] ==> Email nhận được: {last_email}",flush=True)
                elif m := mxn_pattern.match(line):
                    last_mxn = m.group(1)
                    print(f"[Thread] ==> MXN nhận được: {last_mxn}",flush=True)

    except Exception as e:
        print(f"[Thread] Lỗi: {e}",flush=True)

def start_watcher():
    global current_process, current_thread

    if current_process:
        current_process.terminate()
        current_process.wait()
    current_process = subprocess.Popen(
        ['./dist/mailer_nakskw.exe'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        env=env,
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    print("[Main] Đã khởi động tiến trình con mailer.py",flush=True)
    current_thread = threading.Thread(target=reader_thread_fn, args=(current_process,), daemon=True)
    current_thread.start()
def stop_process(myprocess):
    if myprocess.poll() is None:
        print("Đang kết thúc tiến trình Mailer...")
        myprocess.terminate()  # Cách nhẹ nhàng
        try:
            myprocess.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print("Tiến trình mailer không phản hồi, buộc dừng...")
            myprocess.kill()  # Cách mạnh nếu terminate không hiệu quả
try:
    while True:
        a = None 
        while True: 
            status = reset_server()
            if status:
                break
        print("[Main] 🔁 Đang khởi động lại server PROXY",flush=True)
        last_email = None
        last_mxn = None
        start_watcher()
        while True:
            with lock_email:
                if last_email:
                    break
        runn(last_email, GLOBAL_PASSWORD)
        powershell_command = '''
        Get-Process | Where-Object { $_.Name -like "*mailer_nakskw*" } | ForEach-Object { Stop-Process -Id $_.Id -Force }
        '''

        # Gọi PowerShell từ Python
        try:
            subprocess.run(["powershell", "-Command", powershell_command], check=True)
            print("Đã dừng tất cả tiến trình chứa 'mailer_nakskw'.")
        except subprocess.CalledProcessError as e:
            print("Có lỗi khi dừng tiến trình:", e)
        current_process = None
except Exception as e:
    print("Có Lỗi")
finally:
    print("App bị dừng đột ngột")
    powershell_command = '''
    Get-Process | Where-Object { $_.Name -like "*mailer_nakskw*" } | ForEach-Object { Stop-Process -Id $_.Id -Force }
    '''

    # Gọi PowerShell từ Python
    try:
        subprocess.run(["powershell", "-Command", powershell_command], check=True)
        print("Đã dừng tất cả tiến trình chứa 'mailer_nakskw'.")
    except subprocess.CalledProcessError as e:
        print("Có lỗi khi dừng tiến trình:", e)
    sys.exit(1)

