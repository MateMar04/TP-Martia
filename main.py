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
        self.pantalones = 0
        self.buzos = 0
        self.remeras = 0
        self.ventana_lista.show()

    @Slot()
    def agregar_pantalon(self):
        self.pantalones += int(self.ui.le_cant_pantalon.text())
        print(self.pantalones)
        self.ventana_lista.agregar_prendas("pantalones", self.pantalones)


    @Slot()
    def quitar_pantalon(self):
        self.pantalones -= int(self.ui.le_cant_pantalon.text())
        print(self.pantalones)

    @Slot()
    def agregar_buzo(self):
        self.buzos += int(self.ui.le_cant_buzo.text())
        print(self.buzos)

    @Slot()
    def quitar_buzo(self):
        self.buzos -= int(self.ui.le_cant_buzo.text())
        print(self.buzos)

    @Slot()
    def agregar_remera(self):
        self.remeras += int(self.ui.le_cant_remera.text())
        print(self.remeras)

    @Slot()
    def quitar_remera(self):
        self.remeras -= int(self.ui.le_cant_remera.text())
        print(self.remeras)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tiendaropa = MainWindow()
    tiendaropa.show()

    sys.exit(app.exec_())