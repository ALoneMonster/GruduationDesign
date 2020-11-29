# encoding: utf-8
"""
@author: XLYF
@file: MyButton.py
@time: 2020/11/27 16:33
@desc:
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


# 自定义按钮
class myButton(QtWidgets.QPushButton):
    openSingal = QtCore.pyqtSignal()

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.openSingal.emit()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print("here")
        print(event.key())
        if event.key() == 16777220:
            self.mouseDoubleClickEvent(QtGui.QMouseEvent)   # 按钮选中回车相当于发送鼠标双击信号
        elif event.key() == Qt.Key_Up:
            print("捕获up")
        elif event.key() == Qt.Key_Down:
            print("捕获down")

    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:
        self.setStyleSheet("background-color: rgb(85, 255, 255)")