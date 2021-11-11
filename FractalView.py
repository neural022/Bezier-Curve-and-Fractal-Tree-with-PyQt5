
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap

class FractalView(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        canvas = QPixmap(600, 600)
        canvas.fill(QColor("white"))
        self.setPixmap(canvas)
