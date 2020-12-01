# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from MyButton import myButton
from myWidget import myWidget
import source_rc


# 主页窗口类
class MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainForm.sizePolicy().hasHeightForWidth())
        MainForm.setSizePolicy(sizePolicy)
        MainForm.setMinimumSize(QtCore.QSize(800, 600))
        # 总布局
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainForm)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 各组件的容器
        self.Container = myWidget(MainForm)
        self.Container.setMinimumSize(QtCore.QSize(800, 600))
        self.Container.setStyleSheet("border-image: url(:/newPrefix/image/background_one.jpg);\n"
"font: 75 italic 20pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.Container.setObjectName("Container")

        # 垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Container)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # to body window
        self.BodyButton = myButton(self.Container)
        self.BodyButton.setObjectName("BodyButton")
        self.verticalLayout.addWidget(self.BodyButton)

        # to outline window
        self.OutlineButton = myButton(self.Container)
        self.OutlineButton.setObjectName("OutlineButton")
        self.verticalLayout.addWidget(self.OutlineButton)

        # 单行输入框——小说文件夹尾路径
        self.FileEndPathText = QtWidgets.QLineEdit(self.Container)
        self.FileEndPathText.setObjectName("FileEndPathText")
        self.verticalLayout.addWidget(self.FileEndPathText)
        self.FileEndPathText.setAlignment(QtCore.Qt.AlignCenter)

        # 组件加入水平布局
        self.horizontalLayout.addWidget(self.Container)

        # text初始化
        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    # 窗体text初始化
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainForm", "StoryTool"))
        self.FileEndPathText.setText(_translate("MainForm", "修仙"))
        self.BodyButton.setText(_translate("MainForm", "正文"))
        self.OutlineButton.setText(_translate("MainForm", "大纲"))
