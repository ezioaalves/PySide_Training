#IMPORT MODULES
import sys
import os

#IMPORT QT CORE
from qt_core import *

#IMPORT MAIN WINDOW
from gui.windows.main_win.ui_main_window import *

#MAIN WINDOW
class MainWindow(QMainWindow):
  def __init__(self):
      super().__init__()

      self.setWindowTitle("Curso de Python e Pyside6")

      #SETUP MAIN WINDOW
      self.ui = UI_MainWindow()
      self.ui.setup_ui(self)

      # TOGGLE BUTTON
      self.ui.toggle_button.clicked.connect(self.toggle_button)

      #EXIBE A NOSSA APLICAÇÃO
      self.show()
  
  def toggle_button(self):
    # GET MENU WIDTH
    menu_width = self.ui.left_menu.width()

    # CHECK WITH
    width = 50
    if menu_width == 50:
      width = 240
    
    # START ANIMATION
    self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
    self.animation.setStartValue(menu_width)
    self.animation.setEndValue(width)
    self.animation.setDuration(500)
    self.animation.setEasingCurve(QEasingCurve.InOutCirc)
    self.animation.start()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  sys.exit(app.exec())
  
