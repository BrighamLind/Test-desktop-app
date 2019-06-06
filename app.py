from PyQt5 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)


class PyQtApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("My First PyQt Application :P")
        self.setWindowIcon(QtGui.QIcon(
            "static/assets/images/logo/Python-Logo.png"))

        self.setMinimumWidth(resolution.width() / 3)
        self.setMinimumHeight(resolution.height() / 1.5)
        self.setStyleSheet(
            "QWidget {background-color: rgba(6, 25, 31, 255);} QScrollBar:horizontal {width: 1px; height: 1px; background-color: rgba(6, 25, 31, 255);} QScrollBar:vertical {width: 1px; height: 1px; background-color: rgba(6, 25, 31, 255);}")
        self.textf = QtWidgets.QTextEdit(self)
        self.textf.setPlaceholderText("Results...")
        self.textf.setStyleSheet(
            "margin: 1px; padding 7px; background-color: rgba(3, 72, 95, 100); color: rgba(255, 255, 255, 100); border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0, 0, 0, 100);")

        self.btn1 = Button(self)
        self.btn1.setText("▼")
        self.btn1.setFixedWidth(72)
        self.btn1.setFont(Button.font_btn)
        self.btn2 = Button(self)
        self.btn2.setText("▼")
        self.btn2.setFixedWidth(72)
        self.btn2.setFont(Button.font_btn)
        self.btn3 = Button(self)
        self.btn3.setText("▼")
        self.btn3.setFixedWidth(72)
        self.btn3.setFont(Button.font_btn)
        self.btn4 = Button(self)
        self.btn4.setText("▼")
        self.btn4.setFixedWidth(72)
        self.btn4.setFont(Button.font_btn)
        self.btn5 = Button(self)
        self.btn5.setText("▼")
        self.btn5.setFixedWidth(72)
        self.btn5.setFont(Button.font_btn)
        self.btn6 = Button(self)
        self.btn6.setText("▼")
        self.btn6.setFixedWidth(72)
        self.btn6.setFont(Button.font_btn)
        self.btn7 = Button(self)
        self.btn7.setText("▼")
        self.btn7.setFixedWidth(72)
        self.btn7.setFont(Button.font_btn)

        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.addWidget(self.textf, 0, 0, 14, 13)
        self.grid1.addWidget(self.btn1, 0, 14, 1, 1)
        self.grid1.addWidget(self.btn2, 1, 14, 1, 1)
        self.grid1.addWidget(self.btn3, 2, 14, 1, 1)
        self.grid1.addWidget(self.btn4, 3, 14, 1, 1)
        self.grid1.addWidget(self.btn5, 4, 14, 1, 1)
        self.grid1.addWidget(self.btn6, 5, 14, 1, 1)
        self.grid1.addWidget(self.btn7, 6, 14, 1, 1)
        self.grid1.setContentsMargins(7, 7, 7, 7)
        self.setLayout(self.grid1)


class Button(QtWidgets.QPushButton):
    font_btn = QtGui.QFont()
    font_btn.setFamily("Segoe UI Symbol")
    font_btn.setPointSize(10)
    font_btn.setWeight(95)

    def __init__(self, parent=None):
        super(Button, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(153, 78, 0, 100); color: rgba(255, 255, 255, 100); border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(198, 102, 0, 100);")

    def enterEvent(self, event):
        self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(244, 125, 0, 100); color rgba(255, 255, 255, 100); border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(244, 125, 0, 100);")

    def leaveEvent(self, event):
        self.setStyleSheet(
            "margin: 1px; padding: 7px; background-color: rgba(153, 78, 0, 100); color: rgba(255, 255, 255, 100); border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(198, 102, 0, 100);")


if __name__ == "__main__":
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = PyQtApp()
    myapp.setWindowOpacity(1)
    myapp.show()
    myapp.move(resolution.center() - myapp.rect().center())
    sys.exit(app.exec_())
else:
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
