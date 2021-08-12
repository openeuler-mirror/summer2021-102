from CETwindow import CET_mainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import PyQt5

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = CET_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.slot1)
        self.ui.pushButton_2.clicked.connect(self.slot1)
        self.ui.pushButton_3.clicked.connect(self.slot1)
        self.ui.pushButton_4.clicked.connect(self.slot1)
        self.ui.pushButton_5.clicked.connect(self.slot1)
        self.ui.pushButton_6.clicked.connect(self.slot1)
        self.ui.pushButton_7.clicked.connect(self.slot1)
        self.ui.pushButton_8.clicked.connect(self.slot1)
        self.ui.pushButton_9.clicked.connect(self.slot1)
        self.ui.pushButton_12.clicked.connect(self.showDialog)
        self.ui.t = 0
        self.ui.buttonrgb = [(255,255,255)]*9
        self.ui.buttonrgb1 = [(1,1,1)]*9
        self.ui.buttonrgb1 = [('#FFFFFF')]*9
        self.ui.setcounts = 0

        timer = PyQt5.QtCore.QTimer(self)
        timer.timeout.connect(self.Get_color)
        timer.start(20)

    def showDialog(self):
        col = PyQt5.QtWidgets.QColorDialog.getColor()
        if col.isValid():
            #self.ui.lineEdit_3.setText(col.name())
            '''
            self.ui.setcounts = self.ui.setcounts % 9 + 1
            exec('self.ui.pushButton_' + str(self.ui.setcounts) + '.setStyleSheet(' + '\"background-color: rgb' + str(self.ui.rgb) + '\")')
            self.ui.lineEdit.setText(str(list(self.ui.rgb)[0]) + ',' + str(list(self.ui.rgb)[1]) + ',' + str(list(self.ui.rgb)[2]))
            self.ui.lineEdit_2.setText(str(list(self.ui.rgb1)[0]) + ',' + str(list(self.ui.rgb1)[1]) + ',' + str(list(self.ui.rgb1)[2]))
            self.ui.lineEdit_3.setText(('#' + str(self.ui.rgb2).strip('0x')).upper())
            self.ui.buttonrgb[self.ui.setcounts % 9 - 1] = self.ui.rgb
            self.ui.buttonrgb1[self.ui.setcounts % 9 - 1] = self.ui.rgb1
            '''
            #exec('self.ui.pushButton_' + str(self.ui.setcounts) + '.setStyleSheet(' + '\"background-color: rgb' + str(self.ui.rgb) + '\")')
            #self.widget.setStyleSheet('QWidget {background-color:%s}' % col.name())
            pass

    def Get_color(self):

        x = QCursor.pos().x()
        y = QCursor.pos().y()
        pixmap = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, 1, 1)
        image = pixmap.toImage()
        color = QColor(image.pixel(0, 0))
        r, g, b = color.red(), color.green(), color.blue()
        self.ui.rgb = (r, g, b)
        self.ui.toolLabel.setStyleSheet("background-color:rgb"+str(self.ui.rgb))
        self.ui.rgb1 = (round(r/255,2) ,round(g/255,2),round(b/255,2))
        self.ui.rgb2 = '#'+(str(hex(r))[2:].zfill(2).upper()+str(hex(g))[2:].zfill(2).upper()+str(hex(b))[2:].zfill(2).upper())


    def set_colors(self):
        exec('self.ui.pushButton_' + str(self.ui.setcounts) + '.setStyleSheet('+'\"background-color: rgb'+str(self.ui.rgb)+'\")')
        self.ui.lineEdit.setText(str(list(self.ui.rgb)[0])+','+str(list(self.ui.rgb)[1])+','+str(list(self.ui.rgb)[2]))
        self.ui.lineEdit_2.setText(str(list(self.ui.rgb1)[0])+','+str(list(self.ui.rgb1)[1])+','+str(list(self.ui.rgb1)[2]))
        self.ui.lineEdit_3.setText(self.ui.rgb2)

    def slot1(self):
        def round2(x):
            return round(x,2)
        RGB = self.sender().palette().button().color().getRgb()
        RGB1 = self.sender().palette().button().color().getRgbF()
        RGB = RGB[0:3]
        RGB1 = RGB1[0:3]
        RGB1 = tuple(map(round2,RGB1))
        self.ui.lineEdit.setText(str(list(RGB)[0])+','+str(list(RGB)[1])+','+str(list(RGB)[2]))
        self.ui.lineEdit_2.setText(str(list(RGB1)[0])+','+str(list(RGB1)[1])+','+str(list(RGB1)[2]))
        self.ui.lineEdit_3.setText('#'+(str(hex(RGB[0]))[2:].zfill(2).upper()+str(hex(RGB[1]))[2:].zfill(2).upper()+str(hex(RGB[2]))[2:].zfill(2).upper()))
        self.ui.toolLabel.setStyleSheet("background-color: rgb"+str(RGB))



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter-1:
            self.ui.setcounts = self.ui.setcounts%9 +1
            self.set_colors()
            self.ui.buttonrgb[self.ui.setcounts%9 -1] = self.ui.rgb
            self.ui.buttonrgb1[self.ui.setcounts%9 -1] = self.ui.rgb1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    CETwindow = mainWindow()
    CETwindow.show()
    sys.exit(app.exec_())