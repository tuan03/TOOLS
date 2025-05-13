import pywinauto
from pywinauto.application import Application
import pyautogui
import numpy as np
import random
from scipy.interpolate import CubicSpline
from pywinauto.keyboard import send_keys
import string
import time
from pywinauto import findwindows

pyautogui.FAILSAFE = True  # Kích hoạt chế độ an toàn
pyautogui.PAUSE = random.uniform(0.01, 0.03)  # Thêm độ trễ nhỏ sau mỗi hành động

def click_create_acc(window,auto_id="btn_newprofile", control_type="Button"):
    # Tìm control theo tên (panel)
    panel = window.child_window( auto_id=auto_id, control_type=control_type)
    panel_rect = panel.rectangle() 
    x = (panel_rect.left + panel_rect.right ) // 2
    y = (panel_rect.top + panel_rect.bottom) // 2
    pyautogui.click(x, y)

def go_to_url(window, url):
    # Tìm control theo tên (panel)
    panel = window.child_window(title="Go", auto_id="btn_go", control_type="Button")
    panel_rect = panel.rectangle() 
    x = panel_rect.left -100
    y = (panel_rect.top + panel_rect.bottom) // 2
    pyautogui.doubleClick(x, y)
    time.sleep(random.uniform(0.3, 0.5))
    pyautogui.typewrite(url)
    x = (panel_rect.left + panel_rect.right ) // 2
    y = (panel_rect.top + panel_rect.bottom) // 2
    pyautogui.click(x, y)

# Tạo đường đi cong tự nhiên cho chuột
def generate_smooth_path(start_x, start_y, end_x, end_y, num_points=3):
    t = np.linspace(0, 1, num_points)
    # Thêm nhiễu ngẫu nhiên để giống chuyển động con người
    x = np.linspace(start_x, end_x, num_points) + np.random.normal(0, 10, num_points)
    y = np.linspace(start_y, end_y, num_points) + np.random.normal(0, 10, num_points)
    cs_x = CubicSpline(t, x)
    cs_y = CubicSpline(t, y)
    smooth_t = np.linspace(0, 1, num_points * 2)
    return list(zip(cs_x(smooth_t), cs_y(smooth_t)))

# Di chuyển chuột mượt mà với đường cong ngẫu nhiên, thêm overshoot và điều chỉnh
def move_mouse_smoothly(from_x, from_y, to_x, to_y, num_points=3):
    # Tạo đường đi cong đến điểm đích
    points = generate_smooth_path(from_x, from_y, to_x, to_y, num_points)
    
    # Di chuyển qua các điểm trên đường cong
    for point in points:
        pyautogui.moveTo(point[0], point[1], duration=random.uniform(0.05, 0.15), tween=pyautogui.easeInOutQuad)
        time.sleep(random.uniform(0.005, 0.02))
    
    # Tính hướng di chuyển ban đầu (vector từ start đến end)
    direction_x = to_x - from_x
    direction_y = to_y - from_y
    
    # Tạo điểm overshoot: di chuyển lố theo hướng ngược lại
    overshoot_distance = random.uniform(50, 150)  # Khoảng cách overshoot ngẫu nhiên
    # Hướng ngược lại (đảo dấu vector hướng)
    overshoot_x = to_x + direction_x * overshoot_distance / np.sqrt(direction_x**2 + direction_y**2 + 1e-6)
    overshoot_y = to_y + direction_y * overshoot_distance / np.sqrt(direction_x**2 + direction_y**2 + 1e-6)
    
    # Di chuyển đến điểm overshoot
    pyautogui.moveTo(overshoot_x, overshoot_y, duration=random.uniform(0.1, 0.4), tween=pyautogui.easeInOutQuad)
    time.sleep(random.uniform(0.1, 0.2))
    
    # Quay lại điểm đích
    pyautogui.moveTo(to_x, to_y, duration=random.uniform(0.1, 0.4), tween=pyautogui.easeInOutQuad)


# Di chuyển chuột đến vị trí của một control và nhấn
def simulate_mouse_click_with_smooth_move(control):
    rect = control.rectangle()
    x_center = (rect.left + rect.right) // 2
    y_center = (rect.top + rect.bottom) // 2

    # Lấy vị trí chuột hiện tại
    current_x, current_y = pyautogui.position()

    # Di chuyển chuột mượt mà đến vị trí control
    move_mouse_smoothly(current_x, current_y, x_center, y_center)

    # Mô phỏng nhấp chuột đôi
    pyautogui.click()

    # Thêm độ trễ sau khi nhấp
    time.sleep(random.uniform(0.05, 0.1))

# Mô phỏng nhập liệu giống con người
def simulate_typing(field, text):
    simulate_mouse_click_with_smooth_move(field)
    time.sleep(random.uniform(0.1, 0.2))  # Đợi một chút trước khi nhập liệu
    my_tick = text.isdigit()
    for i, char in enumerate(text):
        if char == ' ':
            send_keys('{SPACE}')
        else:
            if random.random() < 0.05:  # 5% cơ hội gõ nhầm
                wrong_char = '1'
                if my_tick:
                    wrong_char = random.choice(string.digits)
                else:
                    wrong_char = random.choice(string.ascii_letters)
                field.type_keys(wrong_char)
                time.sleep(random.uniform(0.01, 0.04))
                field.type_keys('{BACKSPACE}')  # Xóa ký tự nhầm
            field.type_keys(char)
        if random.random() < 0.3:  # 30% cơ hội tạm dừng giữa các từ
            time.sleep(random.uniform(0.05, 0.1))
    time.sleep(random.uniform(0.1, 0.4))  # Tạm dừng ngắn sau khi nhập xong

# Tìm và nhấn nút hoặc nhập văn bản vào trường nhập liệu
def find_and_interact_with_control(window, control_type, auto_id, action_type, text=None, timeout=15):
    start_time = time.time()
    while True:
        try:
            control = window.child_window(auto_id=auto_id, control_type=control_type)
            control.wait("ready", timeout=1)
            
            if action_type == "click":
                simulate_mouse_click_with_smooth_move(control)
                print(f"Đã nhấn vào {auto_id}.")
            elif action_type == "type" and text is not None:
                simulate_typing(control, text)
                print(f"Đã nhập '{text}' vào {auto_id}.")
            break
        except findwindows.ElementNotFoundError:
            print(f"Không tìm thấy ô {auto_id}. Tiếp tục tìm lại...")
        except Exception as e:
            print(f"Lỗi khi tìm/nhấn/nhập vào {auto_id}: {e}")

        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout:
            raise Exception(f"Không tìm thấy {auto_id} sau {timeout} giây.")
        
        time.sleep(random.uniform(0.5, 2.0))


def fill_text_field(window, auto_id, text, timeout=5):
    while True:
        try:
            field = window.child_window(auto_id=auto_id, control_type="Edit")
            field.set_edit_text("")  # Xóa nội dung cũ
            field.type_keys(text, with_spaces=True)
            print(f"Đã nhập '{text}' vào ô {auto_id}.")
            break
        except findwindows.ElementNotFoundError:
            print(f"Không tìm thấy ô {auto_id}. Đang tìm lại...")
            timeout-=1
            time.sleep(1)
        if timeout <= 0:
            raise Exception(f"Không tìm thấy ô {auto_id} sau thời gian chờ.")
        


def simulate_mouse_interaction(window):
    """Mô phỏng hành vi chuột trước khi cuộn."""
    rect = window.rectangle()
    x_center = (rect.left + rect.right) // 2
    y_center = (rect.top + rect.bottom) // 2

    # Thêm độ lệch ngẫu nhiên nhỏ
    x_offset = int(random.gauss(0, 10))
    y_offset = int(random.gauss(0, 10))
    target_x = x_center + x_offset
    target_y = y_center + y_offset

    # Di chuyển chuột đến khu vực pane
    pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.2, 0.5), tween=pyautogui.easeInOutQuad)
    time.sleep(random.uniform(0.05, 0.2))

    # Nhấp chuột để kích hoạt khu vực
    pyautogui.click()
    if random.random() < 0.1:  # 10% cơ hội nhấp đúp (mô phỏng hành vi vô ý)
        pyautogui.click()

def scroll_to_bottom(window, max_attempts=10):
    """Mô phỏng hành vi cuộn xuống cuối trang bằng chuột, giống con người."""
    try:
        # Tìm pane
        pane = window.child_window(title="Sign Up for a Personal Account | PayPal", auto_id="RootWebArea", control_type="Document")
        pane.set_focus()
        time.sleep(random.uniform(0.1, 0.3))

        # Mô phỏng tương tác chuột trước khi cuộn
        if random.random() < 0.7:  # 70% cơ hội
            simulate_mouse_interaction(pane)

        # Lưu vị trí cuộn trước đó để kiểm tra (placeholder)
        last_scroll_position = None
        attempts = 0

        while attempts < max_attempts:
            # Cuộn chuột với biên độ ngẫu nhiên
            scroll_amount = random.randint(100, 400)  # Biên độ cuộn mỗi lần
            pyautogui.scroll(-scroll_amount)  # Cuộn xuống
            time.sleep(random.uniform(0.15, 0.4))  # Độ trễ ngẫu nhiên

            # Thêm hành vi cuộn ngược lên (mô phỏng sửa lỗi)
            if random.random() < 0.15:  # 15% cơ hội
                pyautogui.scroll(random.randint(50, 150))  # Cuộn lên một chút
                time.sleep(random.uniform(0.5, 1.2))
                pyautogui.scroll(-random.randint(100, 200))  # Cuộn xuống lại
                time.sleep(random.uniform(0.2, 0.5))

            # Tạm dừng ngẫu nhiên để mô phỏng đọc nội dung
            if random.random() < 0.4:  # 40% cơ hội
                time.sleep(random.uniform(1.0, 3.5))  # Dừng lâu hơn để đọc

            # Giả lập kiểm tra xem có đến cuối trang chưa
            # (Lưu ý: pywinauto không cung cấp API kiểm tra scrollHeight.
            # Nếu dùng trình duyệt, cần Selenium/Playwright để kiểm tra thực)
            attempts += 1

            # Placeholder cho kiểm tra trạng thái cuộn
            current_scroll_position = attempts
            if last_scroll_position == current_scroll_position:
                print("Đã cuộn đến cuối trang.")
                break
            last_scroll_position = current_scroll_position

        # Thêm hành vi phụ sau khi cuộn
        if random.random() < 0.3:  # 30% cơ hội
            pyautogui.move(random.randint(-20, 20), random.randint(-20, 20), duration=0.2)

        print("Đã cuộn pane xuống cuối.")
    except findwindows.ElementNotFoundError:
        raise Exception("Không tìm thấy pane với auto_id 'RootWebArea'.")
    except Exception as e:
        raise Exception(f"Lỗi khi cuộn trang: {e}")
# Ví dụ tìm và nhấn vào nút hoặc nhập văn bản
# find_and_interact_with_control(window, "Button", "btn_go", "click")
# find_and_interact_with_control(window, "Edit", "paypalAccountData_email", "type", text="Xin chào các bạn rất nhiều")
