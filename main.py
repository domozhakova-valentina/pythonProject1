import sys


from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.w = self.size().width()
        self.h = self.size().height()
        self.color = QColor(255, 255, 0)
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_figure(qp)
            qp.end()
            self.do_paint = False

    def draw_figure(self, qp):
        side = randint(20, 200)
        x = randint(0, self.w)
        y = randint(0, self.h)
        qp.setBrush(self.color)
        qp.drawEllipse(x, y, side, side)

    def run(self):
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
