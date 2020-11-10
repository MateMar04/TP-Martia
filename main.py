

import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import Slot

from tiendaropa_ui import Ui_MainWindow
from ventana_lista import ListWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ventana_lista = ListWindow()
        self.ventana_lista.show()

    @Slot()
    def agregar_pantalon(self):
        pass

    @Slot()
    def quitar_pantalon(self):
        pass

    @Slot()
    def agregar_buzo(self):
        pass

    @Slot()
    def quitar_buzo(self):
        pass

    @Slot()
    def agregar_remera(self):
        pass

    @Slot()
    def quitar_remera(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    tiendaropa = MainWindow()
    tiendaropa.show()

    sys.exit(app.exec_())