from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 390)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.button_show = QtWidgets.QPushButton(self.centralwidget)
        self.button_show.setGeometry(QtCore.QRect(10, 10, 451, 71))
        self.button_show.setObjectName("button_show")
        ##########  Add action to button   #####################

        self.button_show.clicked.connect(lambda: self.action_button_show("gowno"))
            #triggered.connect(lambda: self.action_button_show())


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 130, 431, 181))
        self.label.setText("")
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def action_button_show(self, data):
        print (data)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_show.setText(_translate("MainWindow", "Show"))
        #

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
