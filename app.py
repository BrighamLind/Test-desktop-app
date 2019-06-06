from PyQt5 import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)


class PyQtApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("My First PyQt Application")
        self.setWindowIcon(QtGui.QIcon("test-image-here.png"))


if __name__ == "__main__":
    myapp = PyQtApp()
    myapp.show()
    sys.exit(app.exec_())
