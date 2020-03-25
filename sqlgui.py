# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sqlgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 515)
        MainWindow.setStyleSheet("QLabel{\n"
"font: 12pt \"楷体\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:9px;\n"
"}\n"
"\n"
"QCheckBox{\n"
"font: 11pt \"楷体\";\n"
"}\n"
"QPushButton{\n"
"font: 11pt \"楷体\";\n"
"background-color: rgb(57, 209, 255);\n"
"border-radius:9px;\n"
"}\n"
"\n"
"QTextEdit#sql_te{\n"
"border:none;\n"
"}\n"
"QTextEdit#view_te{\n"
"border:none;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 311, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.acc_le = QtWidgets.QLineEdit(self.frame)
        self.acc_le.setGeometry(QtCore.QRect(140, 10, 151, 31))
        self.acc_le.setObjectName("acc_le")
        self.pwd_le = QtWidgets.QLineEdit(self.frame)
        self.pwd_le.setGeometry(QtCore.QRect(140, 50, 151, 31))
        self.pwd_le.setObjectName("pwd_le")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 101, 31))
        self.label_2.setObjectName("label_2")
        self.login_btn = QtWidgets.QPushButton(self.frame)
        self.login_btn.setGeometry(QtCore.QRect(30, 130, 261, 28))
        self.login_btn.setObjectName("login_btn")
        self.remerber_pwd = QtWidgets.QCheckBox(self.frame)
        self.remerber_pwd.setGeometry(QtCore.QRect(30, 100, 101, 19))
        self.remerber_pwd.setObjectName("remerber_pwd")
        self.auto_login = QtWidgets.QCheckBox(self.frame)
        self.auto_login.setGeometry(QtCore.QRect(160, 100, 101, 19))
        self.auto_login.setObjectName("auto_login")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 190, 311, 311))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.db_cb = QtWidgets.QComboBox(self.frame_2)
        self.db_cb.setGeometry(QtCore.QRect(120, 10, 161, 31))
        self.db_cb.setObjectName("db_cb")
        self.excute_btn = QtWidgets.QPushButton(self.frame_2)
        self.excute_btn.setGeometry(QtCore.QRect(30, 170, 261, 28))
        self.excute_btn.setObjectName("excute_btn")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.label_3.setObjectName("label_3")
        self.sql_te = QtWidgets.QTextEdit(self.frame_2)
        self.sql_te.setGeometry(QtCore.QRect(30, 50, 251, 91))
        self.sql_te.setDocumentTitle("")
        self.sql_te.setObjectName("sql_te")
        self.result_te = QtWidgets.QTextEdit(self.frame_2)
        self.result_te.setGeometry(QtCore.QRect(30, 220, 251, 61))
        self.result_te.setObjectName("result_te")
        self.create_db = QtWidgets.QPushButton(self.centralwidget)
        self.create_db.setGeometry(QtCore.QRect(320, 30, 93, 28))
        self.create_db.setObjectName("create_db")
        self.create_table = QtWidgets.QPushButton(self.centralwidget)
        self.create_table.setGeometry(QtCore.QRect(320, 70, 93, 28))
        self.create_table.setObjectName("create_table")
        self.select_data = QtWidgets.QPushButton(self.centralwidget)
        self.select_data.setGeometry(QtCore.QRect(550, 110, 93, 28))
        self.select_data.setObjectName("select_data")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(310, 150, 521, 361))
        self.tableView.setObjectName("tableView")
        self.drop_db = QtWidgets.QPushButton(self.centralwidget)
        self.drop_db.setGeometry(QtCore.QRect(430, 30, 93, 28))
        self.drop_db.setObjectName("drop_db")
        self.drop_table = QtWidgets.QPushButton(self.centralwidget)
        self.drop_table.setGeometry(QtCore.QRect(430, 70, 93, 28))
        self.drop_table.setObjectName("drop_table")
        self.table_cb = QtWidgets.QComboBox(self.centralwidget)
        self.table_cb.setGeometry(QtCore.QRect(550, 70, 101, 28))
        self.table_cb.setObjectName("table_cb")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 30, 81, 21))
        self.label_4.setObjectName("label_4")
        self.export_table = QtWidgets.QPushButton(self.centralwidget)
        self.export_table.setGeometry(QtCore.QRect(690, 30, 111, 71))
        self.export_table.setObjectName("export_table")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "数据库用户"))
        self.label_2.setText(_translate("MainWindow", "数据库密码"))
        self.login_btn.setText(_translate("MainWindow", "登录"))
        self.remerber_pwd.setText(_translate("MainWindow", "记住密码"))
        self.auto_login.setText(_translate("MainWindow", "自动登录"))
        self.excute_btn.setText(_translate("MainWindow", "执行sql语句"))
        self.label_3.setText(_translate("MainWindow", "选择当前库"))
        self.sql_te.setPlaceholderText(_translate("MainWindow", "请输入sql语句"))
        self.result_te.setPlaceholderText(_translate("MainWindow", "执行结果"))
        self.create_db.setText(_translate("MainWindow", "创建库"))
        self.create_table.setText(_translate("MainWindow", "创建表"))
        self.select_data.setText(_translate("MainWindow", "查询数据"))
        self.drop_db.setText(_translate("MainWindow", "删除库"))
        self.drop_table.setText(_translate("MainWindow", "删除表"))
        self.label_4.setText(_translate("MainWindow", "选择表"))
        self.export_table.setText(_translate("MainWindow", "导出表"))
