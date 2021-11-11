# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bezier_fractal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from BezierView import BezierView
from FractalView import FractalView


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 700)
        Form.setMinimumSize(QtCore.QSize(650, 700))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        Form.setFont(font)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 9, 630, 700))
        self.tabWidget.setMinimumSize(QtCore.QSize(630, 700))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(270, 620, 101, 31))
        self.pushButton.setObjectName("pushButton")

        # BezierView
        self.label = BezierView(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.label.setMinimumSize(QtCore.QSize(600, 600))
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(0)
        self.label.setText("")
        self.label.setObjectName("label")

        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(210, 620, 47, 12))
        self.label_3.setObjectName("label_3")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(260, 620, 160, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")

        # FractalView
        self.label_2 = FractalView(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.label_2.setMinimumSize(QtCore.QSize(600, 600))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(0)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Redraw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Bezier Curve"))
        self.label_3.setText(_translate("Form", "Level:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Fractral Tree"))
