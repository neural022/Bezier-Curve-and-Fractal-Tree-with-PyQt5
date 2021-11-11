

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtCore import QRect, Qt, QPoint, QSize
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap, QBrush

class BezierView(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.canvas = QPixmap(600, 600)
        self.canvas.fill(QColor("white"))
        self.setPixmap(self.canvas)
        
        self.control_points = list()
        self.point_size = 10
        self.drag_idx = -1
    
    
    def draw_bezier_curve(self):
        pass

    def is_pointSelected(self, point_coord, position):
        # point range
        x_min = point_coord.x()
        x_max = point_coord.x() + self.point_size
        y_min = point_coord.y() 
        y_max = point_coord.y() + self.point_size

        # check control points in select range position
        x, y = position.x(), position.y()
        if x_min < x < x_max and y_min < y < y_max:
            return True
        return False
    
    def drag_index(self, position):
        for i, point in enumerate(self.control_points):
            if self.is_pointSelected(point, position):
                return i
        return -1
    
    def paintEvent(self, event):
        # cover
        super(BezierView, self).paintEvent(event)
        # draw
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black, 1)
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing)
        for point in self.control_points:
            painter.drawRect(QRect(point.x(), point.y(), self.point_size, self.point_size))
        painter.end()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print(event.pos())
            if len(self.control_points) == 4:
                self.drag_idx = self.drag_index(event.pos())
                print('drag_index:', self.drag_idx)
    
    def mouseMoveEvent(self, event):
        if self.drag_idx != -1:
            self.control_points[self.drag_idx] = event.pos()
            parent_rect = self.rect()
            # x axis
            if self.control_points[self.drag_idx].x() < 0:
                self.control_points[self.drag_idx].setX(1)
            elif self.control_points[self.drag_idx].x() > parent_rect.right():
                self.control_points[self.drag_idx].setX(parent_rect.right() - self.point_size)
            # y axis
            if self.control_points[self.drag_idx].y() < 0:
                self.control_points[self.drag_idx].setY(1)
            elif self.control_points[self.drag_idx].y() > parent_rect.bottom():
                self.control_points[self.drag_idx].setY(parent_rect.bottom() - self.point_size)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if len(self.control_points) < 4:
                # add control points
                control_point = event.pos()
                self.control_points.append(control_point)
            else:
                self.drag_idx = -1
            self.update()

    def redraw_click_event(self):
        self.control_points = list()
        self.setPixmap(self.canvas)