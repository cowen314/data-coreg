# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(220, 510, 322, 27))
        self.horizontalLayout = QHBoxLayout(self.gridLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.startDateLabel = QLabel(self.gridLayoutWidget)
        self.startDateLabel.setObjectName(u"startDateLabel")

        self.horizontalLayout.addWidget(self.startDateLabel)

        self.startDate = QDateEdit(self.gridLayoutWidget)
        self.startDate.setObjectName(u"startDate")

        self.horizontalLayout.addWidget(self.startDate)

        self.endDateLabel = QLabel(self.gridLayoutWidget)
        self.endDateLabel.setObjectName(u"endDateLabel")

        self.horizontalLayout.addWidget(self.endDateLabel)

        self.endDate = QDateEdit(self.gridLayoutWidget)
        self.endDate.setObjectName(u"endDate")

        self.horizontalLayout.addWidget(self.endDate)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startDateLabel.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
#if QT_CONFIG(tooltip)
        self.startDate.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Start Date</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.endDateLabel.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
#if QT_CONFIG(tooltip)
        self.endDate.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>End Date</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

