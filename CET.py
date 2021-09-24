from Qwindow import CET_mainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QFileDialog,QDialog,QLabel,QPushButton
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import PyQt5
import cv2
from PIL import Image

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
        self.ui.pushButton_10.clicked.connect(self.load)
        self.ui.pushButton_11.clicked.connect(self.help)
        self.ui.pushButton_12.clicked.connect(self.showDialog)

        self.ui.t = 0
        self.isload = False
        self.ui.buttonrgb = [(255,255,255)]*9
        #self.ui.buttonrgb1 = [(1,1,1)]*9
        #self.ui.buttonrgb1 = [('#FFFFFF')]*9
        self.ui.setcounts = 0

        timer = PyQt5.QtCore.QTimer(self)
        timer.timeout.connect(self.Get_color)
        timer.start(20)


    def showDialog(self):
        col = PyQt5.QtWidgets.QColorDialog.getColor()
        if col.isValid():
            self.ui.setcounts = self.ui.setcounts % 9 + 1
            rgb16=col.name()[1:]
            r,g,b=eval('0x'+rgb16[:2]),eval('0x'+rgb16[2:4]),eval('0x'+rgb16[4:6])
            self.ui.rgb = (r,g,b)
            self.ui.toolLabel.setStyleSheet("background-color:rgb" + str(self.ui.rgb))
            self.ui.rgb1 = (round(r / 255, 2), round(g / 255, 2), round(b / 255, 2))
            self.ui.rgb2 = '#' + (str(hex(r))[2:].zfill(2).upper() + str(hex(g))[2:].zfill(2).upper() + str(hex(b))[2:].zfill(2).upper())
            exec('self.ui.pushButton_' + str(self.ui.setcounts) + '.setStyleSheet(' + '\"background-color: rgb' + str(self.ui.rgb) + '\")')
            self.ui.lineEdit.setText(str(list(self.ui.rgb)[0]) + ',' + str(list(self.ui.rgb)[1]) + ',' + str(list(self.ui.rgb)[2]))
            self.ui.lineEdit_2.setText(str(list(self.ui.rgb1)[0]) + ',' + str(list(self.ui.rgb1)[1]) + ',' + str(list(self.ui.rgb1)[2]))
            self.ui.lineEdit_3.setText(self.ui.rgb2)
            #QMessageBox.question(self, "使用帮助", col.name())
            #self.ui.lineEdit_3.setText(col.name())
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

        if self.isload:
            self.ui.lineEdit.setText(str(list(self.ui.rgb)[0]) + ',' + str(list(self.ui.rgb)[1]) + ',' + str(list(self.ui.rgb)[2]))
            self.ui.lineEdit_2.setText(str(list(self.ui.rgb1)[0]) + ',' + str(list(self.ui.rgb1)[1]) + ',' + str(list(self.ui.rgb1)[2]))
            self.ui.lineEdit_3.setText(self.ui.rgb2)

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
            #self.ui.buttonrgb[self.ui.setcounts%9 -1] = self.ui.rgb
            #self.ui.buttonrgb1[self.ui.setcounts%9 -1] = self.ui.rgb1

    def help(self):
        font3 = PyQt5.QtGui.QFont()
        font3.setFamily("Times New Roman")
        font3.setPointSize(12)
        mb=QMessageBox()
        mb.setFont(font3)
        mb.setWindowTitle('Help')
        mb.setText("This colorimeter is a tool that can take the color of desktop content in real time and display the corresponding color code. \n\nThe specific usage methods are as follows:\n\n"
                                         "(1) Ordinary taking color:\n Move the mouse to the position you need and press 【Enter】 to take color. \n\n"
                                         "(2) Historical record:\n Press the corresponding color in the【Nine grids】 to display the color code. \n\n"
                                         "(3) Query the color palette:\n Press the 【Pick】 button to call up the color palette and select the color and its corresponding color code. \n\n"
                                         "(4) Pick local picture color:\n Press 【Load】 to select a local picture, open the picture, and click the left mouse button to pick the color.")
        mb.setIcon(QMessageBox.Information)
        mb.setStandardButtons(QMessageBox.Yes)
        #mb.setStyleSheet("QPushButton:hover{background-color: rgb(255, 93, 52);}")
        '''
        mb=QMessageBox.question(self,"使用帮助","本取色计是一款能够实时对桌面内容进行取色，并显示对应颜色代码的工具，具体使用方法如下：\n\n"
                                         "①普通取色：将鼠标移至需要取色的位置，按下回车即可取色\n\n"
                                         "②历史记录：按下九宫格中的对应颜色，即可显示颜色代码\n\n"
                                         "③查询调色板：按下Pick按键，即可调出调色板，并在其中选取颜色及其对应颜色代码\n\n"
                                         "④本地图片取色：按下Load按键，选择本地图片，打开图片后单击鼠标左键进行取色",QMessageBox.Yes,QMessageBox.Yes)
        '''
        mb.exec_()

    def load(self):

        def loadcolor():
            self.ui.setcounts = self.ui.setcounts % 9 + 1
            x = QCursor.pos().x()
            y = QCursor.pos().y()
            pixmap = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(), x, y, 1, 1)
            image = pixmap.toImage()
            color = QColor(image.pixel(0, 0))
            r, g, b = color.red(), color.green(), color.blue()
            self.ui.rgb = (r, g, b)
            self.ui.toolLabel.setStyleSheet("background-color:rgb" + str(self.ui.rgb))
            self.ui.rgb1 = (round(r / 255, 2), round(g / 255, 2), round(b / 255, 2))
            self.ui.rgb2 = '#' + (str(hex(r))[2:].zfill(2).upper() + str(hex(g))[2:].zfill(2).upper() + str(hex(b))[2:].zfill(2).upper())
            exec('self.ui.pushButton_' + str(self.ui.setcounts) + '.setStyleSheet(' + '\"background-color: rgb' + str(self.ui.rgb) + '\")')
            self.ui.lineEdit.setText(str(list(self.ui.rgb)[0]) + ',' + str(list(self.ui.rgb)[1]) + ',' + str(list(self.ui.rgb)[2]))
            self.ui.lineEdit_2.setText(str(list(self.ui.rgb1)[0]) + ',' + str(list(self.ui.rgb1)[1]) + ',' + str(list(self.ui.rgb1)[2]))
            self.ui.lineEdit_3.setText(self.ui.rgb2)
            #print('1')


        self.isload=True
        imgName, imgType = QFileDialog.getOpenFileName(self, "Open Picture", "", "*.jpg;;*.png;;*.bmp;;*.jpeg")
        if imgName!='' and imgType!='':
            dialog_fault = QDialog()
            pic = QPixmap(imgName)
            img = Image.open(imgName)
            size = img.size
            #x_pic=size[0]
            #y_pic=size[1]
            #while x_pic>=2000:
            #    x_pic=round(x_pic/2)
            #while y_pic>=2000:
            #    y_pic=round(y_pic/2)
            #print(size)
            #size=(x_pic,y_pic)
            dialog_fault.setWindowTitle('Pick Color')
            PushButton_111=QPushButton(dialog_fault)
            PushButton_111.clicked.connect(loadcolor)
            PushButton_111.setStyleSheet("QPushButton{\n"
                                 "background-image: url(\"%s\");\n"
                                 "background-position:center;\n"
                                 "background-repeat:no-repeat;\n"
                                 "}" % imgName)
            #print(type(size))
            #print(size)
            PushButton_111.setGeometry(10, 10, size[0], size[1])
            dialog_fault.exec_()
        self.isload=False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    CETwindow = mainWindow()
    CETwindow.show()
    sys.exit(app.exec_())