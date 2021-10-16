# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memoryGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import functools
import os
import random
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QEvent
from PyQt5.QtGui import QColor, QPen, QPainter, QPixmap, QIcon
from PyQt5.QtWidgets import QLabel

from constant import *

global level
global time


class Ui_Dialog(object):
    level = 0

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, WINDOW_WIDTH, LEVEL_LABEL_HEIGHT))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background: rgb(255, 255, 255)")
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("level_label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, WINDOW_WIDTH, TIME_LABEL_HEIGHT))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("time_label")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(GRID_MARGIN, 70, GRID_WIDTH, GRID_HEIGHT))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayoutWidget.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget.setObjectName("gridLayout")
        self.gridLayoutWidget.setRowStretch(4, 4)
        self.gridLayoutWidget.setRowMinimumHeight(0, IMAGE_TILE_HEIGHT)
        self.gridLayoutWidget.setRowMinimumHeight(1, IMAGE_TILE_HEIGHT)
        self.gridLayoutWidget.setRowMinimumHeight(2, IMAGE_TILE_HEIGHT)
        self.gridLayoutWidget.setRowMinimumHeight(3, IMAGE_TILE_HEIGHT)
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(START_BUTTON_X, START_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.startButton.setObjectName("startButton")
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background: rgb(255, 255, 255)")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        global level
        level = 0
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "기억력 테스트"))
        Dialog.setWindowIcon(QIcon(ICON_PATH + ICON_NAME))
        self.label.setText(_translate("Dialog", "Level " + str(level)))
        self.label_2.setText(_translate("Dialog", str(STOPWATCH_TIME)))
        self.drawImageTile()
        self.startButton.setText(_translate("Dialog", "Game Start"))
        self.startButton.clicked.connect(self.startButtonClicked)

    def drawImageTile(self):
        # for i in range(IMAGE_TILE_COUNT):
        #     image_label = QtWidgets.QLabel(self)
        #     image_label.setObjectName("image_label_{}".format(i))
        #     image_label.setAlignment(Qt.AlignCenter)
        #     image_label.setStyleSheet("background: rgb(245, 236, 235)")
        image_label_1 = QtWidgets.QLabel(Dialog)
        image_label_1.setObjectName("image_label_1")
        image_label_1.setAlignment(Qt.AlignCenter)
        image_label_1.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_1, 0, 0)

        image_label_2 = QtWidgets.QLabel(Dialog)
        image_label_2.setObjectName("image_label_2")
        image_label_2.setAlignment(Qt.AlignCenter)
        image_label_2.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_2, 0, 1)

        image_label_3 = QtWidgets.QLabel(Dialog)
        image_label_3.setObjectName("image_label_3")
        image_label_3.setAlignment(Qt.AlignCenter)
        image_label_3.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_3, 0, 2)

        image_label_4 = QtWidgets.QLabel(Dialog)
        image_label_4.setObjectName("image_label_4")
        image_label_4.setAlignment(Qt.AlignCenter)
        image_label_4.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_4, 0, 3)

        image_label_5 = QtWidgets.QLabel(Dialog)
        image_label_5.setObjectName("image_label_5")
        image_label_5.setAlignment(Qt.AlignCenter)
        image_label_5.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_5, 1, 0)

        image_label_6 = QtWidgets.QLabel(Dialog)
        image_label_6.setObjectName("image_label_6")
        image_label_6.setAlignment(Qt.AlignCenter)
        image_label_6.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_6, 1, 1)

        image_label_7 = QtWidgets.QLabel(Dialog)
        image_label_7.setObjectName("image_label_7")
        image_label_7.setAlignment(Qt.AlignCenter)
        image_label_7.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_7, 1, 2)

        image_label_8 = QtWidgets.QLabel(Dialog)
        image_label_8.setObjectName("image_label_8")
        image_label_8.setAlignment(Qt.AlignCenter)
        image_label_8.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_8, 1, 3)

        image_label_9 = QtWidgets.QLabel(Dialog)
        image_label_9.setObjectName("image_label_9")
        image_label_9.setAlignment(Qt.AlignCenter)
        image_label_9.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_9, 2, 0)

        image_label_10 = QtWidgets.QLabel(Dialog)
        image_label_10.setObjectName("image_label_10")
        image_label_10.setAlignment(Qt.AlignCenter)
        image_label_10.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_10, 2, 1)

        image_label_11 = QtWidgets.QLabel(Dialog)
        image_label_11.setObjectName("image_label_11")
        image_label_11.setAlignment(Qt.AlignCenter)
        image_label_11.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_11, 2, 2)

        image_label_12 = QtWidgets.QLabel(Dialog)
        image_label_12.setObjectName("image_label_12")
        image_label_12.setAlignment(Qt.AlignCenter)
        image_label_12.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_12, 2, 3)

        image_label_13 = QtWidgets.QLabel(Dialog)
        image_label_13.setObjectName("image_label_13")
        image_label_13.setAlignment(Qt.AlignCenter)
        image_label_13.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_13, 3, 0)

        image_label_14 = QtWidgets.QLabel(Dialog)
        image_label_14.setObjectName("image_label_14")
        image_label_14.setAlignment(Qt.AlignCenter)
        image_label_14.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_14, 3, 1)

        image_label_15 = QtWidgets.QLabel(Dialog)
        image_label_15.setObjectName("image_label_15")
        image_label_15.setAlignment(Qt.AlignCenter)
        image_label_15.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_15, 3, 2)

        image_label_16 = QtWidgets.QLabel(Dialog)
        image_label_16.setObjectName("image_label_16")
        image_label_16.setAlignment(Qt.AlignCenter)
        image_label_16.setStyleSheet("background: rgb(245, 236, 235)")
        self.gridLayoutWidget.addWidget(image_label_16, 3, 3)

        image_label_1.mouseReleaseEvent = functools.partial(self.imageClickEvent, source_object=image_label_1)

    def imageClickEvent(self, event, source_object=None):
        if event.button() == QtCore.Qt.LeftButton:
            print(source_object.objectName())

    def startButtonClicked(self):
        # Level Setting
        global level
        level = level + 1

        # Time Setting
        global time
        time = STOPWATCH_TIME

        self.label.setText("Level " + str(level))
        self.startButton.setEnabled(False)
        self.setGameBoard()

        def hintProcess():
            self.label_2.setText(str(HINT_TIME))
            schedule = threading.Timer(1, stopwatchProcess)
            schedule.start()

        def stopwatchProcess():
            global time

            self.label_2.setText(str(time))

            schedule = threading.Timer(1, stopwatchProcess)
            schedule.start()

            if time == 0:
                self.startButton.setEnabled(True)
                schedule.cancel()

            time -= 1

        stopwatchProcess()

    def setGameBoard(self):
        global level
        image_list = getImageList()
        mixed_image_list = randomMixImageName(image_list, level)
        self.changeImageLabel(mixed_image_list)

    def changeImageLabel(self, mixed_image_list):
        tile_number_list = []
        for i in range(IMAGE_TILE_COUNT):
            tile_number_list.append(str(i + 1))
        random.shuffle(tile_number_list)

        for image_index in range(len(mixed_image_list)):
            label_name = "image_label_" + tile_number_list.__getitem__(image_index)

            # label_object = self.gridLayoutWidget.findChild(QLabel, label_name)
            # print(label_object)
            pixmap = QPixmap(IMAGE_PATH + mixed_image_list.__getitem__(image_index))
            self.gridLayoutWidget.widget[label_name].setPixmap(pixmap)
            # print(IMAGE_PATH + mixed_image_list.__getitem__(image_index))
            # label_object.setPixmap(pixmap)

    def mouseReleaseEvent(self, event):  # event : QMouseEvent
        if event.button() == Qt.LeftButton:
            print('click')


# General Method.
def getImageList():
    print('image load start ...')
    imageList = os.listdir(IMAGE_PATH)
    return imageList


def randomMixImageName(image_list, level):
    mixed_image_list = []
    # 짝 맞추기 게임을 위해 2개씩 생성
    for i in range(level + 1):
        item_name = image_list.__getitem__(i)
        mixed_image_list.append(item_name)
        mixed_image_list.append(item_name)

    random.shuffle(mixed_image_list)
    return mixed_image_list


def clickable(widget):
    class Filter(QObject):

        clicked = pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True

            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
