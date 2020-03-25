import sqlgui
import numpy as np
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import MySQLdb

class Mysql:
    url = 'localhost'
    user = ''
    password = ''
    charset = 'gbk'

    def __init__(self):
        self.conn = MySQLdb.connect(self.url, self.user, self.password,charset=self.charset)
        self.cursor = self.conn.cursor()

    def sql(self,query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            gui.ui.result_te.setText('操作成功!')
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            gui.ui.result_te.setText('操作失败!\n%s'%e)

class Gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = sqlgui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_login_info()
        self.auto_login_info()

    def init_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        the_account = settings.value("db_acc")
        the_password = settings.value("db_pwd")
        the_remeberpassword = settings.value("remeberpassword")

        self.ui.acc_le.setText(the_account)
        if the_remeberpassword == "true" or the_remeberpassword == True:
            self.ui.remerber_pwd.setChecked(True)
            self.ui.pwd_le.setText(the_password)

    def auto_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        auto_login_data = settings.value("auto_login")
        if auto_login_data == "true" or auto_login_data == True:
            try:
                self.ui.auto_login.setChecked(True)
                self.login_db()
            except Exception as e:
                print(e)

    def login_db(self):
        self.ui.db_cb.clear()
        try:
            Mysql.user = self.ui.acc_le.text()
            Mysql.password = self.ui.pwd_le.text()
            mysql = Mysql()
            mysql.cursor.execute('show databases')
            db = mysql.cursor.fetchall()

            #添加数据库名到comboBox
            db = np.array(db).tolist()
            db_list = []
            for i in range(len(db)):
                db_list.append(db[i][0])
            self.ui.db_cb.addItems(db_list)

            db_name = self.ui.db_cb.currentText()
            mysql.cursor.execute('use %s'%db_name)
            #添加所有表显示到QComboBox
            mysql.cursor.execute('show tables')
            table = mysql.cursor.fetchall()
            table = np.array(table).tolist()
            table_list = []
            for i in range(len(table)):
                table_list.append(table[i][0])
            self.ui.table_cb.addItems(table_list)

        except Exception as e:
            QMessageBox.information(None,'数据库提示','%s'%e)


def save_info():
    #用QSettings存储账号密码
    try:
        if gui.ui.remerber_pwd.isChecked():
            settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件
            settings.setValue("db_acc", gui.ui.acc_le.text())
            settings.setValue("db_pwd", gui.ui.pwd_le.text())
            settings.setValue("remeberpassword", gui.ui.remerber_pwd.isChecked())
    except Exception as e:
        QMessageBox.information(None, '提示', '%s' %e)
        
#自动登录QCheckBox触发
def auto_login_connect():
    try:
        if gui.ui.auto_login.isChecked():
            settings = QSettings("config.ini", QSettings.IniFormat)  # 使用配置文件
            settings.setValue("auto_login", gui.ui.remerber_pwd.isChecked())
    except Exception as e:
        QMessageBox.information(None, '提示', '%s' % e)

#添加所有表显示到QComboBox
def table_change():
    try:
        gui.ui.table_cb.clear()
        mysql = Mysql()
        mysql.cursor.execute('use '+gui.ui.db_cb.currentText()+'')
        mysql.cursor.execute('show tables')
        table = mysql.cursor.fetchall()
        table = np.array(table).tolist()
        table_list = []
        for i in range(len(table)):
            table_list.append(table[i][0])
        gui.ui.table_cb.addItems(table_list)
    except Exception as e:
        QMessageBox.information(None,'数据库提示','%s'%e)

#提交QTextEdit输入的sql语句
def excute_sql():
    gui.ui.result_te.setText('')
    try:
        mysql = Mysql()
        mysql.cursor.execute('use %s'%gui.ui.db_cb.currentText())
        exc_sql = gui.ui.sql_te.toPlainText()
        mysql.sql(exc_sql)
    except Exception as e:
        QMessageBox.information(None, '提示', '%s' % e)

#查询数据
def select_table():
    try:
        mysql = Mysql()
        #使用QComboBox的当前数据库
        mysql.cursor.execute('use ' + gui.ui.db_cb.currentText() + '')
        db_text = gui.ui.table_cb.currentText()
        columns = mysql.sql('desc %s'%db_text)
        columns = np.array(columns).tolist()
        table_columns_name = []
        for i in range(len(columns)):
            table_columns_name.append(columns[i][0])
        table_rows = mysql.sql('select count(*) from %s'%db_text)

        #把行列填入Qtableview
        model = QStandardItemModel(table_rows[0][0],len(table_columns_name))
        model.setHorizontalHeaderLabels(table_columns_name)
        #写入数据
        result_data = mysql.sql('select * from %s' % db_text)
        for row in range(int(table_rows[0][0])):
            for column in range(len(table_columns_name)):
                item = QStandardItem(result_data[row][column])
                # 设置每个位置的文本值
                model.setItem(row, column, item)
        gui.ui.tableView.setModel(model)
    except Exception as e:
        QMessageBox.information(None, '提示', '%s' % e)

def create_database():
    try:
        #创建QInputDialog
        db_text, db_action = QtWidgets.QInputDialog.getText(None, '创建数据库', '请输入数据库名', QtWidgets.QLineEdit.Normal)
        #判断输入文本与动作
        if (db_text.replace(' ', '') != '') and (db_action is True):
            mysql = Mysql()
            mysql.sql('create database %s'%db_text)
    except Exception as e:
        QMessageBox.information(None, '提示', '%s' % e)

def create_table():
    try:
        db_text, db_action = QtWidgets.QInputDialog.getText(None, '创建表', '请输入完整sql语句', QtWidgets.QLineEdit.Normal)
        if (db_text.replace(' ', '') != '') and (db_action is True):
            mysql = Mysql()
            mysql.cursor.execute('use ' + gui.ui.db_cb.currentText() + '')
            mysql.sql(db_text)
    except Exception as e:
        QMessageBox.information(None, '提示', '%s'%e)
        
def drop_database():
    try:
        db_text, db_action = QtWidgets.QInputDialog.getText(None, '删除数据库', '请输入数据库名', QtWidgets.QLineEdit.Normal)
        if (db_text.replace(' ', '') != '') and (db_action is True):
            mysql = Mysql()
            mysql.sql('drop database %s'%db_text)
    except Exception as e:
        QMessageBox.information(None, '提示', '%s'%e)
        
def drop_table():
    try:
        db_text, db_action = QtWidgets.QInputDialog.getText(None, '删除表', '请输入表名', QtWidgets.QLineEdit.Normal)
        if (db_text.replace(' ', '') != '') and (db_action is True):
            mysql = Mysql()
            mysql.cursor.execute('use ' + gui.ui.db_cb.currentText() + '')
            mysql.sql('drop table %s'%db_text)
    except Exception as e:
        QMessageBox.information(None, '提示', '%s'%e)

def export_table():
    try:
        export_path = QtWidgets.QFileDialog.getSaveFileName(None, 'export table', 'D:\\', 'Excel files (*.xlsx)')
        print(export_path[0])
        mysql = Mysql()
        mysql.cursor.execute('use ' + gui.ui.db_cb.currentText() + '')
        mysql.sql("select * from %s into outfile '%s'"%(gui.ui.table_cb.currentText(),export_path[0]))
    except Exception as e:
        QMessageBox.information(None, '提示', '%s'%e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    #按钮点击
    gui.ui.login_btn.clicked.connect(gui.login_db)
    gui.ui.excute_btn.clicked.connect(excute_sql)
    gui.ui.create_db.clicked.connect(create_database)
    gui.ui.create_table.clicked.connect(create_table)
    gui.ui.drop_db.clicked.connect(drop_database)
    gui.ui.drop_table.clicked.connect(drop_table)
    gui.ui.select_data.clicked.connect(select_table)
    gui.ui.export_table.clicked.connect(export_table)
    # QComboBox状态触发
    gui.ui.db_cb.activated.connect(table_change)
    # QCheckBox状态触发
    gui.ui.remerber_pwd.stateChanged.connect(save_info)
    gui.ui.auto_login.stateChanged.connect(auto_login_connect)

    sys.exit(app.exec_())