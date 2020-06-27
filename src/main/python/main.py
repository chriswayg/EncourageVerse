import sys
import requests
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Encourage')
        self.setStyleSheet("background-color: #ffffe6;")
        text = QLabel()
        text.setWordWrap(True)
        button = QPushButton('Next verse >')
        button.clicked.connect(lambda: text.setText(_get_quote()))
        layout = QVBoxLayout()
        layout.addWidget(text)
        layout.addWidget(button)
        layout.setAlignment(button, Qt.AlignHCenter)
        self.setLayout(layout)
        text.setText(_get_quote())


# http://www.ourmanna.com/verses/api/
def _get_quote():
    return requests.get('https://beta.ourmanna.com/api/v1/get/?format=text&order=random').text


if __name__ == '__main__':
    appctxt = ApplicationContext()
    stylesheet = appctxt.get_resource('styles.qss')
    appctxt.app.setStyleSheet(open(stylesheet).read())
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
