# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tiendaropa.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 797)
        MainWindow.setStyleSheet(u"font: 63 11pt \"URW Gothic L\";\n"
"background-color: rgb(173, 127, 168);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 390, 121, 31))
        self.label.setStyleSheet(u"b\n"
"background-color: rgb(65, 221, 218);")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 70, 711, 299))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cb_pantalon = QComboBox(self.formLayoutWidget)
        self.cb_pantalon.addItem("")
        self.cb_pantalon.addItem("")
        self.cb_pantalon.setObjectName(u"cb_pantalon")
        self.cb_pantalon.setStyleSheet(u"background-color: rgb(186, 189, 182);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_pantalon)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_pantalonagr = QPushButton(self.formLayoutWidget)
        self.pb_pantalonagr.setObjectName(u"pb_pantalonagr")
        self.pb_pantalonagr.setStyleSheet(u"background-color: rgb(173, 127, 168);")

        self.gridLayout.addWidget(self.pb_pantalonagr, 0, 0, 1, 1)

        self.pb_quitarpant = QPushButton(self.formLayoutWidget)
        self.pb_quitarpant.setObjectName(u"pb_quitarpant")
        self.pb_quitarpant.setStyleSheet(u"background-color: rgb(136, 138, 133);\n"
"background-color: rgb(173, 127, 168);")

        self.gridLayout.addWidget(self.pb_quitarpant, 0, 1, 1, 1)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.gridLayout)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.cb_buzo = QComboBox(self.formLayoutWidget)
        self.cb_buzo.addItem("")
        self.cb_buzo.addItem("")
        self.cb_buzo.setObjectName(u"cb_buzo")
        self.cb_buzo.setStyleSheet(u"background-color: rgb(186, 189, 182);")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cb_buzo)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)

        self.cb_remera = QComboBox(self.formLayoutWidget)
        self.cb_remera.addItem("")
        self.cb_remera.addItem("")
        self.cb_remera.setObjectName(u"cb_remera")
        self.cb_remera.setStyleSheet(u"background-color: rgb(186, 189, 182);")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cb_remera)

        self.cantidad = QLabel(self.formLayoutWidget)
        self.cantidad.setObjectName(u"cantidad")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.cantidad)

        self.le_remera = QLineEdit(self.formLayoutWidget)
        self.le_remera.setObjectName(u"le_remera")
        self.le_remera.setStyleSheet(u"\n"
"background-color: rgb(136, 138, 133);")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.le_remera)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_buzoagr = QPushButton(self.formLayoutWidget)
        self.pb_buzoagr.setObjectName(u"pb_buzoagr")

        self.horizontalLayout.addWidget(self.pb_buzoagr)

        self.pb_quitbuzp = QPushButton(self.formLayoutWidget)
        self.pb_quitbuzp.setObjectName(u"pb_quitbuzp")

        self.horizontalLayout.addWidget(self.pb_quitbuzp)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_remeraagr = QPushButton(self.formLayoutWidget)
        self.pb_remeraagr.setObjectName(u"pb_remeraagr")

        self.horizontalLayout_2.addWidget(self.pb_remeraagr)

        self.pb_remeraquit = QPushButton(self.formLayoutWidget)
        self.pb_remeraquit.setObjectName(u"pb_remeraquit")

        self.horizontalLayout_2.addWidget(self.pb_remeraquit)


        self.formLayout.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.le_buzo = QLineEdit(self.formLayoutWidget)
        self.le_buzo.setObjectName(u"le_buzo")
        self.le_buzo.setStyleSheet(u"background-color: rgb(136, 138, 133);")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.le_buzo)

        self.le_pantalon = QLineEdit(self.formLayoutWidget)
        self.le_pantalon.setObjectName(u"le_pantalon")
        self.le_pantalon.setStyleSheet(u"background-color: rgb(136, 138, 133);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_pantalon)

        self.lb_stock = QLabel(self.centralwidget)
        self.lb_stock.setObjectName(u"lb_stock")
        self.lb_stock.setGeometry(QRect(110, 390, 421, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 788, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.pb_pantalonagr.clicked.connect(MainWindow.agregarpant)
        self.pb_quitarpant.clicked.connect(MainWindow.quitarpant)
        self.pb_buzoagr.clicked.connect(MainWindow.agregarbuzo)
        self.pb_quitbuzp.clicked.connect(MainWindow.quitarbuzo)
        self.pb_remeraagr.clicked.connect(MainWindow.agregarremera)
        self.pb_remeraquit.clicked.connect(MainWindow.quitarremera)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#000000;\">stock</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'URW Gothic L'; font-size:11pt; font-weight:56; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#8f5902;\">pantalon</span></p></body></html>", None))
        self.cb_pantalon.setItemText(0, QCoreApplication.translate("MainWindow", u"jean", None))
        self.cb_pantalon.setItemText(1, QCoreApplication.translate("MainWindow", u"short", None))

        self.pb_pantalonagr.setText(QCoreApplication.translate("MainWindow", u"agregar pantalon", None))
        self.pb_quitarpant.setText(QCoreApplication.translate("MainWindow", u"quitar pantalon", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600; font-style:italic; color:#8f5902;\">buzo</span></p></body></html>", None))
        self.cb_buzo.setItemText(0, QCoreApplication.translate("MainWindow", u"deportivo", None))
        self.cb_buzo.setItemText(1, QCoreApplication.translate("MainWindow", u"clasico", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600; font-style:italic; color:#8f5902;\">remera</span></p></body></html>", None))
        self.cb_remera.setItemText(0, QCoreApplication.translate("MainWindow", u"corta", None))
        self.cb_remera.setItemText(1, QCoreApplication.translate("MainWindow", u"larga", None))

        self.cantidad.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic; color:#2e3436;\">cantidad</span></p></body></html>", None))
        self.le_remera.setInputMask(QCoreApplication.translate("MainWindow", u"999", None))
        self.le_remera.setText("")
        self.pb_buzoagr.setText(QCoreApplication.translate("MainWindow", u"agregar buzo", None))
        self.pb_quitbuzp.setText(QCoreApplication.translate("MainWindow", u"quitar buzo", None))
        self.pb_remeraagr.setText(QCoreApplication.translate("MainWindow", u"agregar remera", None))
        self.pb_remeraquit.setText(QCoreApplication.translate("MainWindow", u"quitar remera", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic; color:#2e3436;\">cantidad</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#2e3436;\">cantidad</span></p></body></html>", None))
        self.le_buzo.setInputMask(QCoreApplication.translate("MainWindow", u"999", None))
        self.le_buzo.setText("")
        self.le_pantalon.setInputMask(QCoreApplication.translate("MainWindow", u"999", None))
        self.lb_stock.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

