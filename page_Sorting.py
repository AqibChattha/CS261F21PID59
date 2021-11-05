import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import page_Scrapping as page2
import pandas as pd

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
        self.setWindowTitle('View Scrapped Data')
        self.resize(1024, 720)

        self.setCentralWidget(SubStackedWidget())
        label_3 = QLabel("", self)
        label_3.setGeometry(QRect(380, 20, 211, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        label_3.setFont(font)
        label_3.setStyleSheet("background-color: rgb(225, 225, 225,225);\n"
        "border-radius:20px")
        label_3.setText("      GameBase")

        label_4 = QLabel("", self)
        label_4.setGeometry(20, 100, 101, 31)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        label_4.setFont(font)
        label_4.setStyleSheet("background-color: rgb(225, 225, 225,225);\n"
        "border-radius:30px")
        label_4.setText("Time taken:")
        label_5 = QLabel("", self)
        label_5.setGeometry(130, 100, 91, 31)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        label_5.setFont(font)
        label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius:30px")
        label_5.setText("98.6 ms")
        comboBox = QComboBox(self)
        comboBox.setGeometry(640, 100, 361, 31)
        font = QFont()
        font.setPointSize(10)
        comboBox.setFont(font)
        comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        comboBox.setObjectName("comboBox")
        comboBox.addItem("Selection sort")
        comboBox.addItem("Merge sort")
        comboBox.addItem("Shell sort")
        comboBox.addItem("Buuble sort")
        comboBox.addItem("Quick sort")
        comboBox.addItem("Heap sort")
        comboBox.addItem("Radix sort")
        comboBox.addItem("Counting sort")
        pushButton = QPushButton(self)
        pushButton.setGeometry(QRect(20, 600, 131, 41))
        font = QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        pushButton.setFont(font)
        pushButton.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "background-color: rgb(225, 225, 225,225);\n"
        "")
        pushButton.setText("Back..")
        pushButton.clicked.connect(self.goMainWindow)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(30, 210, 961, 361)
        self.tableWidget.setMinimumSize(731, 0)
        self.tableWidget.setStyleSheet("background-color: rgb(225, 225, 225,225);\n"
        "border-radius:30px")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.resizeColumnsToContents()
        
        

    def goMainWindow(self):
        self.cams = page2.Window(QMainWindow)
        self.cams.show()
        self.close()    

    def load_File(self, table):
        try:
            all_data = pd.read_csv('GameBase.csv')
            headers = list(all_data)
            table.setRowCount(all_data.shape[0])
            table.setColumnCount(all_data.shape[1])
            table.setHorizontalHeaderLabels(headers)        

            # getting data from df is computationally costly so convert it to array first
            df_array = all_data.values
            for row in range(all_data.shape[0]):
                for col in range(all_data.shape[1]):
                    table.setItem(row, col, QTableWidgetItem(str(df_array[row,col])))
        except:
            print("An Error Occured!")

