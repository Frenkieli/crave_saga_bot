import os
import cv2
import pyautogui
import numpy as np
import time
import random  # 导入random库

def find_button(button_image_path, threshold=0.9):
    # 加载按钮图像
    button_image = cv2.imread(button_image_path, cv2.IMREAD_UNCHANGED)
    
    # 屏幕截图并转换成OpenCV格式
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 图像匹配
    result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 如果找到了匹配的图像，返回其位置
    if max_val >= threshold:
        return max_loc, button_image.shape
    return None

def click_button(button_position, button_size):
    # 为点击位置添加随机偏移量，使点击不总是在按钮的正中央
    x_offset = random.randint(-button_size[1] // 4, button_size[1] // 4)
    y_offset = random.randint(-button_size[0] // 4, button_size[0] // 4)
    button_center = (button_position[0] + button_size[1] // 2 + x_offset, 
                     button_position[1] + button_size[0] // 2 + y_offset)

    # 移动鼠标并点击
    pyautogui.click(button_center)

def wait_for_button_and_click(button_image_path, threshold=1, timeout=99):

    start_time = time.time()
    while True:
        position = find_button(button_image_path, threshold)
        if position:
            time.sleep(0.2)  # 等待一小段时间，确保按钮已经完全出现在屏幕上
            click_button(position[0], position[1])
            break
        elif time.time() - start_time > timeout:
            raise TimeoutError(f"Button not found within {timeout} seconds.")
        # 在尝试之间等待一个随机的时间
        time.sleep(random.uniform(0.2, 0.7))

def check_and_click_additional_button(button_image_path, threshold=0.9, check_duration=10):
    start_time = time.time()
    while time.time() - start_time < check_duration:
        position = find_button(button_image_path, threshold)
        if position:
            click_button(position[0], position[1])
            return True  # 找到并点击了图片
        time.sleep(0.5)  # 每次检查之间稍作等待
    return False  # 指定时间内未找到图片


# 在主循环中使用 wait_for_button_and_click 函数等待确认按钮出现
def main_loop():
    try:
        while True:
            # 步骤 1: 点参战按钮
            wait_for_button_and_click('assets/images/zh-tw/1_participate_button.jpg', threshold=0.97)
            
            # # 步骤 2: 点決定按钮
            wait_for_button_and_click('assets/images/zh-tw/2_ok_button.jpg', threshold=0.97)


            # # 步骤 3: 点出级按钮
            wait_for_button_and_click('assets/images/zh-tw/3_level_button.jpg', threshold=0.99)

            # 新增步骤: 检查并点击特定图片（如果存在），如果找到则从步骤一重新开始
            if check_and_click_additional_button('assets/images/zh-tw/ok_button.jpg', threshold=0.98, check_duration=10):
                continue  # 如果找到图片并点击，则继续从头开始

            # 步骤 4: 等待战斗结束（确认按钮出现）
            wait_for_button_and_click('assets/images/zh-tw/4_confirm_button.jpg', threshold=0.94, timeout=999999999)

            # 步骤 5: 点前往下一页按钮
            wait_for_button_and_click('assets/images/zh-tw/5_next_page_button.jpg', threshold=0.99)

            # 步骤 6: 点冒险任务一览
            wait_for_button_and_click('assets/images/zh-tw/6_adventure_list_button.jpg', threshold=0.99)

    except TimeoutError as e:
        print(e)  # 打印错误信息
        shutdown_system()  # 执行关机命令

def shutdown_system():
    try:
        # 对于Windows
        if os.name == 'nt':
            os.system('shutdown /s /t 1')
        # 对于Unix-like系统
        else:
            os.system('shutdown -h now')
    except Exception as e:
        print(f"Error shutting down: {e}")

if __name__ == '__main__':
    main_loop()
