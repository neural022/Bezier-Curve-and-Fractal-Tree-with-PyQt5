import sys
from PyQt5 import QtWidgets
from Bezier_Fractal_UI import Ui_Form

class MyWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        '''
        # variables:
        # label: bezier view
        # label_2: fractal view
        # pushButton: bezier view redraw button
        # horizontalSlider: fractal view level horizontal slider
        '''
        self.pushButton.clicked.connect(self.label.redraw_click_event)
        self.horizontalSlider.valueChanged.connect(self.label_2.level_change_event)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())