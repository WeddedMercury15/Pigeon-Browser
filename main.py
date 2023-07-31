import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class PigeonBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.navigate_to_url)

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        self.back_btn = QAction("Back", self)
        self.back_btn.triggered.connect(self.browser.back)
        self.toolbar.addAction(self.back_btn)

        self.forward_btn = QAction("Forward", self)
        self.forward_btn.triggered.connect(self.browser.forward)
        self.toolbar.addAction(self.forward_btn)

        self.reload_btn = QAction("Reload", self)
        self.reload_btn.triggered.connect(self.browser.reload)
        self.toolbar.addAction(self.reload_btn)

        self.toolbar.addWidget(self.search_bar)
        self.search_bar.setFixedWidth(400)

        self.browser.urlChanged.connect(self.update_url)

        self.setCentralWidget(self.browser)
        self.setWindowTitle("Pigeon Browser")  # 修改浏览器名称为 "Pigeon Browser"
        self.show()

    def navigate_to_url(self):
        url = QUrl(self.search_bar.text())
        self.browser.setUrl(url)

    def update_url(self, q):
        self.search_bar.setText(q.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = PigeonBrowser()
    sys.exit(app.exec_())
