from PyQt5.QtWidgets import QLabel, QPushButton
from templates.BaseWindowPage import BaseWindow  # 导入BaseWindow类
from views.FollowUpPage import FollowUpMainWindow  # 引入后续逻辑页面的类
from utils import getImages, fineView

class EntranceMainWindow(BaseWindow):
    def __init__(self):
        # 调用基类构造器，传递标题和几何尺寸
        super().__init__("导航辅助工具", (100, 100, 1200, 800))

    def setupUI(self):
        # 加载并显示图片
        self.label = QLabel()
        self.label.setPixmap(getImages.get_language_specific_image("entrance"))
        self.layout.addWidget(self.label)

        # 添加说明文字
        self.instruction = QLabel("请先打开网页，并将网页切换至这个画面后再打开本窗口点击确认到达")
        self.layout.addWidget(self.instruction)

        # 添加按钮
        self.button = QPushButton("确认到达")
        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.button)

    def on_button_click(self):
        self.hide()  # 隐藏当前窗口
        page_position = self.check_page_arrival()

        if page_position:
            # 创建后续逻辑页面的实例并传递位置和大小参数
            self.follow_up_window = FollowUpMainWindow(
                page_position[0][0] + 1, page_position[0][1], 399, page_position[1][0])
            self.follow_up_window.show()  # 显示后续逻辑页面
        else:
            # 处理未检测到页面的情况
            print("页面检测失败，请再次尝试")
            self.button.setText("页面检测失败，请再次尝试")
            self.button.setStyleSheet("QPushButton { color: red; }")
            self.show()  # 重新显示窗口

    def check_page_arrival(self):
        pixmap = getImages.get_language_specific_image("entrance")
        found_view = fineView.find_view(pixmap)
        return found_view
