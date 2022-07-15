
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
#from PyQt5.QtWebEngineWidgets import *


class MyWebBrowser():
    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle('Kc Emma Web Broswer')

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_box = QTextEdit()
        self.url_box.setMaximumHeight(30)

        self.go_btn = QPushButton('Go')
        self.go_btn.setMaximumHeight(30)

        self.back_btn = QPushButton('<')
        self.back_btn.setMaximumHeight(30)

        self.forward_btn = QPushButton('>')
        self.forward_btn.setMaximumHeight(30)

        self.horizontal.addWidget(self.url_box)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl('https://google.com'))

        self.window.setLayout(self.layout)
        self.window.show()


app = QApplication([])
window = MyWebBrowser()
app.exec_()
