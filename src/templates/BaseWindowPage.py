from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class BaseWindow(QMainWindow):
    def __init__(self, title, geometry):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(*geometry)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口为无边框
        self.initUI()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:  # 检测是否按下了 ESC 键
            self.close()  # 关闭窗口

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.setupUI()

    def setupUI(self):
        # 由子类实现具体的UI设置
        pass
