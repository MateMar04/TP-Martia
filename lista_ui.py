# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lista.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ListWindow(object):
    def setupUi(self, ListWindow):
        if not ListWindow.objectName():
            ListWindow.setObjectName(u"ListWindow")
        ListWindow.resize(470, 388)
        self.centralwidget = QWidget(ListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tb_stock = QTableWidget(self.centralwidget)
        if (self.tb_stock.columnCount() < 1):
            self.tb_stock.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_stock.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tb_stock.rowCount() < 6):
            self.tb_stock.setRowCount(6)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_stock.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_stock.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_stock.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_stock.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_stock.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_stock.setVerticalHeaderItem(5, __qtablewidgetitem6)
        self.tb_stock.setObjectName(u"tb_stock")
        self.tb_stock.setGeometry(QRect(0, 0, 481, 391))
        self.tb_stock.setStyleSheet(u"background-color: rgb(173, 127, 168);\n"
"font: 57 11pt \"Ubuntu\";")
        self.tb_stock.horizontalHeader().setDefaultSectionSize(325)
        self.tb_stock.verticalHeader().setDefaultSectionSize(45)
        ListWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ListWindow)

        QMetaObject.connectSlotsByName(ListWindow)
    # setupUi

    def retranslateUi(self, ListWindow):
        ListWindow.setWindowTitle(QCoreApplication.translate("ListWindow", u"Stock de Ropa", None))
        ___qtablewidgetitem = self.tb_stock.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ListWindow", u"Cantidad", None));
        ___qtablewidgetitem1 = self.tb_stock.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ListWindow", u"Jean", None));
        ___qtablewidgetitem2 = self.tb_stock.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ListWindow", u"Short", None));
        ___qtablewidgetitem3 = self.tb_stock.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ListWindow", u"Buzo Deportivo", None));
        ___qtablewidgetitem4 = self.tb_stock.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ListWindow", u"Buzo Clasico", None));
        ___qtablewidgetitem5 = self.tb_stock.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ListWindow", u"Remera m. Corta", None));
        ___qtablewidgetitem6 = self.tb_stock.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ListWindow", u"Remera m. Larga", None));
    # retranslateUi

