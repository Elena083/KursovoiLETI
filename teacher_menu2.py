# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\форма_предметы.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 460)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_saveitems = QtWidgets.QPushButton(self.centralwidget)
        self.Button_saveitems.setGeometry(QtCore.QRect(20, 75, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Button_saveitems.setFont(font)
        self.Button_saveitems.setStyleSheet("background-color: rgb(196, 207, 255);")
        self.Button_saveitems.setObjectName("Button_saveitems")
        self.id_items = QtWidgets.QLabel(self.centralwidget)
        self.id_items.setGeometry(QtCore.QRect(10, 0, 250, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_items.setFont(font)
        self.id_items.setStyleSheet("background-color: rgb(196, 207, 255);")
        self.id_items.setAlignment(QtCore.Qt.AlignCenter)
        self.id_items.setObjectName("id_items")
        self.Name_items = QtWidgets.QLabel(self.centralwidget)
        self.Name_items.setGeometry(QtCore.QRect(270, 0, 250, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Name_items.setFont(font)
        self.Name_items.setStyleSheet("background-color: rgb(196, 207, 255);")
        self.Name_items.setAlignment(QtCore.Qt.AlignCenter)
        self.Name_items.setObjectName("Name_items")
        self.input_id_items = QtWidgets.QLineEdit(self.centralwidget)
        self.input_id_items.setGeometry(QtCore.QRect(10, 35, 250, 30))
        self.input_id_items.setObjectName("input_id_items")
        self.input_items = QtWidgets.QLineEdit(self.centralwidget)
        self.input_items.setGeometry(QtCore.QRect(270, 35, 250, 30))
        self.input_items.setObjectName("input_items")


        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 160, 391, 171))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_saveitems.setText(_translate("MainWindow", "Сохранить"))
        self.id_items.setText(_translate("MainWindow", "ID предмета"))
        self.Name_items.setText(_translate("MainWindow", "Название предмета"))

        self.comboBox.setItemText(0, _translate("MainWindow", "gthdsq"))
        self.comboBox.setItemText(1, _translate("MainWindow", "yjugjkh"))
        self.comboBox.setItemText(2, _translate("MainWindow", "tgyuytu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
