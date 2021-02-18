# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nnldemo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NNLDemo(object):
    def setupUi(self, NNLDemo):
        NNLDemo.setObjectName("NNLDemo")
        NNLDemo.resize(498, 158)
        self.centralwidget = QtWidgets.QWidget(NNLDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_first_name = QtWidgets.QLabel(self.centralwidget)
        self.label_first_name.setObjectName("label_first_name")
        self.horizontalLayout.addWidget(self.label_first_name)
        self.le_first_name = QtWidgets.QLineEdit(self.centralwidget)
        self.le_first_name.setObjectName("le_first_name")
        self.horizontalLayout.addWidget(self.le_first_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_last_name = QtWidgets.QLabel(self.centralwidget)
        self.label_last_name.setObjectName("label_last_name")
        self.horizontalLayout_2.addWidget(self.label_last_name)
        self.le_last_name = QtWidgets.QLineEdit(self.centralwidget)
        self.le_last_name.setObjectName("le_last_name")
        self.horizontalLayout_2.addWidget(self.le_last_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_yes = QtWidgets.QPushButton(self.centralwidget)
        self.bt_yes.setObjectName("bt_yes")
        self.horizontalLayout_3.addWidget(self.bt_yes)
        self.bt_no = QtWidgets.QPushButton(self.centralwidget)
        self.bt_no.setObjectName("bt_no")
        self.horizontalLayout_3.addWidget(self.bt_no)
        self.bt_maybe = QtWidgets.QPushButton(self.centralwidget)
        self.bt_maybe.setObjectName("bt_maybe")
        self.horizontalLayout_3.addWidget(self.bt_maybe)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        NNLDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NNLDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAnimals = QtWidgets.QMenu(self.menubar)
        self.menuAnimals.setObjectName("menuAnimals")
        NNLDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NNLDemo)
        self.statusbar.setObjectName("statusbar")
        NNLDemo.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(NNLDemo)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(NNLDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCut = QtWidgets.QAction(NNLDemo)
        self.actionCut.setObjectName("actionCut")
        self.actionWombat = QtWidgets.QAction(NNLDemo)
        self.actionWombat.setObjectName("actionWombat")
        self.actionHoney_Badger = QtWidgets.QAction(NNLDemo)
        self.actionHoney_Badger.setObjectName("actionHoney_Badger")
        self.actionPine_Marten = QtWidgets.QAction(NNLDemo)
        self.actionPine_Marten.setObjectName("actionPine_Marten")
        self.actionLeast_weasel = QtWidgets.QAction(NNLDemo)
        self.actionLeast_weasel.setObjectName("actionLeast_weasel")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCut)
        self.menuAnimals.addAction(self.actionWombat)
        self.menuAnimals.addAction(self.actionHoney_Badger)
        self.menuAnimals.addAction(self.actionPine_Marten)
        self.menuAnimals.addAction(self.actionLeast_weasel)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAnimals.menuAction())
        self.label_first_name.setBuddy(self.le_first_name)
        self.label_last_name.setBuddy(self.le_last_name)

        self.retranslateUi(NNLDemo)
        self.actionQuit.triggered.connect(NNLDemo.close)
        QtCore.QMetaObject.connectSlotsByName(NNLDemo)
        NNLDemo.setTabOrder(self.le_first_name, self.le_last_name)
        NNLDemo.setTabOrder(self.le_last_name, self.bt_yes)
        NNLDemo.setTabOrder(self.bt_yes, self.bt_no)
        NNLDemo.setTabOrder(self.bt_no, self.bt_maybe)

    def retranslateUi(self, NNLDemo):
        _translate = QtCore.QCoreApplication.translate
        NNLDemo.setWindowTitle(_translate("NNLDemo", "NNL PyQt5 Demo"))
        self.label_first_name.setText(_translate("NNLDemo", "FIrst Name"))
        self.label_last_name.setText(_translate("NNLDemo", "Last Name"))
        self.bt_yes.setText(_translate("NNLDemo", "Yes"))
        self.bt_no.setText(_translate("NNLDemo", "No"))
        self.bt_maybe.setText(_translate("NNLDemo", "Maybe"))
        self.menuFile.setTitle(_translate("NNLDemo", "File"))
        self.menuEdit.setTitle(_translate("NNLDemo", "Edit"))
        self.menuAnimals.setTitle(_translate("NNLDemo", "Animals"))
        self.actionOpen.setText(_translate("NNLDemo", "Open..."))
        self.actionQuit.setText(_translate("NNLDemo", "Quit"))
        self.actionCut.setText(_translate("NNLDemo", "Cut"))
        self.actionWombat.setText(_translate("NNLDemo", "Wombat"))
        self.actionHoney_Badger.setText(_translate("NNLDemo", "Honey Badger"))
        self.actionPine_Marten.setText(_translate("NNLDemo", "Pine Marten"))
        self.actionLeast_weasel.setText(_translate("NNLDemo", "Least weasel"))
