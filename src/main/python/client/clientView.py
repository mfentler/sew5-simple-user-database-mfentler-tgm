# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientView.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Client(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.allStudentsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.allStudentsTable.setGeometry(QtCore.QRect(20, 80, 651, 401))
        self.allStudentsTable.setMaximumSize(QtCore.QSize(981, 16777215))
        self.allStudentsTable.setAlternatingRowColors(True)
        self.allStudentsTable.setShowGrid(True)
        self.allStudentsTable.setWordWrap(True)
        self.allStudentsTable.setCornerButtonEnabled(True)
        self.allStudentsTable.setRowCount(2)
        self.allStudentsTable.setColumnCount(5)
        self.allStudentsTable.setObjectName("allStudentsTable")
        item = QtWidgets.QTableWidgetItem()
        self.allStudentsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.allStudentsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.allStudentsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.allStudentsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.allStudentsTable.setHorizontalHeaderItem(4, item)
        self.loadStudent_button = QtWidgets.QPushButton(self.centralwidget)
        self.loadStudent_button.setGeometry(QtCore.QRect(20, 490, 93, 28))
        self.loadStudent_button.setObjectName("loadStudent_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(699, 30, 411, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.addStudent_username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.addStudent_username.setObjectName("addStudent_username")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.addStudent_username)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.addStudent_email = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.addStudent_email.setObjectName("addStudent_email")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.addStudent_email)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.addStudent_picture = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.addStudent_picture.setObjectName("addStudent_picture")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.addStudent_picture)
        self.addStudent_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.addStudent_button.setMaximumSize(QtCore.QSize(93, 16777215))
        self.addStudent_button.setObjectName("addStudent_button")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.addStudent_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.allStudentsTable.setSortingEnabled(False)
        item = self.allStudentsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Username"))
        item = self.allStudentsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.allStudentsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Picture"))
        item = self.allStudentsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Edit"))
        item = self.allStudentsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Delete"))
        self.loadStudent_button.setText(_translate("MainWindow", "Load"))
        self.label.setText(_translate("MainWindow", "All Students"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Add new student"))
        self.label_5.setText(_translate("MainWindow", "Email"))
        self.label_4.setText(_translate("MainWindow", "Picture"))
        self.addStudent_button.setText(_translate("MainWindow", "Add"))




