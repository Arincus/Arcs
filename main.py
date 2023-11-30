import sys
import random
import io

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QListWidget

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>873</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>510</y>
      <width>131</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
      <italic>false</italic>
      <strikeout>false</strikeout>
     </font>
    </property>
    <property name="text">
     <string>рисовать</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>873</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        # uic.loadUi('UI.ui', self)

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
        v = random.randint(1, 600)
        s = random.randint(0, 500)
        qp.setPen(QColor(255, 255, 0))
        qp.drawArc(a, v, s, s, 0, 90 * 90)

        a = random.randint(0, 600)
        v = random.randint(1, 600)
        s = random.randint(0, 500)
        qp.setPen(QColor(255, 255, 0))
        qp.drawArc(a, v, s, s, 0, 90 * 90)

        a = random.randint(0, 600)
        v = random.randint(1, 600)
        s = random.randint(0, 500)
        qp.setPen(QColor(255, 255, 0))
        qp.drawArc(a, v, s, s, 0, 90 * 90)

        a = random.randint(0, 600)
        v = random.randint(1, 600)
        s = random.randint(0, 500)
        qp.setPen(QColor(255, 255, 0))
        qp.drawArc(a, v, s, s, 0, 90 * 90)

        a = random.randint(0, 600)
        v = random.randint(1, 600)
        s = random.randint(0, 500)
        qp.setPen(QColor(255, 255, 0))
        qp.drawArc(a, v, s, s, 0, 90 * 90)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())