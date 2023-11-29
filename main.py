import sys
import random
from PIL import Image, ImageDraw
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QListWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        # self.pushButton = QPushButton()
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        a = random.randint(0, 600)
        b = random.randint(0, 500)
        qp.setPen(QColor(255, 250, 0))
        qp.drawArc(a, a, b, b, 0, 90*90)

        a = random.randint(0, 600)
        b = random.randint(0, 500)
        qp.setPen(QColor(255, 250, 0))
        qp.drawArc(a, a, b, b, 0, 90 * 90)

        a = random.randint(0, 600)
        b = random.randint(0, 500)
        qp.setPen(QColor(255, 250, 0))
        qp.drawArc(a, a, b, b, 0, 90 * 90)

        a = random.randint(0, 600)
        b = random.randint(0, 500)
        qp.setPen(QColor(255, 250, 0))
        qp.drawArc(a, a, b, b, 0, 90 * 90)

        a = random.randint(0, 600)
        b = random.randint(0, 500)
        qp.setPen(QColor(255, 250, 0))
        qp.drawArc(a, a, b, b, 0, 90 * 90)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
