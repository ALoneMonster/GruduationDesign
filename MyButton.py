# encoding: utf-8
"""
@author: XLYF
@file: MyButton.py
@time: 2020/11/27 16:33
@desc:
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal


# 自定义按钮
class myButton(QtWidgets.QPushButton):
    # openSingal = pyqtSignal()    # 双击事件信号
    focus_change = pyqtSignal()   # 焦点改变信号

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

    # 鼠标双击事件
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.openSingal.emit()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == 16777220:
            self.click()    # 回车相当于鼠标单击
            # self.mouseDoubleClickEvent(QtGui.QMouseEvent)   # 按钮选中回车相当于发送鼠标双击信号
        elif event.key() == Qt.Key_Up:
            self.focusPreviousChild()   # 焦点移到前一个组件
        elif event.key() == Qt.Key_Down:
            self.focusNextChild()       # 焦点移到下一个组件

    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:      # 得到焦点的背景改变，后期可更改为更好看的
        self.focus_change.emit()
        self.setStyleSheet("background-color: rgb(85, 255, 255)")

    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None:
        self.setStyleSheet("")