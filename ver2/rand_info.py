import random
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
    "An Giang": "089", "Bắc Giang": "024", "Bắc Kạn": "006", "Bạc Liêu": "095",
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