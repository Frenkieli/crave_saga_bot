# randomClick.py
import pyautogui
import random
import time

def random_click(position, size, wait_time=0):
    """
    在給定的範圍內隨機點擊，並在點擊前等待指定的時間。
    
    :param position: 一個元組，表示匹配圖像在螢幕上的左上角座標 (x, y)。
    :param size: 一個元組，表示匹配圖像的尺寸 (width, height)。
    :param wait_time: 點擊前的等待時間（秒）。默認為 0 秒。
    """
    if wait_time > 0:
        time.sleep(wait_time)  # 在點擊前等待指定的時間

    time.sleep(random.uniform(0.2, 0.7))

    # 計算點擊範圍
    x_start, y_start = position
    height, width , _ = size
    x_end = x_start + width
    y_end = y_start + height

    # 在範圍內生成隨機點擊座標
    x_click = random.randint(x_start, x_end)
    y_click = random.randint(y_start, y_end)

    # 執行點擊
    pyautogui.click(x_click, y_click)

