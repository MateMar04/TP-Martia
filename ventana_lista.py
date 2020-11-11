import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import Slot

from lista_ui import Ui_ListWindow


class ListWindow(QMainWindow):
    def __init__(self):
        super(ListWindow, self).__init__()
        self.ui = Ui_ListWindow()
        self.ui.setupUi(self)

    def agregar_prendas(self, f, c, cantidad):
        self.ui.tb_stock.setItem(f, c, QtWidgets.QTableWidgetItem(str(cantidad)))
