import pyautogui
import keyboard
import time

def main():
    try:
        print("正在偵測滑鼠位置，按 'Esc' 鍵停止...")
        while True:
            x, y = pyautogui.position()
            print(f"滑鼠位置：({x}, {y})")

            if keyboard.is_pressed('esc'):
                print("停止")
                break

            # 等待 0.5 秒
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n程式被中斷。")

if __name__ == "__main__":
    main()
