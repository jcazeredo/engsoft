from PyQt5 import QtWidgets
from View.interface import Interface
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    engsoft = QtWidgets.QMainWindow()
    user_interface = Interface(engsoft)
    engsoft.show()
    sys.exit(app.exec_())

# module_name, package_name, ClassName, method_name, \
# ExceptionName, function_name, GLOBAL_CONSTANT_NAME, \
# global_var_name, instance_var_name, function_parameter_name, local_var_name
