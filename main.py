import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import Slot

from tiendaropa_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot()
    def agregarpant(self):
        pass

    @Slot()
    def quitarpant(self):
        pass

    @Slot()
    def agregarbuzo(self):
        pass

    @Slot()
    def quitarbuzo(self):
        pass

    @Slot()
    def agregarremera(self):
        pass

    @Slot()
    def quitarremera(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    tiendaropa = MainWindow()
    tiendaropa.show()

    sys.exit(app.exec_())