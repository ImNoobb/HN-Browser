import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        #self.widget = QWidget()
        #self.setCentralWidget(self.widget)

        self.browser = QWebEngineView()
        #self.browser.load(QUrl.fromLocalFile('D:\\jar\\HN-Browser\\main.html'))

        self.setCentralWidget(self.browser)

        self.showMaximized()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: black; color: white")

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('', self)
        back_btn.setFont(QFont('JetBrainsMono NF',8))
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('', self)
        forward_btn.setFont(QFont('JetBrainsMono NF',8))
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('勒', self)
        reload_btn.setFont(QFont('JetBrainsMono NF',8))
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        face_btn = QAction('', self)
        face_btn.setFont(QFont('JetBrainsMono NF',8))
        face_btn.triggered.connect(lambda: self.get_to('https://www.facebook.com/'))
        navbar.addAction(face_btn)

        you_btn = QAction('', self)
        you_btn.setFont(QFont('JetBrainsMono NF',8))
        you_btn.triggered.connect(lambda: self.get_to('https://www.youtube.com/'))
        navbar.addAction(you_btn)

        gg_btn = QAction('', self)
        gg_btn.setFont(QFont('JetBrainsMono NF',8))
        gg_btn.triggered.connect(lambda: self.get_to('https://www.google.com/'))
        navbar.addAction(gg_btn)

        self.show()



    def get_to(self,s):
        self.browser.setUrl(QUrl(s))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))



app = QApplication(sys.argv)
QApplication.setApplicationName('HN Browser')
window = MainWindow()
app.exec_()