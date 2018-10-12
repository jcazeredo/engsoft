from PyQt5 import QtWidgets
from View.interface import Interface
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    engsoft = QtWidgets.QMainWindow()
    user_interface = Interface(engsoft)
    engsoft.show()
    sys.exit(app.exec_())