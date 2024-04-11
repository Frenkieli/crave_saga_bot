from PyQt5.QtWidgets import QLabel, QPushButton
from templates.BaseWindowPage import BaseWindow
from views.InHomePage import InHomePageWindow
from utils import getImages, fineView, randomClick

class EntranceMainWindow(BaseWindow):
    def __init__(self):

        super().__init__("導航輔助工具", (100, 100, 360, 800))

    def setupUI(self):
        # 載入並顯示圖片
        self.label = QLabel()
        self.label.setPixmap(getImages.get_language_specific_image("entrance"))
        self.layout.addWidget(self.label)

        # 新增說明文字
        self.instruction = QLabel("請先開啟網頁，並將網頁切換至這個畫面後再開啟本視窗點擊確認到達")
        self.layout.addWidget(self.instruction)

        # 新增按鈕
        self.button = QPushButton("確認到達")
        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.button)

    def on_button_click(self):
        self.hide()  # 隱藏目前視窗
        page_position = self.check_page_arrival()

        if page_position:
            # 建立後續邏輯頁面的實例並傳遞位置和大小參數
            self.follow_up_window = InHomePageWindow(
                page_position[0][0] - 360 , page_position[0][1], 360, page_position[1][0])
            self.follow_up_window.show()  # 顯示後續邏輯頁面
        else:
            # 處理未偵測到頁面的情況
            print("頁面偵測失敗，請再嘗試")
            self.button.setText("頁面偵測失敗，請再嘗試")
            self.button.setStyleSheet("QPushButton { color: red; }")
            self.show()  # 重新顯示視窗

    def check_page_arrival(self):
        pixmap = getImages.get_language_specific_image("entrance")
        found_view = fineView.find_view(pixmap)
        print("found_view: ", found_view)
        if(found_view):
            randomClick.random_click([found_view[0][0] - 360, found_view[0][1]], found_view[1])
        return found_view
