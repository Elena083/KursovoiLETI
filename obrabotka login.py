import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from login import Ui_login #первое окно откуда открывать
from Ui_Anketa import Ui_Anketa #что открывается
from teacher_menu import Ui_MenuChoice #что открывается
from obrabotka_menu import TeacherMenu #что открывается


#создадим для кнопки анкета отклик (2класса)
class Application(QMainWindow, Ui_login):
    def __init__(self):
        super().__init__()

        self.sotrudMenuWindow = TeacherMenu()
        self.abiturAnketaWindow = Ui_Anketa(None)
        self.setupUi(self)
        #self.setWindowTitle('Добро пожаловать!')
        self.abiturButton.clicked.connect(self.showAbiturAnketaWindow)
        self.sotrudnik.clicked.connect(self.showTeacherMenuWindow)

    def showAbiturAnketaWindow(self):
        self.abiturAnketaWindow.show()

    def showTeacherMenuWindow(self):
        self.sotrudMenuWindow.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec())