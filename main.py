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
        self.precio_pantalon = 100
        self.precio_buzo = 150
        self.precio_remera = 50

        self.ventana_lista.show()

    @Slot()
    def actualizar_precio_slot(self):
        #total = (int(self.ui.le_cant_remera.text()) * self.precio_remera) + (int(self.ui.le_cant_buzo.text()) * self.precio_buzo) + (int(self.ui.le_cant_pantalon.text()) * self.precio_pantalon)

        if len(self.ui.le_cant_pantalon.text()) > 0:
            self.ui.lb_precio_pantalones.setText(str(int(self.ui.le_cant_pantalon.text()) * self.precio_pantalon))
            #pantalones = int(self.ui.le_cant_pantalon.text()) * self.precio_pantalon
        else:
            self.ui.lb_precio_pantalones.setText("0")
            #pantalones = 0

        if len(self.ui.le_cant_buzo.text()) > 0:
            self.ui.lb_precio_buzo.setText(str(int(self.ui.le_cant_buzo.text()) * self.precio_buzo))
            #buzo = int(self.ui.le_cant_buzo.text()) * self.precio_buzo
        else:
            self.ui.lb_precio_buzo.setText("0")
            #buzo = 0

        if len(self.ui.le_cant_remera.text()) > 0:
            self.ui.lb_precio_remera.setText(str(int(self.ui.le_cant_remera.text()) * self.precio_remera))
            #remeras = int(self.ui.le_cant_remera.text()) * self.precio_remera
        else:
            self.ui.lb_precio_remera.setText("0")
            #remeras = 0

        #self.ui.lb_total.setText(str(remeras + buzo + pantalones))



    @Slot()
    def agregar_pantalon(self):
        self.pantalones += int(self.ui.le_cant_pantalon.text())
        print(self.pantalones)
        self.ventana_lista.agregar_prendas(0, 0, self.pantalones)

    @Slot()
    def quitar_pantalon(self):
        self.pantalones -= int(self.ui.le_cant_pantalon.text())
        self.ventana_lista.agregar_prendas(0, 0, self.pantalones)
        print(self.pantalones)

    @Slot()
    def agregar_buzo(self):
        self.buzos += int(self.ui.le_cant_buzo.text())
        self.ventana_lista.agregar_prendas(2, 0, self.buzos)
        print(self.buzos)

    @Slot()
    def quitar_buzo(self):
        self.buzos -= int(self.ui.le_cant_buzo.text())
        self.ventana_lista.agregar_prendas(2, 0, self.buzos)
        print(self.buzos)

    @Slot()
    def agregar_remera(self):
        self.remeras += int(self.ui.le_cant_remera.text())
        self.ventana_lista.agregar_prendas(4, 0, self.remeras)
        print(self.remeras)

    @Slot()
    def quitar_remera(self):
        self.remeras -= int(self.ui.le_cant_remera.text())
        self.ventana_lista.agregar_prendas(4, 0, self.remeras)
        print(self.remeras)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    tienda_ropa = MainWindow()
    tienda_ropa.show()

    sys.exit(app.exec_())
