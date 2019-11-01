# Filename: f_layout.py

"""Form layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('W QFormLayout')

l = QFormLayout()

l.addRow('Push for:', QPushButton('Extreme Far-Left'))
l.addRow('Push for:', QPushButton('Far-Left'))
l.addRow('Push for:', QPushButton('Left-wing'))
l.addRow('Push for:', QPushButton('Center-Left'))
l.addRow('Push for:', QPushButton('Center'))
l.addRow('Do not push for:', QPushButton('Center-Right'))
l.addRow('Do not push for:', QPushButton('Right-wing'))
l.addRow('Do not push for:', QPushButton('Far-Right'))
l.addRow('Do not push for:', QPushButton('Extreme Far-Right'))

w.setLayout(l)
w.show()

sys.exit(app.exec_())