# encoding: utf-8
"""
@author: XLYF
@file: main.py
@time: 2020/11/12 15:11
@desc:
"""

from Controller import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
import time


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Controller()
    window.show_main()
    sys.exit(app.exec_())