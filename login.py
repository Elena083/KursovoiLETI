
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.abiturButton = QtWidgets.QPushButton(self.centralwidget)
        self.abiturButton.setGeometry(QtCore.QRect(0, 100, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.abiturButton.setFont(font)
        self.abiturButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.abiturButton.setObjectName("abitur")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setStyleSheet("background-color: rgb(196, 207, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.sotrudnik = QtWidgets.QPushButton(self.centralwidget)
        self.sotrudnik.setGeometry(QtCore.QRect(200, 100, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.sotrudnik.setFont(font)
        self.sotrudnik.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.sotrudnik.setObjectName("sotrudnik")
        self.label_select_role = QtWidgets.QLabel(self.centralwidget)
        self.label_select_role.setGeometry(QtCore.QRect(0, 50, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_select_role.setFont(font)
        self.label_select_role.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label_select_role.setStyleSheet("background-color: rgb(196, 207, 255);")
        self.label_select_role.setAlignment(QtCore.Qt.AlignCenter)
        self.label_select_role.setObjectName("label_select_role")
        #self.Button_ok = QtWidgets.QPushButton(self.centralwidget)
        #self.Button_ok.setGeometry(QtCore.QRect(0, 150, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        #self.Button_ok.setFont(font)
        #self.Button_ok.setObjectName("Button_ok")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# добавим функцию (метод) за счет недо будет добавлчть обработчики событий ко всем кнопкам впроекте
        self.add_functions()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система Абитуриент"))
        self.abiturButton.setText(_translate("MainWindow", "Абитуриент"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать!"))
        self.sotrudnik.setText(_translate("MainWindow", "Сотрудник"))
        self.label_select_role.setText(_translate("MainWindow", "Выберите роль"))
        #self.Button_ok.setText(_translate("MainWindow", "OK"))

#чтоб писалось в проге при нажатии на кнопки метод обработки
    def add_functions(self):
        self.abiturButton.clicked.connect(lambda:  self.write_role(self.abiturButton.text()))
        self.sotrudnik.clicked.connect(lambda: self.write_role(self.sotrudnik.text()))

#чтоб писалось в проге при нажатии на кнопки метод обработки
    def write_role(self, role):
        self.label_select_role.setText(role)
        print(role)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

