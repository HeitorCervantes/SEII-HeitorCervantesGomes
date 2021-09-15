import sys

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout

from PyQt5.QtGui import QPixmap

from PyQt5 import QtGui, QtCore

from PyQt5.QtGui import QCursor

from Parte02 import frame1, frame2, frame3, frame4, grid


app = QApplication(sys.argv)


window = QWidget()
window.setWindowTitle("Who wants to be a programmer???")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

frame1()

window.setLayout(grid)

window.show()
sys.exit(app.exec())