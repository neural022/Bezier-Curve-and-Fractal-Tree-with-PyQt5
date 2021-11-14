
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QSlider
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap

# binary tree
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

        self.size = 0
        self.top = 0


class FractalView(QtWidgets.QLabel):
    def __init__(self, slider, parent=None):
        super().__init__(parent)
        self.slider = slider

        canvas = QPixmap(600, 600)
        canvas.fill(QColor("white"))
        self.setPixmap(canvas)
        

    
    def branch_size(self, parent):
        return parent.height*3/4, parent.width / 2
    
    def add_branch(self):
        pass

    def add_flower(self):
        pass

    def flower_size(self):
        pass

    def paintEvent(self, event):
        pass

    