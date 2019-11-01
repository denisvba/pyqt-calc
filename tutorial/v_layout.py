# Filename: h_layout.py

"""Horizontal layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('W QVBoxLayout')

l = QVBoxLayout()

l.addWidget(QPushButton('Extreme Far-Left'))
l.addWidget(QPushButton('Far-Left'))
l.addWidget(QPushButton('Left-wing'))
l.addWidget(QPushButton('Center-Left'))
l.addWidget(QPushButton('Center'))
l.addWidget(QPushButton('Center-Right'))
l.addWidget(QPushButton('Right-wing'))
l.addWidget(QPushButton('Far-Right'))
l.addWidget(QPushButton('Extreme Far-Right'))

w.setLayout(l)
w.show()

sys.exit(app.exec_())