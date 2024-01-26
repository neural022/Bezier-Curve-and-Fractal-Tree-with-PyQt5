# -*- coding: utf-8 -*-
"""
@author: george chen(neural022)
"""
from PyQt5 import QtWidgets
import PyQt5
from PyQt5.QtCore import QPointF, QLineF
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap, qRgb
from math import cos, sin

class Branch():
    def __init__(self, start_point, end_point, pen_style):
        self.line = QLineF(start_point, end_point)
        self.pen_style = pen_style

class Flower():
    def __init__(self, center_point, radius, pen_style):
        self.center_point = center_point
        self.radius = radius
        self.pen_style = pen_style

class FractalView(QtWidgets.QLabel):
    def __init__(self, level_label, horizental_slider, parent=None):
        super().__init__(parent)
        self.horizental_slider = horizental_slider
        self.level_label = level_label

        self.canvas = QPixmap(750, 600)
        self.canvas.fill(QColor("white"))
        self.setPixmap(self.canvas)
        # component setting
        self.max_level = self.horizental_slider.value()
        # branch setting
        self.theta = 120
        self.branch_commom_ratio = (3/4)
        self.branch_level = 1
        self.flower_level = 0
        self.tree_branches = list()
        self.tree_flower = list()
        # first branch
        self.first_branch = self.calc_first_branch()
        

    def calc_first_branch(self):
        width = float(self.pixmap().rect().width())
        height = float(self.pixmap().height())
        pen_style = QPen(QColor("brown"), 15)
        return Branch(QPointF(width/2, float(self.pixmap().rect().y())), QPointF(width/2, height), pen_style)

    def rotate(self, point, theta):
        return QPointF(cos(theta)*point.x() - sin(theta)*point.y(), sin(theta)*point.x() + cos(theta)*point.y())

    def first_item(self, geo_seq_sum, commom_ratio, item_num):
        return geo_seq_sum*(1-commom_ratio)  / (1-commom_ratio**(item_num))
    
    def flower(self, center_point, diameter, width, level):
        if level > 0:
            ''' style process '''
            # style attribute setting
            if level > 1:
                pen_style = QPen(QColor(qRgb(255, 204, 229)), width)
            else:
                pen_style = QPen(QColor("pink"), width)
            ''' flower process '''
            # target point
            target_x = center_point.x()
            target_y = center_point.y()
            target_point = QPointF(target_x, target_y)
            radius = diameter/2
            self.tree_flower.append(Flower(target_point, radius, pen_style))
            # width and diameter
            diameter /= 2
            width -= 1
            # petals
            # Because the coordinate system is reflective
            # upper left, upper right, lower left, lower right
            for i in range(60, 180, 60):
                rotate_point = self.rotate(QPointF(radius, 0), i)
                self.flower(rotate_point+target_point, diameter, width, level-1)
                rotate_point = self.rotate(QPointF(-radius, 0), -i)
                self.flower(rotate_point+target_point, diameter, width, level-1)
            # up and bottom
            rotate_point = self.rotate(QPointF(radius, 0), 300)
            self.flower(rotate_point+target_point, diameter, width, level-1)
            rotate_point = self.rotate(QPointF(radius, 0), -300)
            self.flower(rotate_point+target_point, diameter, width, level-1)

    def branch(self, start_point, dirX, dirY, theta, width, height, level):
        ''' recursive branch '''
        if level > 0:
            ''' style process '''
            # style attribute setting
            if height < 60:
                pen_style = QPen(QColor("green"), width)
            elif height >= 60:
                pen_style = QPen(QColor("brown"), width)
            ''' branch process '''
            # target point
            target_x = int(start_point.x() + height * dirX)
            target_y = int(start_point.y() + height * dirY)
            target_point = QPointF(target_x, target_y)
            # print(start_point.x(), start_point.y(), target_x, target_y)
            # print('branch level:', level)
            self.tree_branches.append(Branch(start_point, target_point, pen_style))
            ''' Flower process '''
            if self.max_level > 7 and level == 1:
                self.flower(target_point, diameter=30, width=4, level=self.flower_level)
            ''' branch procces cont '''
            # new start point
            new_start_point = target_point
            # width and height
            width -= 2
            height *= self.branch_commom_ratio
            # rotate left branch
            rotate_point = self.rotate(QPointF(dirX, dirY), theta)
            self.branch(new_start_point, rotate_point.x(), rotate_point.y(), theta, width, height, level-1)
            # rotate right branch
            rotate_point = self.rotate(QPointF(dirX, dirY), -theta)
            self.branch(new_start_point, rotate_point.x(), rotate_point.y(), theta, width, height, level-1)
    
    
    def paintEvent(self, event):
        super(FractalView, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        if self.max_level == 1:
            # draw first branch
            painter.setPen(self.first_branch.pen_style)
            painter.drawLine(self.first_branch.line)
        else:
            # draw branch
            for branch in self.tree_branches:
                painter.setPen(branch.pen_style)
                painter.drawLine(branch.line)
            # draw flower
            for flower in self.tree_flower:
                painter.setPen(flower.pen_style)
                painter.drawEllipse(flower.center_point, flower.radius, flower.radius)
                
    def level_change_event(self):
        # component setting
        self.setPixmap(self.canvas)
        self.max_level = self.horizental_slider.value()
        self.level_label.setText("Level %s :" % str(self.max_level))
        self.tree_branches = list()
        self.tree_flower = list()
        # flower
        if self.max_level > 7:
            self.flower_level = self.max_level - 7
        # branch
        if self.max_level > 7:
            self.branch_level = 7
        else:
            self.branch_level = self.max_level
        first_branch_height = self.first_item(self.pixmap().height(), self.branch_commom_ratio, self.branch_level)
        self.branch(QPointF(int(self.rect().width()/2), int(self.rect().height())), float(0), float(-1), theta=self.theta, width=15, height=first_branch_height, level=self.branch_level)
        
