import pickle
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

        self.datos = self.read_file()

        self.jeans = self.datos[0]
        self.shorts = self.datos[1]
        self.buzos_deportivos = self.datos[2]
        self.buzos_clasicos = self.datos[3]
        self.remeras_cortas = self.datos[4]
        self.remeras_largas = self.datos[5]

        self.precio_jeans = 100
        self.precio_shorts = 80
        self.precio_buzo_clasico = 150
        self.precio_buzo_deportivo = 130
        self.precio_remera_larga = 50
        self.precio_remera_corta = 30

        self.ventana_lista.agregar_prendas(0, 0, self.jeans)
        self.ventana_lista.agregar_prendas(0, 1, self.shorts)
        self.ventana_lista.agregar_prendas(0, 2, self.buzos_deportivos)
        self.ventana_lista.agregar_prendas(0, 3, self.buzos_clasicos)
        self.ventana_lista.agregar_prendas(0, 4, self.remeras_cortas)
        self.ventana_lista.agregar_prendas(0, 5, self.remeras_largas)

        self.ventana_lista.show()

    @Slot()
    def actualizar_precio_slot(self):
        if self.ui.cb_pantalon.currentText() == "jean":
            if len(self.ui.le_cant_pantalon.text()) > 0:
                self.ui.lb_precio_pantalones.setText(str(int(self.ui.le_cant_pantalon.text()) * self.precio_jeans))
                jeans = int(self.ui.le_cant_pantalon.text()) * self.precio_jeans
            else:
                self.ui.lb_precio_pantalones.setText("0")
                jeans = 0
        else:
            if len(self.ui.le_cant_pantalon.text()) > 0:
                self.ui.lb_precio_pantalones.setText(str(int(self.ui.le_cant_pantalon.text()) * self.precio_shorts))
                shorts = int(self.ui.le_cant_pantalon.text()) * self.precio_shorts
            else:
                self.ui.lb_precio_pantalones.setText("0")
                shorts = 0

        if self.ui.cb_buzo.currentText() == "deportivo":
            if len(self.ui.le_cant_buzo.text()) > 0:
                self.ui.lb_precio_buzo.setText(str(int(self.ui.le_cant_buzo.text()) * self.precio_buzo_deportivo))
                buzos_deportivos = int(self.ui.le_cant_buzo.text()) * self.precio_buzo_deportivo
            else:
                self.ui.lb_precio_buzo.setText("0")
                buzos_deportivos = 0
        else:
            if len(self.ui.le_cant_pantalon.text()) > 0:
                self.ui.lb_precio_buzo.setText(str(int(self.ui.le_cant_buzo.text()) * self.precio_buzo_clasico))
                buzos_clasicos = int(self.ui.le_cant_buzo.text()) * self.precio_buzo_clasico
            else:
                self.ui.lb_precio_buzo.setText("0")
                buzos_clasicos = 0

        if self.ui.cb_remera.currentText() == "corta":
            if len(self.ui.le_cant_remera.text()) > 0:
                self.ui.lb_precio_remera.setText(str(int(self.ui.le_cant_remera.text()) * self.precio_remera_corta))
                remeras_cortas = int(self.ui.le_cant_remera.text()) * self.precio_remera_corta
            else:
                self.ui.lb_precio_remera.setText("0")
                remeras_cortas = 0
        else:
            if len(self.ui.le_cant_pantalon.text()) > 0:
                self.ui.lb_precio_remera.setText(str(int(self.ui.le_cant_remera.text()) * self.precio_remera_larga))
                remeras_largas = int(self.ui.le_cant_remera.text()) * self.precio_remera_larga
            else:
                self.ui.lb_precio_remera.setText("0")
                remeras_largas = 0

    @Slot()
    def agregar_pantalon(self):
        if self.ui.cb_pantalon.currentText() == "jean":
            self.jeans += int(self.ui.le_cant_pantalon.text())
            self.ventana_lista.agregar_prendas(0, 0, self.jeans)
        else:
            self.shorts += int(self.ui.le_cant_pantalon.text())
            self.ventana_lista.agregar_prendas(0, 1, self.shorts)

    @Slot()
    def quitar_pantalon(self):
        if self.ui.cb_pantalon.currentText() == "jean":
            self.jeans -= int(self.ui.le_cant_pantalon.text())
            self.ventana_lista.agregar_prendas(0, 0, self.jeans)
        else:
            self.shorts -= int(self.ui.le_cant_pantalon.text())
            self.ventana_lista.agregar_prendas(0, 1, self.shorts)

    @Slot()
    def agregar_buzo(self):
        if self.ui.cb_buzo.currentText() == "deportivo":
            self.buzos_deportivos += int(self.ui.le_cant_buzo.text())
            self.ventana_lista.agregar_prendas(0, 2, self.buzos_deportivos)
        else:
            self.buzos_clasicos += int(self.ui.le_cant_buzo.text())
            self.ventana_lista.agregar_prendas(0, 3, self.buzos_clasicos)

    @Slot()
    def quitar_buzo(self):
        if self.ui.cb_buzo.currentText() == "deportivo":
            self.buzos_deportivos -= int(self.ui.le_cant_buzo.text())
            self.ventana_lista.agregar_prendas(0, 2, self.buzos_deportivos)
        else:
            self.buzos_clasicos -= int(self.ui.le_cant_buzo.text())
            self.ventana_lista.agregar_prendas(0, 3, self.buzos_clasicos)

    @Slot()
    def agregar_remera(self):
        if self.ui.cb_remera.currentText() == "corta":
            self.remeras_cortas += int(self.ui.le_cant_remera.text())
            self.ventana_lista.agregar_prendas(0, 4, self.remeras_cortas)
        else:
            self.remeras_largas += int(self.ui.le_cant_remera.text())
            self.ventana_lista.agregar_prendas(0, 5, self.remeras_largas)

    @Slot()
    def quitar_remera(self):
        if self.ui.cb_remera.currentText() == "corta":
            self.remeras_cortas -= int(self.ui.le_cant_remera.text())
            self.ventana_lista.agregar_prendas(0, 4, self.remeras_cortas)
        else:
            self.remeras_largas -= int(self.ui.le_cant_remera.text())
            self.ventana_lista.agregar_prendas(0, 5, self.remeras_largas)

    @Slot()
    def cerrar_ventana(self):
        self.window().close()

    @Slot()
    def borrar_stock(self):
        self.jeans -= self.jeans
        self.shorts -= self.shorts
        self.buzos_deportivos -= self.buzos_deportivos
        self.buzos_clasicos -= self.buzos_clasicos
        self.remeras_cortas -= self.remeras_cortas
        self.remeras_largas -= self.remeras_largas

        self.ventana_lista.agregar_prendas(0, 0, self.jeans)
        self.ventana_lista.agregar_prendas(0, 1, self.shorts)
        self.ventana_lista.agregar_prendas(0, 2, self.buzos_deportivos)
        self.ventana_lista.agregar_prendas(0, 3, self.buzos_clasicos)
        self.ventana_lista.agregar_prendas(0, 4, self.remeras_cortas)
        self.ventana_lista.agregar_prendas(0, 5, self.remeras_largas)

    @Slot()
    def save_file(self):
        with open("datos.v", "wb") as f:
            self.datos = [self.jeans, self.shorts, self.buzos_deportivos, self.buzos_clasicos, self.remeras_cortas, self.remeras_largas]
            pickle.dump(self.datos, f)

    def read_file(self):
        try:
            with open("datos.v", "rb") as f:
                datos = pickle.load(f)
        except FileNotFoundError:
            datos = []
        return datos


if __name__ == "__main__":
    app = QApplication(sys.argv)

    tienda_ropa = MainWindow()
    tienda_ropa.show()

    sys.exit(app.exec_())
