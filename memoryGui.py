# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memoryGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import threading

from PyQt5 import QtCore, QtGui, QtWidgets

from constant import STOPWATCH_TIME

global level
global time


class Ui_Dialog(object):
    level = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 540)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 31))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: rgb(255, 255, 255)")
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 70, 521, 411))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(230, 500, 75, 23))
        self.startButton.setObjectName("startButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        global level
        level = 0
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "기억력 테스트"))
        self.label.setText(_translate("Dialog", "Level " + str(level)))
        self.label_2.setText(_translate("Dialog", str(STOPWATCH_TIME)))
        self.startButton.setText(_translate("Dialog", "시작"))
        self.startButton.clicked.connect(self.startButtonClicked)

    def startButtonClicked(self):
        global level
        level = level + 1

        global time
        time = STOPWATCH_TIME

        self.label.setText("Level " + str(level))

        def stopwatchProcess():
            global time
            time -= 1

            self.label_2.setText(str(time))

            threading.Timer(1, stopwatchProcess).start()

        stopwatchProcess()

    # def stopwatchStart(self):
    #     global time
    #     time = STOPWATCH_TIME
    #     time -= 1
    #     self.label_2.setText(time)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
