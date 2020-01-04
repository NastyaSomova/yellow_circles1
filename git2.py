from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
from PyQt5 import uic


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.add.clicked.connect(self.run)

    def run(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        print('ok')
        qp.setBrush(QColor('yellow'))
        x = random.randint(100, 500)
        y = random.randint(100, 400)
        r = random.randint(10, 300)
        print('ok')
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.show()

    app.exec()
