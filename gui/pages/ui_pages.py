# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagestOjhmV.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(933, 658)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        StackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout = QHBoxLayout(self.page_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        StackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_2 = QHBoxLayout(self.page_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        StackedWidget.addWidget(self.page_3)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"P\u00e1gina Inicial", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"P\u00e1gina 2", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"P\u00e1gina 3", None))
    # retranslateUi

