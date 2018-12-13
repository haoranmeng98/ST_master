
import sys
import train
from PyQt5 import QtGui
from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtWidgets import *
from settings import setpath,setpath2,setbeta
from PyQt5.QtGui import QPixmap

class GUI(QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Style Transfer Master')
        self.setGeometry(300, 300, 1000, 600)
        #self.setWindowTitle('')
        #self.label2 = QLabel('Let\'s magic your picture', self)
        #self.move(self,200)
        #self.pbar = QProgressBar(self)
        #self.pbar.setGeometry(130, 20, 300, 25)
        #self.timer = QBasicTimer()
        #self.step = 0
        self.bar = QSlider(Qt.Horizontal, self)
        self.bar.setRange(0, 100)
        #bar.setGeomerty(100,100,100,100)
        self.bar.setGeometry(200*2, 20*2, 100*2, 30*2)
        self.bar.valueChanged.connect(self.barfunc)
        self.bar.setMinimum(10)
        #self.bar.slierReleased.connect(self.barfunc)
        #bar.setSliderPosition(100)
        #self.bar.move(200.200)



        #start button
        self.gobuton = QPushButton('Go!', self)
        self.gobuton.resize(self.gobuton.sizeHint())
        self.gobuton.move(210*2, 250*2)
        self.gobuton.clicked.connect(self.go)
        #self.gobuton.clicked.connect(self.Action)
        self.gobuton.clicked.connect(train.train)

        self.label = QLabel(self)
        #self.label.setText("显示图片")
        self.label.setFixedSize(220*2, 180*2)
        self.label.move(20*2, 50*2)
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )
        pixmap = QPixmap('cloud.png').scaled(self.label.width(), self.label.height())
        #jpg = QtGui.QPixmap(imgName).scaled(self.label2.width(), self.label2.height())
        self.label.setPixmap(pixmap)


        self.label2 = QLabel(self)
        # self.label.setText("显示图片")
        self.label2.setFixedSize(230*2, 180*2)
        self.label2.move(250*2, 50*2)
        self.label2.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )
        pixmap = QPixmap('cloud.png').scaled(self.label2.width(), self.label2.height())
        # jpg = QtGui.QPixmap(imgName).scaled(self.label2.width(), self.label2.height())
        self.label2.setPixmap(pixmap)

        self.openbt =QPushButton('Open',self)
        self.openbt.move(100*2,250*2)
        self.openbt.clicked.connect(self.openim)

        self.openbt2 = QPushButton('Open', self)
        self.openbt2.move(320*2, 250*2)
        self.openbt2.clicked.connect(self.openim2)



       # self.show()
    def say_hi(self):
        QMessageBox.information(self,'Hi','Nice to see you.')
        sys.exit()

    def openim(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "Open", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        #print(imgName)
        setpath(imgName)
        self.label.setPixmap(jpg)

    def go(self):
        QMessageBox.information(self,'Please wait a sec','AI painter is working hard!')

    def openim2(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "Open", "", "*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label2.width(), self.label2.height())
        self.label2.setPixmap(jpg)
        setpath2(imgName)
    def barfunc(self):
        v = self.bar.value()

        v = v*50
        print(v)
        setbeta(v)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yes = GUI()
    yes.show()
    sys.exit(app.exec_())