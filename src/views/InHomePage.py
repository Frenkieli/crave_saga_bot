from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QTimer, Qt
from templates.BaseWindowPage import BaseWindow  # 导入BaseWindow类
from utils import getImages, fineView, randomClick, waitTime
import time

class InHomePageWindow(BaseWindow):
    def __init__(self, x, y, width, height):
        # 呼叫基類構造器，傳遞標題和幾何尺寸
        super().__init__("進入遊戲頁面", (x, y, width, height))
        # 設定視窗始終保持在最前面
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

    def setupUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        self.layout = layout

        layout.addStretch()

        # 定義特定於InHomePageWindow的UI元件
        layout.addWidget(QLabel("正在進入遊戲頁面..."))
    
        layout.addWidget(QLabel("找尋 OK 按鈕並點擊..."))

        QTimer.singleShot(100, self.check_and_click_ok_btn)
        

    def check_and_click_ok_btn(self, threshold= .91):
        pixmap = getImages.get_language_specific_image("ok_btn")
        found_view = fineView.find_view(pixmap, threshold)
        print("found_view: ", found_view)
        if found_view:
            randomClick.random_click(found_view[0], found_view[1])
            self.layout.addWidget(QLabel("已點擊 OK 按鈕，等待進入遊戲..."))
            QTimer.singleShot(100, self.check_loading_finish)

        else:
            self.layout.addWidget(QLabel("未找到 OK 按鈕，正在請重新尋找..."))
            QTimer.singleShot(100, self.check_and_click_ok_btn)
            self.check_and_click_ok_btn(threshold=threshold - .01)

    def check_loading_finish(self):
        self.layout.addWidget(QLabel("正在檢查遊戲載入狀態..."))
        pixmap = getImages.get_language_specific_image("TAP_START")
        found_view = fineView.find_view(pixmap, 0.95)

        if found_view:
            self.layout.addWidget(QLabel("遊戲載入完成，請開始遊戲..."))
            randomClick.random_click(found_view[0], found_view[1])

        else:
            QTimer.singleShot(500, self.check_loading_finish)