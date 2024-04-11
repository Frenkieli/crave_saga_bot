# src\main.py

from PyQt5.QtWidgets import QApplication
from views import EntrancePage  # 从views模块导入EntranceMainWindow
import sys

def main():
    app = QApplication(sys.argv)
    main_window = EntrancePage.EntranceMainWindow()
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
