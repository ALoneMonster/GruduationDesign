# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from MyButton import myButton
from myWidget import myWidget
import source_rc


class MainForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        # Form.setStyleSheet("border-image: url(:/newPrefix/image/background_one.jpg);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 容器
        self.Container = myWidget(Form)
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

        # 小说文件夹尾路径输入框
        self.FileEndPathText = QtWidgets.QLineEdit(self.Container)
        self.FileEndPathText.setObjectName("FileEndPathText")
        self.verticalLayout.addWidget(self.FileEndPathText)
        self.FileEndPathText.setAlignment(QtCore.Qt.AlignCenter)

        # 组件加入水平布局
        self.horizontalLayout.addWidget(self.Container)

        # text初始化
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "StoryTool"))
        self.FileEndPathText.setText(_translate("Form", "修仙"))
        self.BodyButton.setText(_translate("Form", "正文"))
        self.OutlineButton.setText(_translate("Form", "大纲"))
