# -*- coding: utf-8 -*-
"""
@author: george chen(neural022)
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect, Qt, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap, QBrush, QPolygonF

class BezierCurve():
    def __init__(self):
        self.bezier_points = list()
        self.MAX_LEVEL = 8

    def _calc_mid_point(self, p1, p2):
        return QPointF((p1.x()+p2.x())/2, (p1.y()+p2.y())/2)
    
    def bezier(self, p1, p2, p3, p4, level=1):
        # recursive mid point approximate
        if level < self.MAX_LEVEL:
            '''
            # variables
            # L2: Point(1, 2) is mid point between the Point 1 and Point 2
            # H:  Point(2, 3) is mid point between the Point 2 and Point 3
            # R3: Point(3, 4) is mid point between the Point 3 and Point 4
            '''
            # step 1: calculate first mid points
            L2 = self._calc_mid_point(p1, p2)
            H = self._calc_mid_point(p2, p3)
            R3 = self._calc_mid_point(p3, p4)
            '''
            # variables
            # L3: Point(1, 2, 3) is mid point between the Point(1, 2) and Point(2, 3)
            # R2: Point(2, 3, 4) is mid point between the Point(2, 3) and Point(3, 4)
            # L4(Q Point): Point(123, 234) is mid point between the PoinPoint(1, 2, 3) and Point(2, 3, 4)
            '''
            # step 2 calculate second mid points
            L3 = self._calc_mid_point(L2, H)
            R2 = self._calc_mid_point(R3, H)
            L4 = self._calc_mid_point(L3, R2)
            '''
            # variables
            # p1: Point(1) is initial first point
            # p4: Point(4) is intial last point
            '''
            # step 3 split left and right partition, add mid point to bezier points
            self.bezier(p1, L2, L3, L4, level+1)
            self.bezier_points.append(L4)
            self.bezier(L4, R2, R3, p4, level+1)
    
    def recalc(self, p1, p2, p3, p4, level):
        self.bezier_points = list()
        self.bezier(p1, p2, p3, p4, level)


class BezierView(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.canvas = QPixmap(750, 600)
        self.canvas.fill(QColor("white"))
        self.setPixmap(self.canvas)
        
        # self.control_points = [ QPoint(198, 270), QPoint(198, 190), QPoint(133, 197), QPoint(133, 267) ]
        self.control_points = list()
        self.point_size = 10
        self.drag_idx = -1
        
        # bezier curve
        self.bezier_curve = BezierCurve()
        # calculate bezier curve mid point
        if self.bezier_curve.bezier_points:
            self.bezier_curve.bezier(self.control_points[0], self.control_points[1], self.control_points[2], self.control_points[3], 0)

    def is_pointSelected(self, point_coord, position):
        # point range
        x_min = point_coord.x() - self.point_size
        x_max = point_coord.x() + self.point_size
        y_min = point_coord.y() - self.point_size
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
        ''' drawing '''
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # draw control point
        pen = QPen(Qt.black, 1)
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.setPen(pen)
        for point in self.control_points:
            painter.drawRect(QRect(point.x()-(self.point_size/2), point.y()-(self.point_size/2), self.point_size, self.point_size))
        # draw bezier curve
        if self.bezier_curve.bezier_points:
            pen = QPen(Qt.black, 1)
            painter.setPen(pen)
            painter.drawPolyline(QPolygonF(self.bezier_curve.bezier_points))
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # print(event.pos())
            if len(self.control_points) == 4:
                self.drag_idx = self.drag_index(event.pos())
                # print('drag_index:', self.drag_idx)
    
    def mouseMoveEvent(self, event):
        if self.drag_idx != -1:
            # update move control points
            self.control_points[self.drag_idx] = event.pos()
            parent_rect = self.rect()
            # x axis
            if self.control_points[self.drag_idx].x() < 0:
                self.control_points[self.drag_idx].setX(1 + (self.point_size / 2))
            elif self.control_points[self.drag_idx].x() > parent_rect.right():
                self.control_points[self.drag_idx].setX(parent_rect.right() - (self.point_size / 2))
            # y axis
            if self.control_points[self.drag_idx].y() < 0:
                self.control_points[self.drag_idx].setY(1 + (self.point_size / 2))
            elif self.control_points[self.drag_idx].y() > parent_rect.bottom():
                self.control_points[self.drag_idx].setY(parent_rect.bottom() - (self.point_size / 2))
            # recalculate bezier curve mid point
            self.bezier_curve.recalc(self.control_points[0], self.control_points[1], self.control_points[2], self.control_points[3], 0)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if len(self.control_points) < 4:
                # add control points
                control_point = event.pos()
                self.control_points.append(control_point)
                # calculate bezier curve mid point
                if len(self.control_points) == 4:      
                    self.bezier_curve.bezier(self.control_points[0], self.control_points[1], self.control_points[2], self.control_points[3], 0)
            else:
                self.drag_idx = -1
            self.update()

    def redraw_click_event(self):
        # clear initial
        self.control_points = list()
        self.bezier_curve = BezierCurve()
        self.drag_idx = -1
        self.setPixmap(self.canvas)