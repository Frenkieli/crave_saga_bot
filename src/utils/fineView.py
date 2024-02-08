import cv2
import pyautogui
import tempfile
import os
import numpy as np
import time

def find_view(pixmap, threshold=0.99):
  time.sleep(1)

  # 加载按钮图像
  temp_path = save_pixmap_to_temp(pixmap)

  image = cv2.imread(temp_path, cv2.IMREAD_UNCHANGED)
  
  # 屏幕截图并转换成OpenCV格式
  screenshot = pyautogui.screenshot()
  screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

  # 图像匹配
  result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

  os.remove(temp_path)  # 删除临时文件

  # 如果找到了匹配的图像，返回其位置
  if max_val >= threshold:
    return max_loc, image.shape
  return None

def save_pixmap_to_temp(pixmap):
  # 创建临时文件
  temp_file, temp_path = tempfile.mkstemp(suffix='.jpg')
  os.close(temp_file)  # 关闭文件句柄

  # 保存 QPixmap 到临时文件
  pixmap.save(temp_path, 'JPG')
  
  return temp_path