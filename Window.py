# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(210, 0, 421, 31))
        self.textEdit.setObjectName("textEdit")
        self.shipinzhanshi = QtWidgets.QTableView(self.centralwidget)
        self.shipinzhanshi.setGeometry(QtCore.QRect(90, 90, 611, 321))
        self.shipinzhanshi.setObjectName("shipinzhanshi")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(130, 60, 75, 24))
        self.open.setObjectName("open")
        self.yundongxuanze = QtWidgets.QComboBox(self.centralwidget)
        self.yundongxuanze.setGeometry(QtCore.QRect(230, 60, 201, 21))
        self.yundongxuanze.setObjectName("yundongxuanze")
        self.yundongxuanze.addItem("")
        self.yundongxuanze.addItem("")
        self.jishu_2 = QtWidgets.QPushButton(self.centralwidget)
        self.jishu_2.setGeometry(QtCore.QRect(480, 60, 75, 24))
        self.jishu_2.setObjectName("jishu_2")
        self.jishu = QtWidgets.QTextEdit(self.centralwidget)
        self.jishu.setGeometry(QtCore.QRect(210, 460, 71, 41))
        self.jishu.setObjectName("jishu")
        self.zongji = QtWidgets.QLabel(self.centralwidget)
        self.zongji.setGeometry(QtCore.QRect(140, 460, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zongji.setFont(font)
        self.zongji.setObjectName("zongji")
        self.jiazaishipin = QtWidgets.QProgressBar(self.centralwidget)
        self.jiazaishipin.setGeometry(QtCore.QRect(100, 420, 601, 21))
        self.jiazaishipin.setProperty("value", 24)
        self.jiazaishipin.setObjectName("jiazaishipin")
        self.hege_num = QtWidgets.QLabel(self.centralwidget)
        self.hege_num.setGeometry(QtCore.QRect(320, 470, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hege_num.setFont(font)
        self.hege_num.setObjectName("hege_num")
        self.hegeshu = QtWidgets.QTextEdit(self.centralwidget)
        self.hegeshu.setGeometry(QtCore.QRect(410, 460, 71, 41))
        self.hegeshu.setObjectName("hegeshu")
        self.buhege_num = QtWidgets.QLabel(self.centralwidget)
        self.buhege_num.setGeometry(QtCore.QRect(500, 470, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buhege_num.setFont(font)
        self.buhege_num.setObjectName("buhege_num")
        self.buhegeshu = QtWidgets.QTextEdit(self.centralwidget)
        self.buhegeshu.setGeometry(QtCore.QRect(580, 460, 71, 41))
        self.buhegeshu.setObjectName("buhegeshu")
        self.zongfen_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.zongfen_2.setGeometry(QtCore.QRect(310, 510, 181, 41))
        self.zongfen_2.setObjectName("zongfen_2")
        self.zongfennum = QtWidgets.QLabel(self.centralwidget)
        self.zongfennum.setGeometry(QtCore.QRect(230, 510, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zongfennum.setFont(font)
        self.zongfennum.setObjectName("zongfennum")
        self.baocun = QtWidgets.QPushButton(self.centralwidget)
        self.baocun.setGeometry(QtCore.QRect(590, 60, 75, 24))
        self.baocun.setObjectName("baocun")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">运动姿态识别</span></p></body></html>"))
        self.open.setText(_translate("MainWindow", "打开"))
        self.yundongxuanze.setItemText(0, _translate("MainWindow", "仰卧起坐"))
        self.yundongxuanze.setItemText(1, _translate("MainWindow", "引体向上"))
        self.jishu_2.setText(_translate("MainWindow", "计数"))
        self.zongji.setText(_translate("MainWindow", "总计："))
        self.hege_num.setText(_translate("MainWindow", "合格数量："))
        self.buhege_num.setText(_translate("MainWindow", "不合格数量："))
        self.zongfennum.setText(_translate("MainWindow", "总分："))
        self.baocun.setText(_translate("MainWindow", "保存"))

import sys
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_Window() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程

