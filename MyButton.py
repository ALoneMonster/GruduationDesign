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
    double_click = pyqtSignal()   # 双击信号
    focus_change = pyqtSignal()   # 焦点改变信号

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

    # 鼠标双击事件
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.double_click.emit()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == 16777220:
            # self.click()    # 回车相当于鼠标单击
            self.mouseDoubleClickEvent(QtGui.QMouseEvent)    # 发送双击信号
        elif event.key() == Qt.Key_Up:
            self.focusPreviousChild()   # 焦点移到前一个组件
        elif event.key() == Qt.Key_Down:
            self.focusNextChild()       # 焦点移到下一个组件

    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:      # 得到焦点的背景改变，后期可更改为更好看的
        self.focus_change.emit()        # 发送焦点改变信号
        self.setStyleSheet("background-color: rgb(85, 255, 255)")

    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None:
        self.setStyleSheet("")