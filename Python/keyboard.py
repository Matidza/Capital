import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
import subprocess

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            subprocess.Popen('code --new-terminal', shell=True)

app = QApplication(sys.argv)
widget = MyWidget()
sys.exit(app.exec_())
