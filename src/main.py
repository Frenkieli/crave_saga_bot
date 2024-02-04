import tkinter as tk
from PIL import Image, ImageTk
from static import pic2str
import base64
import io

# 假設您有一個變量或函數來決定當前的語言代碼
current_language_code = "zh_tw"  # 這個值可以根據您的需要動態變化

def get_image_from_base64(base64_string):
    image_data = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_data))
    return ImageTk.PhotoImage(image)

def get_language_specific_image(language_code, image_base_name):
    variable_name = f"{language_code}_{image_base_name}"
    base64_string = getattr(pic2str, variable_name)
    return get_image_from_base64(base64_string)

def on_button_click():
    print("已確認到達指定頁面")
    # 在這裡添加你需要執行的操作

# 建立主視窗
root = tk.Tk()
root.title("導航輔助工具")
root.geometry("1200x800")  # 設定視窗大小
root.resizable(False, False)  # 禁止大小調整
root.attributes('-topmost', True)  # 設置窗口始終保持在最前面

# 設置窗口圖標
favicon_image = get_image_from_base64(pic2str.favicon)
root.tk.call('wm', 'iconphoto', root._w, favicon_image)

# 加載並顯示根據語言設置的圖片
entrance_image = get_language_specific_image(current_language_code, "entrance")
label = tk.Label(root, image=entrance_image)
label.pack(pady=20)  # 在Y軸方向增加一些間隙

# 添加說明文字和按鈕
instruction = tk.Label(root, text="請先開啟網頁，並將網頁切換至這個畫面後開啟本視窗點擊確定到達")
instruction.pack()  # 添加到視窗中

button = tk.Button(root, text="確定到達", command=on_button_click)
button.pack()

# 啟動事件迴圈
root.mainloop()
