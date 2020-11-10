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
        ListWindow.resize(472, 400)
        self.centralwidget = QWidget(ListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tb_stock = QTableWidget(self.centralwidget)
        if (self.tb_stock.columnCount() < 3):
            self.tb_stock.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_stock.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_stock.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_stock.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tb_stock.setObjectName(u"tb_stock")
        self.tb_stock.setGeometry(QRect(-10, 0, 481, 381))
        self.tb_stock.setStyleSheet(u"background-color: rgb(173, 127, 168);\n"
"font: 57 11pt \"Ubuntu\";")
        ListWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ListWindow)
        self.statusbar.setObjectName(u"statusbar")
        ListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListWindow)

        QMetaObject.connectSlotsByName(ListWindow)
    # setupUi

    def retranslateUi(self, ListWindow):
        ListWindow.setWindowTitle(QCoreApplication.translate("ListWindow", u"Stock de Ropa", None))
        ___qtablewidgetitem = self.tb_stock.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ListWindow", u"Pantalones", None));
        ___qtablewidgetitem1 = self.tb_stock.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ListWindow", u"Buzos", None));
        ___qtablewidgetitem2 = self.tb_stock.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ListWindow", u"Remeras", None));
    # retranslateUi

