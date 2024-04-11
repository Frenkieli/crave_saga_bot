import cv2
import pyautogui
import tempfile
import os
import numpy as np
import time

def find_view(pixmap, threshold=0.99):
  time.sleep(1)

  # 載入按鈕圖像
  temp_path = save_pixmap_to_temp(pixmap)

  image = cv2.imread(temp_path, cv2.IMREAD_UNCHANGED)
  
  # 螢幕截圖並轉換成OpenCV格式
  screenshot = pyautogui.screenshot()
  screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

  # 影像匹配
  result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

  os.remove(temp_path)  # 刪除臨時文件

  # 如果找到了匹配的圖像，返回其位置
  if max_val >= threshold:
    return max_loc, image.shape
  return None

def save_pixmap_to_temp(pixmap):
  # 建立臨時文件
  temp_file, temp_path = tempfile.mkstemp(suffix='.jpg')
  os.close(temp_file)  # 關閉檔案

  # 儲存 QPixmap 到暫存文件
  pixmap.save(temp_path, 'JPG')
  
  return temp_path