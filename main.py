import sys


from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.w = self.size().width()
        self.h = self.size().height()
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
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        x = randint(0, self.w)
        y = randint(0, self.h)
        qp.setBrush(color)
        qp.drawEllipse(x, y, side, side)

    def run(self):
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
