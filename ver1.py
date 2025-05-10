GLOBAL_API_LINK = "https://api.enode.vn/getip/52daa2c23aef86f6bcec6589b63f7dd3adc1ee60"
GLOBAL_PASSWORD =  "AmosIrvin6028"


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
import pyautogui
# Biến lưu giá trị
last_email = None
last_mxn = None
lock = threading.Lock()
stop_mouse_thread = False
url = GLOBAL_API_LINK

import pandas as pd
import random

def generate_vietnam_phone_number():
    # Danh sách các đầu số di động hợp lệ ở Việt Nam
    prefixes = [
        "09"                                      # Gmobile
    ]
    prefix = random.choice(prefixes)
    suffix = ''.join(random.choices("0123456789", k=8))  # 7 chữ số còn lại
    return prefix + suffix
def generate_vietnamese_name():
    family_names = [
        "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng",
        "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý", "Tạ", "Đinh", "Trịnh", "Mai", "Hà",
        "La", "Chu", "Cao", "Thái", "Kiều", "Tô", "Lâm", "Quách",
        "Trương", "Lương", "Vương", "Đoàn", "Quang", "Cung", "Tống", "Triệu", 
        "Nghiêm", "Bạch", "Vi", "Giang", "Nguyễn Thị", "Lưu", "Liêu", "Thạch", "Châu", 
        "Hứa", "Phùng", "Tiêu", "Tăng", "Âu Dương", "Mạc", "Trà"
    ]

    middle_names = [
        "Văn", "Hữu", "Đức", "Công", "Ngọc", "Thị", "Minh", "Gia", "Thanh", "Trọng",
        "Anh", "Quang", "Xuân", "Tiến", "Thành", "Tấn", "Thế", "Nhật", "Bảo", "Diệu",
        "Mạnh", "Khánh", "Thùy", "Phương", "Vĩnh", "Phúc", "Đình", "Thiện",
        "Chí", "Tuấn", "Kim", "Lan", "Hải", "Trí", "Thảo", "Thu", "Mai", "Diễm",
        "Tú", "Ngân", "Yến", "Như", "Tường", "Việt", "Đan", "Thi", "An", "Linh",
        "Tâm", "Cẩm", "Hương", "Hòa", "Lệ", "Thắm", "Quỳnh", "Thục", "Tiểu", "Uyên"
    ]

    given_names = [
        "An", "Bình", "Chi", "Dũng", "Hà", "Hạnh", "Hải", "Hiếu", "Hương", "Hùng",
        "Khoa", "Khôi", "Lan", "Linh", "Mai", "Nam", "Phong", "Phúc", "Quân", "Quỳnh",
        "Sơn", "Tâm", "Thảo", "Thắng", "Thịnh", "Trang", "Trung", "Tú", "Tuấn", "Vy",
        "Anh", "Thư", "Hải", "Long", "Tiến", "Ngân", "Thúy", "Lộc", "Tín", "Loan",
        "Nhung", "Kim", "Diễm", "Yến", "Tường", "Việt", "Châu", "Vân", "Bảo", "Nhi",
        "Đạt", "Kiên", "Cường", "Hạo", "Tài", "Khánh", "Thái", "Trí", "Phát", "Toàn",
        "Duy", "Đức", "Khang", "Thiện", "Lâm", "Hậu", "Tiểu", "Hoa", "Thắm", "Oanh",
        "Trâm", "Ngọc", "Thục", "Hân", "Giang", "My", "Di", "Thu", "Hòa", "Minh",
        "Tú", "Uyên", "Thương", "Lệ", "Tuyến", "Trang", "Như", "Tịnh", "Thúy An", "Bích"
    ]


    family = random.choice(family_names)
    middle = random.choice(middle_names)
    given = random.choice(given_names)

    return family, middle, given
tinh_zipcodes = {
    "An Giang": "880000", "Bà Rịa Vũng Tàu": "790000", "Bạc Liêu": "260000", "Bắc Kạn": "960000", 
    "Bắc Giang": "220000", "Bắc Ninh": "790000", "Bến Tre": "930000", "Bình Dương": "590000", 
    "Bình Định": "820000", "Bình Phước": "830000", "Bình Thuận": "800000", "Cà Mau": "970000", 
    "Cao Bằng": "270000", "Cần Thơ": "900000", "Đà Nẵng": "550000", "Điện Biên": "380000", 
    "Đắk Lắk": "630000", "Đắc Nông": "640000", "Đồng Nai": "810000", "Đồng Tháp": "870000", 
    "Gia Lai": "600000", "Hà Giang": "310000", "Hà Nam": "400000", "Hà Nội": "100000", 
    "Hà Tĩnh": "480000", "Hải Dương": "170000", "Hải Phòng": "180000", "Hậu Giang": "910000", 
    "Hòa Bình": "350000", "TP. Hồ Chí Minh": "700000", "Hưng Yên": "160000", "Khánh Hoà": "650000", 
    "Kiên Giang": "920000", "Kon Tum": "580000", "Lai Châu": "390000", "Lạng Sơn": "240000", 
    "Lào Cai": "330000", "Lâm Đồng": "670000", "Long An": "850000", "Nam Định": "420000", 
    "Nghệ An": "460000", "Ninh Bình": "430000", "Ninh Thuận": "660000", "Phú Thọ": "290000", 
    "Phú Yên": "620000", "Quảng Bình": "510000", "Quảng Nam": "560000", "Quảng Ngãi": "570000", 
    "Quảng Ninh": "200000", "Quảng Trị": "520000", "Sóc Trăng": "950000", "Sơn La": "360000", 
    "Tây Ninh": "840000", "Thái Bình": "410000", "Thái Nguyên": "250000", "Thanh Hoá": "440000", 
    "Thừa Thiên Huế": "530000", "Tiền Giang": "860000", "Trà Vinh": "940000", "Tuyên Quang": "300000", 
    "Vĩnh Long": "890000", "Vĩnh Phúc": "280000", "Yên Bái": "320000"
}

# # Danh sách mã tỉnh
# ma_tinh_dict = {
#     "Hà Nội": "001", "Hà Giang": "002", "Cao Bằng": "004", "Bắc Kạn": "006", "Tuyên Quang": "008",
#     "Lào Cai": "010", "Điện Biên": "011", "Lai Châu": "012", "Sơn La": "014", "Yên Bái": "015",
#     "Hòa Bình": "017", "Thái Nguyên": "019", "Lạng Sơn": "020", "Quảng Ninh": "022", "Bắc Giang": "024",
#     "Phú Thọ": "025", "Vĩnh Phúc": "026", "Bắc Ninh": "027", "Hải Dương": "030", "Hải Phòng": "031",
#     "Hưng Yên": "033", "Thái Bình": "034", "Hà Nam": "035", "Nam Định": "036", "Ninh Bình": "037",
#     "Thanh Hóa": "038", "Nghệ An": "040", "Hà Tĩnh": "042", "Quảng Bình": "044", "Quảng Trị": "045",
#     "Thừa Thiên Huế": "046", "Đà Nẵng": "048", "Quảng Nam": "049", "Quảng Ngãi": "051", "Bình Định": "052",
#     "Phú Yên": "054", "Khánh Hòa": "056", "Ninh Thuận": "058", "Bình Thuận": "060", "Kon Tum": "062",
#     "Gia Lai": "064", "Đắk Lắk": "066", "Đắk Nông": "067", "Lâm Đồng": "068", "Bình Phước": "070",
#     "Tây Ninh": "072", "Bình Dương": "074", "Đồng Nai": "075", "Bà Rịa - Vũng Tàu": "077", "Hồ Chí Minh": "079",
#     "Long An": "080", "Tiền Giang": "082", "Bến Tre": "083", "Trà Vinh": "084", "Vĩnh Long": "086",
#     "Đồng Tháp": "087", "An Giang": "089", "Kiên Giang": "091", "Cần Thơ": "092", "Hậu Giang": "093",
#     "Sóc Trăng": "094", "Bạc Liêu": "095", "Cà Mau": "096"
# }

ma_tinh_dict = {
    "An Giang": "089"
}
from datetime import datetime, timedelta

def generate_random_birthdate(year) -> str:
    # Tạo ngày đầu tiên và ngày cuối cùng trong năm đó
    start_date = datetime(int(year), 1, 1)
    end_date = datetime(int(year), 12, 31)
    
    # Tính số ngày chênh lệch
    delta_days = (end_date - start_date).days

    # Random một số ngày để cộng vào từ ngày đầu năm
    random_days = random.randint(0, delta_days)
    random_date = start_date + timedelta(days=random_days)

    # Trả về chuỗi định dạng DDMMYYYY
    return random_date.strftime("%m%d%Y")

# Đọc dữ liệu từ file Excel
def load_data(file_path):
    # Đọc dữ liệu từ Excel vào DataFrame
    return pd.read_excel(file_path)
def generate_random_number_text():
    if random.choice([True, False]):
        # Dạng 1: Một số 1 hoặc 2 chữ số
        return str(random.randint(1, 99))
    else:
        # Dạng 2: Hai số cách nhau bởi dấu /
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        return f"{num1}/{num2}"
# Hàm sinh địa chỉ ngẫu nhiên
def generate_random_address(province_name, df):
    # Lọc ra các địa chỉ có tỉnh thành tương ứng
    province_data = df[df['Tỉnh Thành Phố'] == province_name]
    
    if not province_data.empty:
        # Chọn ngẫu nhiên một dòng trong tỉnh
        random_row = province_data.sample(n=1).iloc[0]
        tinh_name = random_row['Tỉnh Thành Phố']
        # Tạo địa chỉ mẫu
        address_line = f"{random.randint(1, 99)} đường {generate_random_number_text()} {random_row['Phường Xã']} {random_row['Quận Huyện']} {random_row['Tỉnh Thành Phố']}"
        town = random_row['Quận Huyện']
        
        return address_line, town
    else:
        return None, None

# Đọc dữ liệu từ file Excel
file_path = "./myexc.xls"  # Thay đổi đường dẫn tới file Excel của bạn
df = load_data(file_path)



def generate_cccd():
    # Chọn ngẫu nhiên tỉnh từ danh sách
    tinh = random.choice(list(ma_tinh_dict.keys()))
    ma_tinh = ma_tinh_dict[tinh]
    address, town = generate_random_address(tinh, df)

    if address:
        print(f"Địa chỉ: {address}")
        print(f"Thị trấn/Xã: {town}")
    else:
        print("Không thể lấy dữ liệu địa chỉ.")
    # Chọn ngẫu nhiên giới tính (2 cho Nam, 3 cho Nữ)
    gioi_tinh = random.choice(["2", "3"])
    
    ns = str(random.randint(1, 5) + 2000)
    # Chọn ngẫu nhiên năm sinh từ 2001 đến 2005
    nam_sinh = ns[2:]  # Lấy 2 chữ số cuối (01 đến 05)
    
    # Tạo 6 số ngẫu nhiên cho phần cuối
    so_cuoi = "".join([str(random.randint(0, 9)) for _ in range(6)])

    # Kết hợp tất cả lại thành CCCD
    cccd = ma_tinh + gioi_tinh + nam_sinh + so_cuoi
    
    family, middle, given = generate_vietnamese_name()
    sdt = generate_vietnam_phone_number()
    return cccd, tinh, gioi_tinh, generate_random_birthdate(ns), tinh_zipcodes[tinh], address, town, family, middle, given, sdt

# Kết nối tới ứng dụng WebBrowser.exe
def connect_to_application():
    try:
        app = Application(backend="uia").connect(path="WebBrowser.exe", timeout=10)
        return app.top_window()  # Trả về cửa sổ chính
    except findwindows.ElementNotFoundError:
        print("Không tìm thấy ứng dụng WebBrowser.exe. Vui lòng đảm bảo ứng dụng đang chạy.")
        exit(1)


def simulate_typing(field, text):
    for char in text:
        if char == ' ':
            send_keys('{SPACE}')  # Gửi phím cách явный
        else:
            field.type_keys(char)
        # time.sleep(random.uniform(0.05, 0.1))  # Thêm độ trễ ngẫu nhiên giữa các ký tự
    time.sleep(random.uniform(0.2, 0.3))

def fill_text_field(email,window, auto_id, text, timeout=5):
    while True:
        try:
            field = window.child_window(auto_id=auto_id, control_type="Edit")
            field.set_edit_text("")  # Xóa nội dung cũ
            simulate_typing(field, text)
            print(f"Đã nhập '{text}' vào ô {auto_id}.")
            break
        except findwindows.ElementNotFoundError:
            print(f"Không tìm thấy ô {auto_id}. Đang tìm lại...")
            timeout-=1
            time.sleep(1)
        finally:
            if timeout <= 0:
                raise Exception(f"Không tìm thấy ô {auto_id} sau thời gian chờ.")

def simulate_mouse_click(button):
    # Lấy vị trí giữa của control (vị trí click)
    global stop_mouse_thread
    stop_mouse_thread = True
    rect = button.rectangle()
    target_x = (rect.left + rect.right) // 2 + random.randint(-3, 3)
    target_y = (rect.top + rect.bottom) // 2 + random.randint(-3, 3)

    # Di chuyển chuột từ từ tới vị trí đó
    pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.4, 0.8))

    time.sleep(random.uniform(0.1, 0.3))  # Delay trước khi click
    pyautogui.click()
    time.sleep(random.uniform(0.3, 0.7))  # Delay sau khi click
    stop_mouse_thread = False

def find_and_click_button(email,window, title, auto_id, control_type, timeout=5):
    
    while True:
        try:
            button = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
            button.wait("exists ready", timeout=1)
            simulate_mouse_click(button)
            print(f"Đã nhấn vào nút '{title}'.")
            break
        except findwindows.ElementNotFoundError:
            print(f"Không tìm thấy nút '{title}'. Tiếp tục tìm lại...")
        except Exception as e:
            print(f"Lỗi khi tìm/nhấn nút: {e}")
        
        timeout -= 1
        if timeout <= 0:
            raise Exception(f"Không tìm thấy ô {auto_id} sau thời gian chờ.")

        time.sleep(1)

# Ghi cây control vào file temp.txt
def save_control_tree_to_file(window):
    with open("temp.txt", "w", encoding="utf-8") as f:
        sys.stdout = f
        window.print_control_identifiers()
    sys.stdout = sys.__stdout__  # Trả lại stdout về mặc định
    print("Cây control đã được lưu vào temp.txt.")
def delete_folder(folder_name):
    base_path = r"D:\\TOOLS_KT\\1_Paypal\\Create_Paypal\\Create_Paypal\\Create_Paypal\\profile"
    target_path = os.path.join(base_path, folder_name)

    if os.path.exists(target_path) and os.path.isdir(target_path):
        shutil.rmtree(target_path)
        print(f"Đã xóa thư mục: {target_path}")
    else:
        print(f"Thư mục không tồn tại: {target_path}")

def check_security_challenge(window,email):
    try:
        element = window.child_window(
            title="Security Challenge",
            control_type="Text"
        )
        element.wrapper_object()  # Nếu không tồn tại sẽ raise lỗi
        print("Phát hiện Security Challenge")
        find_and_click_button(email,window, title="Restart", auto_id="btn_restart", control_type="Button")
        time.sleep(2)
        delete_folder(email) # xóa profile
        return True
    except ElementNotFoundError:
        print("Không có Security Challenge")
        return False
def verify_email(window):
    global last_mxn
    while True:
        if last_mxn:
            break
    for (i, digit) in enumerate(last_mxn):
        try:
            auto_id = f"ci-email-confirmation-input-{i}"
            spinner = window.child_window(auto_id=auto_id, control_type="Spinner")
            spinner.set_focus()
            spinner.type_keys(digit, with_spaces=True)
            print(f"Đã nhập số {digit} vào ô thứ {i+1}")
        except ElementNotFoundError:
            print(f"Không tìm thấy ô nhập mã thứ {i+1}")
    with lock:
        last_mxn = None
def check_verfiemail_challen(window,email):
    try:
        element = window.child_window(
            title="Confirm your email", auto_id="paypalAccountData_emailVerificationModalHeading", control_type="Text"
        )
        element.wrapper_object()  # Nếu không tồn tại sẽ raise lỗi
        print("Phát hiện Email Challenge")
        verify_email(window)
        return True
    except ElementNotFoundError:
        print("Không có Email Challenge")
        return False

# Chính thức thực hiện các bước
def scroll_to_bottom(window):
    try:
        # Tìm paneControl6
        pane = window.child_window(title="Sign Up for a Personal Account | PayPal", auto_id="RootWebArea", control_type="Document")
        
        # Đặt focus vào paneControl6 để đảm bảo nó nhận các sự kiện bàn phím
        pane.set_focus()
        
        # Mô phỏng cuộn xuống bằng phím DOWN
        # Sử dụng vòng lặp để cuộn nhiều lần, đảm bảo xuống cuối
        for _ in range(4):  # Số lần cuộn có thể điều chỉnh tùy theo nội dung
            send_keys('{DOWN}')
            time.sleep(0.5)  # Thêm độ trễ để giao diện cập nhật
        
        print("Đã cuộn paneControl6 xuống cuối.")
        
    except Exception as e:
        print(f"Lỗi khi cuộn paneControl6: {e}")
def runn(email, password):
    window = connect_to_application()

    global stop_mouse_thread
    stop_mouse_thread = False
    panel = window.child_window(title="panelControl6", auto_id="panelControl6", control_type="Pane")
    t = threading.Thread(target=mouse_mover_thread, args=(panel,), daemon=True)
    t.start()
    email = email
    password = password
    cccd, tinh, gioi_tinh, nam_sinh, tinh_zipcode , address, town, family, middle, given, sdt = generate_cccd()

    # cccd, tinh, gioi_tinh, nam_sinh, tinh_zipcode , address, town, family, middle, given, sdt = "051203972367", "Quảng Ngãi", "2","08012003","570000", "25 đường số 1 Bình Sơn Quảng Ngãi", "Bình Sơn", "Nguyễn", "Anh", "Tính", "0934432516"
    print(f"CCCD: {cccd}, Tỉnh: {tinh}, Giới tính: {gioi_tinh}, Năm sinh: {nam_sinh}, Zipcode: {tinh_zipcode}, Địa chỉ: {address}, Thị trấn/Xã: {town}, Họ: {family}, Tên đệm: {middle}, Tên: {given}, SĐT: {sdt}")
    # Bước 1: Xóa và nhập "test2@gmail.com" vào ô Profile name
    try:
        fill_text_field(email,window, auto_id="txt_profile", text=email)

        # Bước 2: Xóa và nhập "ahihi" vào ô Password
        fill_text_field(email,window, auto_id="textEdit6", text=password)

        find_and_click_button(email,window, title="Create Profile", auto_id="btn_newprofile", control_type="Button")
        time.sleep(random.uniform(7, 10)) 

        # Bước 3: Nhấn nút Go
        find_and_click_button(email,window, title="Go", auto_id="btn_go", control_type="Button")
        time.sleep(5)  # Đợi 3 giây để tải trang
        # Bước 4: Nhấn nút Sign Up
        find_and_click_button(email,window, title="Sign Up", auto_id="_signup-button_1j7nc_1", control_type="Hyperlink")
        time.sleep(random.uniform(3, 4)) 
        #Chấp nhận cookie
        find_and_click_button(email,window, title="Yes, Accept Cookies", auto_id="acceptAllButton", control_type="Button", timeout=1)
        time.sleep(1) 
        # Bước 5: Nhấn nút Next
        find_and_click_button(email,window, title="Next", auto_id="next-btn", control_type="Button")
        time.sleep(random.uniform(3, 4)) 


        fill_text_field(email,window, auto_id="paypalAccountData_email", text=email)
        find_and_click_button(email,window, title="Next", auto_id="paypalAccountData_submit", control_type="Button")
        time.sleep(random.uniform(3, 4)) 

        if check_security_challenge(window,email) == True:
            print("Bị bắt xác thực")
            return

        fill_text_field(email,window, auto_id="paypalAccountData_phone", text=sdt)
        find_and_click_button(email,window, title="Next", auto_id="paypalAccountData_submit", control_type="Button")
        time.sleep(random.uniform(3, 4)) 

        fill_text_field(email,window, auto_id="paypalAccountData_password", text=password)
        find_and_click_button(email,window, title="Next", auto_id="paypalAccountData_submit", control_type="Button")
        time.sleep(random.uniform(3, 4)) 

        fill_text_field(email,window, auto_id="paypalAccountData_lastName", text=family)
        time.sleep(random.uniform(0.2, 0.8)) 
        fill_text_field(email,window, auto_id="paypalAccountData_middleName", text=middle) 
        time.sleep(random.uniform(0.2, 0.8)) 
        fill_text_field(email,window, auto_id="paypalAccountData_firstName", text=given) 
        time.sleep(random.uniform(0.2, 0.8)) 

        find_and_click_button(email,window, title="Next", auto_id="paypalAccountData_emailPassword", control_type="Button") #chưa chuẩn
        time.sleep(random.uniform(2, 3)) 

        find_and_click_button(email,window, title="Next", auto_id="paypalAccountData_emailPassword", control_type="Button") #chưa chuẩn
        time.sleep(random.uniform(3, 4)) 


        fill_text_field(email,window, auto_id="paypalAccountData_identificationNum", text=cccd) 
        time.sleep(random.uniform(0.2, 0.8)) 
        fill_text_field(email,window, auto_id="paypalAccountData_dob", text=nam_sinh) #MMDDYYYY 
        time.sleep(random.uniform(0.2, 0.8)) 

        find_and_click_button(email,window, title="Next", auto_id="paypalAccountData_emailPassword", control_type="Button") #chuẩn
        time.sleep(random.uniform(3, 4)) 


        
        fill_text_field(email,window, auto_id="paypalAccountData_address1_0", text=address) 
        time.sleep(random.uniform(0.2, 0.8)) 
        fill_text_field(email,window, auto_id="paypalAccountData_city_0", text=town) 
        time.sleep(random.uniform(0.2, 0.8)) 



        fill_text_field(email,window, auto_id="paypalAccountData_zip_0", text=tinh_zipcode)
        time.sleep(1)

        checkbox_agree = window.child_window(
            auto_id="paypalAccountData_termsAgree",
            control_type="CheckBox"
        )
        checkbox_agree.click_input()

        # Tick checkbox nhận khuyến mãi
        checkbox_promo = window.child_window(
            auto_id="paypalAccountData_marketingOptIn",
            control_type="CheckBox"
        )
        checkbox_promo.click_input()
        time.sleep(2)  # Đợi 3 giây để tải trang

        scroll_to_bottom(window)


        find_and_click_button(email,window, title="Larger city / Province", auto_id="dropdownMenuButton_paypalAccountData_state_0", control_type="Button") #chuẩn
        time.sleep(2)  # Đợi 3 giây để tải trang
        find_and_click_button(email,window,title="An Giang", auto_id="smenu_item_An Giang", control_type="ListItem")
    
        
        
        
        time.sleep(2)  # Đợi 3 giây để tải trang
        find_and_click_button(email,window,title="Agree and Create account", auto_id="paypalAccountData_emailPassword", control_type="Button")
        time.sleep(8)

        
    
        find_and_click_button(email,window, title="Not now", auto_id="paypalAccountData_notNow", control_type="Hyperlink")
        time.sleep(5)

        # Truy cập vào Document chứa nội dung web
        document = window.child_window(title="PayPal: Wallet", control_type="Document")

        # Đảm bảo Document được focus
        document.set_focus()

        # Cuộn xuống để hiển thị liên kết "Not now"
        # Sử dụng send_keys để mô phỏng thao tác cuộn (có thể cần điều chỉnh số lần nhấn)
        for _ in range(10):  # Thử cuộn xuống 10 lần (có thể điều chỉnh)
            document.type_keys("{DOWN}")
            time.sleep(0.3)  # Đợi một chút để giao diện cập nhật

        # Tùy chọn: Kiểm tra xem liên kết "Not now" có hiển thị không
        not_now_link = document.child_window(title="Not now", control_type="Hyperlink")
        if not_now_link.exists():
            print("Liên kết 'Not now' đã hiển thị.")
            not_now_link.set_focus()  # Focus vào liên kết
            not_now_link.click_input()
            print("Đã nhấn vào liên kết 'Not now'.")
        else:
            print("Không tìm thấy liên kết 'Not now'.")


        try:
            # Thử tìm Hyperlink
            hyperlink = window.child_window(
                title_re="^Submit info to access your funds.*",
                control_type="Hyperlink"
            )
            hyperlink.wrapper_object()  # Nếu không có sẽ raise lỗi

            print("Tài khoản lỗi")

            find_and_click_button(email,window, title="Restart", auto_id="btn_restart", control_type="Button")
            time.sleep(3)
            delete_folder(email) # xóa profile
            

        except ElementNotFoundError:
            print("Tài khoản thành công")
            time.sleep(2)
            find_and_click_button(email,window,title="Settings", auto_id="header-settings", control_type="Hyperlink")
            time.sleep(5)
            find_and_click_button(email,window,title="Confirm Your Email", auto_id="interstitial-button-1", control_type="Button")
            time.sleep(2)

            verify_email(window)

            find_and_click_button(email,window, title="Restart", auto_id="btn_restart", control_type="Button")
            time.sleep(2)
        # loginn = child_window(title="All done? We’ll log you out in a few moments. Stay Logged In", control_type="Group")
        # loginn.click_input()

    except Exception as e:
        print(f"Lỗi trong quá trình thực hiện: {e}")
        find_and_click_button(email,window, title="Restart", auto_id="btn_restart", control_type="Button")
        time.sleep(5)
        delete_folder(email) # xóa profile
    finally:
        stop_mouse_thread = True
        t.join()
        print("Kết thúc Một lần")
        # Xử lý lỗi nếu cần thiết


def reset_server():
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get("status") == "success":
            info = data.get("info", {})
            print("✅ Đổi IP thành công:")
            print("✅ Vui lòng đợi 10s...")
            time.sleep(10)
            return True

        elif data.get("status") == "error":
            error_msg = data.get("error", "")
            print("⚠️ Lỗi:", error_msg)

            # Trích số giây cần chờ
            match = re.search(r'(\d+)\s*giây', error_msg)
            if match:
                wait_seconds = int(match.group(1)) + 3
                print(f"⏳ Chờ {wait_seconds} giây trước khi thử lại...")
                # time.sleep(wait_seconds)
                for i in range(wait_seconds, 0, -1):
                    print(f"⏳ Còn {i} giây...", end='\r', flush=True)
                    time.sleep(1)
                print()
                return False
            else:
                print("Không xác định thời gian chờ.")
                return False
        else:
            print("❓ Phản hồi không xác định:", data)
            return False

    except requests.RequestException as e:
        print("❌ Request lỗi:", e)
        return False
    except ValueError:
        print("❌ Không phải JSON hợp lệ.")
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

            with lock:
                if m := email_pattern.match(line):
                    last_email = m.group(1)
                    print(f"[Thread] ==> Email nhận được: {last_email}")
                elif m := mxn_pattern.match(line):
                    last_mxn = m.group(1)
                    print(f"[Thread] ==> MXN nhận được: {last_mxn}")

    except Exception as e:
        print(f"[Thread] Lỗi: {e}")

def start_watcher():
    global current_process, current_thread

    if current_process:
        current_process.terminate()
        current_process.wait()

    current_process = subprocess.Popen(
        ['python', './mailer.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        env=env,
        creationflags=subprocess.CREATE_NO_WINDOW
    )
    print("[Main] Đã khởi động tiến trình con mailer.py")
    current_thread = threading.Thread(target=reader_thread_fn, args=(current_process,), daemon=True)
    current_thread.start()


def mouse_mover_thread(panel):
    rect = panel.rectangle()  # Lấy vùng tọa độ của panelControl6
    left, top, right, bottom = rect.left, rect.top, rect.right, rect.bottom
    x = None
    y = None
    if x is None or y is None:
        last_mouse_pos = pyautogui.position()
    idle_timeout = 1.5

    while not stop_mouse_thread:
        current_mouse_pos = pyautogui.position()

        if current_mouse_pos.x != last_mouse_pos[0] or current_mouse_pos.y != last_mouse_pos[1]:
            last_mouse_pos = (current_mouse_pos.x,current_mouse_pos.y)
            time.sleep(idle_timeout)
            continue

        x = random.randint(left + 10, right - 100)
        y = random.randint(top + 10, bottom - 200)
        last_mouse_pos = (x,y)
        pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.5))

while True:
    while True: 
        status = reset_server()
        if status:
            break
    print("[Main] 🔁 Đang khởi động lại server PROXY")
    last_email = None
    last_mxn = None
    start_watcher()
    while True:
        with lock:
            if last_email:
                break
    runn(last_email, GLOBAL_PASSWORD)
    
