# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_case_file_manager.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_case_file_manager(object):
    def setupUi(self, Dialog_case_file_manager):
        Dialog_case_file_manager.setObjectName("Dialog_case_file_manager")
        Dialog_case_file_manager.resize(899, 570)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_case_file_manager)
        self.gridLayout.setObjectName("gridLayout")
        self.label_case = QtWidgets.QLabel(Dialog_case_file_manager)
        self.label_case.setMinimumSize(QtCore.QSize(0, 32))
        self.label_case.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_case.setObjectName("label_case")
        self.gridLayout.addWidget(self.label_case, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog_case_file_manager)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_view = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_view.setGeometry(QtCore.QRect(10, 30, 181, 25))
        self.pushButton_view.setObjectName("pushButton_view")
        self.pushButton_auto_assign = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_auto_assign.setGeometry(QtCore.QRect(10, 60, 381, 25))
        self.pushButton_auto_assign.setObjectName("pushButton_auto_assign")
        self.pushButton_add_files = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_add_files.setGeometry(QtCore.QRect(200, 30, 281, 25))
        self.pushButton_add_files.setObjectName("pushButton_add_files")
        self.pushButton_remove = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_remove.setGeometry(QtCore.QRect(490, 30, 381, 25))
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(660, 60, 211, 25))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog_case_file_manager)
        self.label_2.setMinimumSize(QtCore.QSize(0, 32))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Dialog_case_file_manager)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.textBrowser = QtWidgets.QTextBrowser(self.splitter)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 1)

        self.retranslateUi(Dialog_case_file_manager)
        self.buttonBox.accepted.connect(Dialog_case_file_manager.accept)
        self.buttonBox.rejected.connect(Dialog_case_file_manager.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_case_file_manager)

    def retranslateUi(self, Dialog_case_file_manager):
        _translate = QtCore.QCoreApplication.translate
        Dialog_case_file_manager.setWindowTitle(_translate("Dialog_case_file_manager", "Case file manager"))
        self.label_case.setText(_translate("Dialog_case_file_manager", "Case:"))
        self.groupBox.setTitle(_translate("Dialog_case_file_manager", "Actions"))
        self.pushButton_view.setText(_translate("Dialog_case_file_manager", "View file"))
        self.pushButton_auto_assign.setText(_translate("Dialog_case_file_manager", "Auto assign file text to case"))
        self.pushButton_add_files.setText(_translate("Dialog_case_file_manager", "Add selected files to case"))
        self.pushButton_remove.setText(_translate("Dialog_case_file_manager", "Remove selected files from case"))
        self.label_2.setText(_translate("Dialog_case_file_manager", "Can assign text in a file to this case. Right click to mark selected text in a file to assign to this case."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_case_file_manager = QtWidgets.QDialog()
    ui = Ui_Dialog_case_file_manager()
    ui.setupUi(Dialog_case_file_manager)
    Dialog_case_file_manager.show()
    sys.exit(app.exec_())