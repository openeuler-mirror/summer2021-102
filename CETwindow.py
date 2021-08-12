from PyQt5 import QtCore, QtGui, QtWidgets

class CET_mainWindow(object):
    def setupUi(self, mainWindow):

        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(493, 174)
        mainWindow.setFixedSize(493,174)

        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NP-B")
        font.setPointSize(7)
        font1 = QtGui.QFont()
        font1.setFamily("UD Digi Kyokasho NP-B")
        font1.setPointSize(8)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./need/colours.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.centralwidget.setObjectName("centralwidget")


        self.showWidget=QtWidgets.QWidget(mainWindow)
        self.showWidget.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.showWidget.setObjectName("showWidget")

        self.toolLabel = QtWidgets.QLabel(self.showWidget)
        self.toolLabel.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Sunken)
        self.toolLabel.setMinimumSize(87, 87)

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(120, 20, 170, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label.setFont(font)

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_2.setFont(font)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_3.setFont(font)


        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        #self.lineEdit.setGeometry(QtCore.QRect(30, 0, 100, 30))

        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        #self.lineEdit_2.setGeometry(QtCore.QRect(30, 40, 100, 30))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        #self.lineEdit_3.setGeometry(QtCore.QRect(30, 80, 100, 30))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(310, 20, 28, 28))
        self.pushButton_1.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(338, 20, 28, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(366, 20, 28, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")


        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 48, 28, 28))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(338, 48, 28, 28))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(366, 48, 28, 28))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 76, 28, 28))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(338, 76, 28, 28))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(366, 76, 28, 28))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")


        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./need/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setGeometry(QtCore.QRect(408, 20, 68, 25))
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_10.setText("Load")
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./need/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setGeometry(QtCore.QRect(408, 50, 68, 25))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_11.setText("Help")
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./need/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setGeometry(QtCore.QRect(408, 80, 68, 25))
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushButton_12.setText("Pick ")
        self.pushButton_12.setObjectName("pushButton_12")

        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, QtCore.Qt.darkGreen)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFont(font1)
        self.label_4.setGeometry(QtCore.QRect(10, 115, 450, 51))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.label_4.setWindowIcon(icon)
        self.label_4.setPalette(pe)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Color extraction tool Beta1.0"))
        self.label_2.setText(_translate("mainWindow", "RGB(1)"))
        self.label_3.setText(_translate("mainWindow", "#16"))
        self.label.setText(_translate("mainWindow", "RGB(255)"))
        self.label_4.setText(_translate("mainWindow", "    Press ''Enter'' to extract the colors.       [Designed by Wednesday] "))