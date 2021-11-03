
import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import pandas as pd

class MainStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent=parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("res.jpg"))
        QStackedWidget.paintEvent(self, event)
        
class SubStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent=parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap("res3.jpg"))
        QStackedWidget.paintEvent(self, event)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GameBase")
        self.resize(1024, 720)
        self.setCentralWidget(MainStackedWidget())
        
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
        
        qTextEdit1 = QTextEdit("", self)
        qTextEdit1.setGeometry(110, 210, 811, 341)
        qTextEdit1.setStyleSheet("background-color: rgb(225, 225, 225,225);\n"
        "border-radius:30px;\n"
        "padding:15px;")
        qTextEdit1.setReadOnly(True)
        qTextEdit1.setText("""PLEASE READ THIS DOCUMENT CAREFULLY BEFORE INSTALLING THIS SOFTWARE. BY DOWNLOADING, INSTALLING, AND USING THIS SOFTWARE, YOU AGREE TO BE BOUND BY THE TERMS OF THIS AGREEMENT. IF YOU DO NOT AGREE TO THE TERMS OF THIS AGREEMENT, DO NOT INSTALL OR USE THE SOFTWARE. YOU AGREE THAT YOUR INSTALLING OR USE OF THE SOFTWARE ACKNOWLEDGES THAT YOU HAVE READ THIS LICENSE, UNDERSTAND IT, AND AGREE TO BE BOUND BY ITS TERMS AND CONDITIONS.

 

        YOU AGREE THAT THE AGREEMENT IS ENFORCEABLE LIKE ANY WRITTEN NEGOTIATED AGREEMENT SIGNED BY YOU AND THIS AGREEMENT IS ENFORCEABLE AGAINST YOU.

        

        This is a legal agreement between you (either an individual or a legal entity, "Users") and Octopus Data Inc. and its authorized distributors and resellers. This End User License Agreement (the "Agreement") outlines the rules and regulations for the use of Octopus Data Inc.'s website and the software ("Octoparse") and services made available here (collectively, the "Service").

        

        Grant of License 

        Subject to the terms and conditions of these Terms, Octopus Data hereby grants to you a limited, personal, non-transferable license to use the Service in the manner contemplated by these Terms solely for your internal business purposes. Octoparse is licensed, not sold, to you for use only under the terms of this Agreement. Octopus Data Inc. retains all title to and ownership of the Service and reserves all rights not expressly granted to you. Users shall have no right to sub-license or resell the Service or any component thereof.
        If you have downloaded Octoparse and have a free account, Octopus Data Inc. grants you a non-exclusive, non-transferable license to use Octoparsefree of charge for the purpose of getting data from websites and evaluating whether you wish to purchase an ongoing license for the Service. 
        By using the Service, you hereby grant, and represent and warrant that you have all rights necessary to giant Octopus Data the right to include you as a customer or user of Octopus Data Inc.
        

        Privacy Policy

        The Octoparse Privacy Policy found online at www.octoparse.com/privacy-policy, is incorporated herein by reference.

        

        Billing & Payment Terms

        The Octoparse Payment Terms found online at www.octoparse.com/billing-payments, is incorporated herein by reference.

        

        User Account and User Data  

        You will have to register for the Service and create an account ("User Account") to use certain aspects of the Service. When creating your account for the Service, you agree to provide and update your personal information as needed to keep it true, accurate, current, and complete. If you have reason to believe that your account is no longer secure (for example, in the event of a loss, theft, or unauthorized disclosure or use of your ID, password, or any credit, debit, or charge card number), you agree to immediately notify Octopus Data Inc.

        (b) Octopus Data Inc. shall have no right to sub-license or resell User Data, except, however, that you agree that Octopus Data Inc. may use data derived from User Data, for purposes of operating, analyzing, improving, or marketing the Service and any related services. If Octopus Data Inc. shares or publicly disclose information that is derived from User Data, such data will be aggregated or anonymized to reasonably avoid identification of a specific individual or the User.

        (c) You need to represent, warrant, and agree that: (i) you have obtained the User Data lawfully and the User Data does not and will not violate any applicable laws or any person or entity’s rights; (ii) Octopus Data Inc. takes no responsibility and assumes no liability for any User Data, and you will be solely responsible for your User Data and the consequences of sharing or disclosing it hereunder, including Octopus Data Inc.’s use of such User Data as contemplated herein.

        (d) You are solely responsible for backing up your User Data on a regular basis, and taking appropriate steps to safeguard and ensure the integrity of your User Data.

        (e) You may choose to allow Octoparse to automatically retrieve data from your system(s) or third-party system(s)/services/sites on your behalf, you hereby represent and warrant that you have the permission, authority, and rights to use Service to access and/or to allow Octoparse to automatically access such system(s)/services/sites and retrieve User Data therefrom by indicating the same within your User Account. You agree that your use of the Service will not violate any terms of service, agreement, privacy policy, or any implied statements from any third party.

        (f) You own all right, title and interest (including all intellectual property rights) in and to your User Data.

        

        Copyright

        Octoparse is owned by Octopus Data Inc. and is protected by the prevailing law of the United States and international copyright laws. You may not remove the copyright notice from any copy of the Service or any copy of the written materials, if any, accompanying the Service.

        

        Restrictions

        You agree to the following additional terms and restrictions related to the License:

        a. You may not:

        (i) to transmit Octoparse or display Octoparse ‘s object code on any computer screen or to make any hard copy memory dumps of the Octoparse ‘s object code, for any purpose;

        (ii) modify, adapt or translate the Service;

        (iii) modify the Service in any manner or form, or use modified versions of the Service, including but not limited to for the purpose of obtaining unauthorized access to the Service;

        (iv) use the Service for any purpose that is unlawful or is otherwise prohibited by these Terms;

        (v) rent, lease, loan, resell, sub-license, distribute or otherwise transfer the Service to any third party; or use the Service for any purpose other than your own internal business use; or

        (vi) remove any proprietary notices, labels or marks on the Service.

        b. You acknowledge that Octoparse contains trade secrets and other proprietary information of Octopus Data Inc. You may not decompile, disassemble or otherwise reverse engineer Octoparse, or engage in any other activities to obtain underlying information that is not visible to the user in connection with the normal use of Octoparse.

        

        Termination of License

        (a) Termination by You. You may terminate the license at any time by stopping using and accessing the Service in your possession or control.

        (b) Termination by Octopus Data Inc.. You agree that Octopus Data Inc., in its sole discretion, may terminate your account, delete any content or information that you have posted on the Service, and/or prohibit you from using or accessing the Service (or any portion, aspect, or feature of the Service) for any reason or no reason, at any time in its sole discretion, with or without notice, if you fail to comply with any term or condition of this Agreement. In addition, Octopus Data Inc. reserves the rights to discontinue any aspect of the Service at any time.

        (c) You agree upon any such termination, either by you or Octopus Data Inc., to stop using the Service. Any further use of the Service will be deemed an infringement of Octopus Data Inc.’s intellectual property as well as a violation of this Agreement.

        (d) The provisions of this Agreement that protect the proprietary rights of Octopus Data Inc. will continue in force after termination.

        

        Proprietary Rights

        The Service is owned and operated by Octopus Data Inc. The visual interfaces, graphics, design, compilation, information, computer code, products, software(“Octoparse”), services, and all other elements of the Service provided by Octopus Data Inc., but expressly excluding any of the foregoing owned or licensed by and posted to the Service at the direction of Users are protected by intellectual property and other applicable laws.

        

        No Warranty

        (a) ANY USE BY YOU OF OCTOPARSE IS AT YOUR OWN RISK. OCTOPARSE IS PROVIDED FOR USE “AS IS” WITHOUT WARRANTY OF ANY KIND. TO THE MAXIMUM EXTENT PERMITTED BY LAW OCTOPUS DATA INC. DISCLAIMS ALL WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, WITHOUT LIMITATION, IMPLIED WARRANTIES OR CONDITIONS OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.

        (b) Octopus Data Inc. does not warrant that the functions contained in the Service will meet your requirements or that the operation of the Service will be uninterrupted or error-free or that defects will be corrected within a certain time period, if at all. Any representation, other than the warranties set forth in this Agreement, will not bind Octopus Data Inc. You assume full responsibility for the selection of the Service to achieve your intended results, and for the use and results obtained from the Service. You also assume the entire risk as it applies to the quality and performance of the Service

        (c) Octopus Data Inc. shall not be liable for the accuracy of any information provided by Octopus Data Inc. or third-party technical support personnel, or any damages caused, either directly or indirectly, by acts taken or omissions made by you as a result of such technical support.

        (d) No oral or written information or advice is given by Octopus Data Inc., its officers, employees, agents, representatives, authorized distributors, and resellers shall create a warranty.

        

        Disclaimer of Damages: Limitation of Liability

        IN NO EVENT SHALL OCTOPUS DATA INC. OR ITS AUTHORIZED DISTRIBUTORS OR RESELLERS BE LIABLE FOR ANY DAMAGES WHATSOEVER (INCLUDING WITHOUT LIMITATION, INCIDENTAL, INDIRECT, SPECIAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES, OR FOR ANY LOST PROFITS, LOST SAVINGS, LOST REVENUES, LOST DATA OR BUSINESS INTERRUPTION) ARISING OUT OF OR RELATED TO THE USE OF OR INABILITY TO USE THE SOFTWARE, OR ARISING FROM OR RELATING TO THIS AGREEMENT, EVEN IF OCTOPUS DATA INC. OR ITS AUTHORIZED DISTRIBUTORS OR RESELLERS HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. IN NO EVENT OCTOPUS DATA INC.’S LIABILITY OR DAMAGES TO YOU OR ANY THIRD PARTY EVER EXCEED THE AMOUNT PAID BY YOU TO USE THE SOFTWARE, REGARDLESS OF THE FORM OF THE CLAIM.

        

        Indemnification

        You agree to defend, indemnify, and hold harmless Octopus Data Inc. and its agents, managers, and other affiliated companies, and their employees, contractors, agents, officers and directors, from and against any and all claims, damages, obligations, losses, liabilities, costs or debt, and expenses (including but not limited to attorney’s fees) arising from: (a) your use of and access to the Service, including any data or work transmitted or received by you; (b) your violation of any term of these Terms, including without limitation, your breach of any of the representations and warranties above; (c) your violation of or User Data violating any third-party right, including without limitation any right of privacy, publicity rights or intellectual property rights; (d) your violation of any law, rule or regulation of the United States or any other country; (e) any claim or damages that arise as a result of any of your User Data or any other data that are submitted via your account; or (f) any other party’s access and use of the Service with your unique username, password or other appropriate security code. Octopus Data Inc. will have the right to control the defense, settlement, adjustment or compromise of any such claims, actions or proceedings by using counsel selected by Octopus Data Inc. Octopus Data Inc. will use reasonable efforts to notify you of any such claims, actions, or proceedings upon becoming aware of the same.

        

        General

        (a) This Agreement is the entire agreement between us and supersedes any other understandings or agreements (written), including, but not limited to, advertising, with respect to the Service.

        (b) If any provision of this Agreement is deemed invalid or unenforceable by a court of competent jurisdiction, that particular provision will be deemed modified to the extent necessary to make the provision valid and enforceable and the remaining provisions will remain in full force and effect.

        (c) You agree that Octopus Data Inc. will not have any liability for any untrue statement or representation made by it and its officers, employees, agents and representatives or anyone else (whether innocently or negligently) upon which you relied upon entering this Agreement unless such untrue statement or representation was made fraudulently.

        (d) For questions concerning this Agreement, please contact Octopus Data Inc. via support@octoparse.com.""")
        
        checkbox1 = QCheckBox("I agree to terms and conditions", self)
        checkbox1.setStyleSheet("background-color: rgb(225, 225, 225,225);"
        "padding-left: 10px;")
        checkbox1.setGeometry(120, 590, 261, 31)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        checkbox1.setFont(font1)

        buttonForm1 = QPushButton('Lets Begin!', self)
        buttonForm1.setGeometry(780, 580, 131, 41)
        buttonForm1.clicked.connect(self.buttonForm1_onClick)
        buttonForm1.setStyleSheet("background-color: rgb(225, 225, 225,225);")

        self.show()

    @pyqtSlot()
    def buttonForm1_onClick(self):
        self.statusBar().showMessage("Switched to window 1")
        self.cams = Form1(QMainWindow)
        self.cams.show()
        self.close()
        
        
class Form1(QMainWindow):
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
        self.cams = Form2(QMainWindow)
        self.cams.datahead()
        self.cams.show()
        self.close()

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close() 
        
    
class Form2(QMainWindow):
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
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QTableWidgetItem()
        item.setText("Name")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        item.setText("Category")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        item.setText("Developer")
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        item.setText("Rating")
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        item.setText("Price")
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        item.setText("Images")
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        item.setText("Game Page")
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        

    def goMainWindow(self):
        self.cams = Form1(QMainWindow)
        self.cams.show()
        self.close()    

    def load_File(self):
        try:
            all_data = pd.read_csv('GameBase.csv')
            return all_data
        except:
            print("An Error Occured!")

    def datahead(self):
        data = self.load_File() 
        NumRows = 15000
        self.tableWidget.setColumnCount(len(data.columns))
        self.tableWidget.setRowCount(NumRows)
        self.tableWidget.setHorizontalHeaderLabels(data.columns)
        for i in range(NumRows):
                for j in range(len(data.columns)):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(data.iat[i, j])))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Window()
    sys.exit(app.exec_())