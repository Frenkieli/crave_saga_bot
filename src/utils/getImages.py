import io
from PyQt5.QtGui import QPixmap, QIcon
import base64

from models import language
from static import pic2str

def get_ico():
  return QIcon(get_image_from_base64(pic2str.favicon))

def get_image_from_base64(base64_string):
  image_data = base64.b64decode(base64_string)
  pixmap = QPixmap()
  pixmap.loadFromData(image_data)
  return pixmap

def get_language_specific_image(image_base_name):
  variable_name = f"{language.current_language_code}_{image_base_name}"
  base64_string = getattr(pic2str, variable_name)
  return get_image_from_base64(base64_string)
