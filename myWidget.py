# encoding: utf-8
"""
@author: XLYF
@file: myWidget.py
@time: 2020/11/27 17:28
@desc:
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QStyleOption, QStyle
from PyQt5.QtGui import QPainter


# 自定义widget
class myWidget(QWidget):

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        print("here")
        print(event.key())
        if event.key() == 16777220:
            self.mouseDoubleClickEvent(QtGui.QMouseEvent)  # 按钮选中回车相当于发送鼠标双击信号
        elif event.key() == Qt.Key_Up:
            print("捕获up")
        elif event.key() == Qt.Key_Down:
            print("捕获down")

    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:
        print("得到焦点")

    # 重写此方法，否则样式表多重传值后会失效
    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        # 避免在多重传值后功能失效
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)