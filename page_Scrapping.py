import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import page_Sorting as page3
from selenium import webdriver


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
        pushButton_2.clicked.connect(self.Scrap_onClick)

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
        pushButton_2.clicked.connect(self.Save_onClick)

        self.qTextEdit1 = QTextEdit("", self)
        self.qTextEdit1.setGeometry(20, 310, 961, 231)
        self.qTextEdit1.setStyleSheet("background-color: rgb(225, 225, 225,225);\n"
        "border-radius:30px;\n"
        "padding:15px;")
        self.qTextEdit1.setReadOnly(True)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 220, 781, 23)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setStyleSheet("color:white")
        self.progressBar.setObjectName("progressBar")

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

        self.show()

    def Scrap_onClick(self):
        driver = webdriver.Edge('C:\msedgedriver')
        
        df = pd.read_csv('GamePages.csv')
        list_url = df.GamePage_url.values.tolist()

        Category = []
        Image = []
        Name = []
        Developer = []
        Rating = []
        Price = []
        Game_link = []

        count_in_loop = 0
        count_by_Find = 0
        count1=0
        for a in list_url:
            try:
                driver.get(a)
                driver.execute_script("window.scrollBy(0, 4000)")
                time.sleep(2)
                driver.execute_script("window.scrollBy(0, 4000)")
                time.sleep(2)
                driver.execute_script("window.scrollBy(0, 4000)")
                time.sleep(2)
                driver.execute_script("window.scrollBy(0, 4000)")
                time.sleep(4)
                if count1==3:
                    time.sleep(10)
                else:
                    count1 = count1+1
                content = driver.page_source
                soup = BeautifulSoup(content)
                catagory_n = soup.find('h2', attrs={'class':'sv0AUd bs3Xnd'}).text
                for b in soup.findAll('div',attrs={'class':'Vpfmgd'}):
                    
                    try:
                        Name.append(b.find('div',attrs={'class':'WsMG1c nnK0zc'}).attrs['title'])
                        Developer.append(b.find('div',attrs={'class':'KoLSrc'}).text)
                        Category.append(catagory_n)
                        try:
                            Rating.append(b.find('div',attrs={'role':'img'}).attrs['aria-label'])
                        except:
                            Rating.append("Not Found")
                        try:
                            Price.append(b.find('div',attrs={'class':'zYPPle'}).text)
                        except:
                            Price.append('free')
                        try:
                            Game_link.append(b.find('a',attrs={'aria-hidden':'true'}).attrs['href'])
                        except:
                            Game_link.append("Not Found")
                        try:
                            Image.append(b.find('img',attrs={'class':'T75of QNCnCf'}).attrs['srcset'])
                        except:
                            Image.append("Not Found")
                        count_in_loop = count_in_loop + 1
                    except:
                        print('error')
                                
                count_by_Find = count_by_Find + soup.findAll('div',attrs={'class':'Vpfmgd'}).__len__()
                print(f"Count by find={count_by_Find} ---- Count in loop={count_in_loop}")
                self.progressBar.setProperty('value', (count_by_Find/15991)*100)
            except:
                print("page not loaded")

        return Name, Developer,Category,Rating,Price,Image,Game_link


    def Save_onClick(Name, Developer, Category, Rating, Price, Image, Game_link):
        df = pd.DataFrame({'GameName':Name, 'Developer': Developer,'Category':Category,'Rating':Rating,'Price':Price,'Image_link':Image,'Game_link':Game_link})
        df.to_csv('SaveTest.csv', index=False, encoding='utf-8')


    @pyqtSlot()
    def buttonForm2_onClick(self):
        self.statusBar().showMessage("Switched to window 2")
        self.cams = page3.Window(QMainWindow)
        self.cams.load_File(self.cams.tableWidget)
        self.close()