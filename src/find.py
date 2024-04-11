from PyQt5.QtWidgets import QApplication
import sys
from utils import getImages, fineView, waitTime
from functools import partial

def print_not_found():
    print("not found")
app = QApplication(sys.argv)

def main(key, threshold):
    pixmap = getImages.get_language_specific_image(key)
    found_view = fineView.find_view(pixmap, threshold)
    if found_view:
        print("found_view: ", found_view)
        return True
    return False

waitTime.wait_and_execute(partial(main, "TAP_START", 0.96), print_not_found, 0.2, 20)