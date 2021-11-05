import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import page_Sorting as page3

class SubStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent=parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("res3.jpg"))
        QStackedWidget.paintEvent(self, event)

class Window(QMainWindow):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Web Scrapping')
        self.resize(1024, 720)

        self.setCentralWidget(SubStackedWidget())
        
        label1 = QLabel("", self)
        label1.setGeometry(400, 70, 231, 71)
        label1.setStyleSheet("background-color: rgb(225, 225, 225,225);\n"
        "border-radius:30px;")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        label1.setFont(font)
        label1.setText("      GameBase")

        label4 = QLabel("", self)
        label4.setGeometry(30, 170, 781, 31)
        font = QFont()
        font.setPointSize(8)
        font.setWeight(50)
        label4.setFont(font)
        label4.setStyleSheet("background-color: rgb(225, 225, 225,225);\n"
        "border-radius:30px;\n"
        "padding:10px")
        label4.setText("https://play.google.com/store/apps/collection/cluster?clp=ogoQCA0SBEdBTUUqAggCUgIIAQ%3D%3D:S:ANO1ljLkXME&gsr=ChOiChAIDRIER0FNRSoCCAJSAggB:S:ANO1ljJOCxY")

        pushButton_2 = QPushButton("", self)
        pushButton_2.setGeometry(840, 170, 131, 31)
        font = QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        pushButton_2.setFont(font)
        pushButton_2.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "background-color: rgb(225, 225, 225,225);")
        pushButton_2.setText("Start")

        pushButton_3 = QPushButton("", self)
        pushButton_3.setGeometry(30, 260, 121, 31)
        font = QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        pushButton_3.setFont(font)
        pushButton_3.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "background-color: rgb(225, 225, 225,225);\n"
        "")
        pushButton_3.setText("Pause")

        pushButton_4 = QPushButton("", self)
        pushButton_4.setGeometry(171, 260, 121, 31)
        font = QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        pushButton_4.setFont(font)
        pushButton_4.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "background-color: rgb(225, 225, 225,225);\n"
        "")
        pushButton_4.setText("Save")

        self.label_2 = QLabel("", self)
        self.label_2.setGeometry(20, 310, 961, 231)
        self.label_2.setStyleSheet("background-color: rgb(225, 225, 225,225);\n"
        "border-radius:30px")
        self.label_2.setText("")

        progressBar = QProgressBar(self)
        progressBar.setGeometry(30, 220, 781, 23)
        progressBar.setProperty("value", 24)
        progressBar.setStyleSheet("color:white")
        progressBar.setObjectName("progressBar")

        btnSort = QPushButton("", self)
        btnSort.setGeometry(830, 600, 131, 41)
        font = QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        btnSort.setFont(font)
        btnSort.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "background-color: rgb(225, 225, 225,225);")
        btnSort.setText("Sort...")
        btnSort.clicked.connect(self.buttonForm2_onClick)

    @pyqtSlot()
    def buttonForm2_onClick(self):
        self.statusBar().showMessage("Switched to window 2")
        self.cams = page3.Window(QMainWindow)
        self.cams.show()
        self.cams.load_File(self.cams.tableWidget)
        self.close()