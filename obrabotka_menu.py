import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from teacher_menu import Ui_MenuChoice #первое окно откуда открывать
from Ui_Anketa import Ui_Anketa  #что открывается
from prof_window import Ui_ProfWindow #что открывается
from items_window import Ui_itemsWindow #что открывается

class TeacherMenu(QMainWindow, Ui_MenuChoice):
    def __init__(self):
        super().__init__()

        self.abiturAnketaWindow = Ui_Anketa(self.load_anketas)
        self.proffWindow = Ui_ProfWindow(self.load_proff)
        self.itemsWindow = Ui_itemsWindow(self.load_items)
        self.setupUi(self)

        self.Button_Proff.clicked.connect(self.showProffWindow)
        self.Button_Items.clicked.connect(self.showItemsWindow)
        self.Button_Students.clicked.connect(self.showAbiturAnketaWindow)

    def showAbiturAnketaWindow(self):
        self.abiturAnketaWindow.show()

    def showProffWindow(self):
        self.proffWindow.show()

    def showItemsWindow(self):
        self.itemsWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TeacherMenu()
    ex.show()
    sys.exit(app.exec())