# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from myWidget import myWidget
from MyButton import myButton
import source_rc


class BodyForm(object):
    def setupUi(self, BodyForm):
        BodyForm.setObjectName("BodyForm")
        BodyForm.resize(802, 600)
        BodyForm.setMinimumSize(QtCore.QSize(0, 500))

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(BodyForm)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_top = QtWidgets.QHBoxLayout()
        self.horizontalLayout_top.setSpacing(0)
        self.horizontalLayout_top.setObjectName("horizontalLayout_top")

        self.scrollArea = QtWidgets.QScrollArea(BodyForm)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QtCore.QSize(150, 500))
        self.scrollArea.setMaximumSize(QtCore.QSize(200, 16777215))
        # "font: 75 italic 18pt \"Arial\";\n"
        self.scrollArea.setStyleSheet(
"color: rgb(0, 0, 0);\n"
"background: transparent;\n")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # 自定义Widget
        self.scrollAreaWidgetContents = myWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 116, 496))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_top.addWidget(self.scrollArea)

        self.graphicsView = QtWidgets.QGraphicsView(BodyForm)
        self.graphicsView.setMinimumSize(QtCore.QSize(680, 0))
        self.graphicsView.setStyleSheet("border-image: url(:/newPrefix/image/background_one.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_top.addWidget(self.graphicsView)
        self.verticalLayout_2.addLayout(self.horizontalLayout_top)
        self.horizontalLayout_frame = QtWidgets.QHBoxLayout()
        self.horizontalLayout_frame.setObjectName("horizontalLayout_frame")

        # 跳转按钮容器
        self.MainFrame = QtWidgets.QFrame(BodyForm)
        self.MainFrame.setMinimumSize(QtCore.QSize(400, 100))
        self.MainFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.MainFrame.setStyleSheet("font: 75 italic 18pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"background: transparent;")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")


        # 新建、删除按钮容器
        self.ToolFrame = QtWidgets.QFrame(self.MainFrame)
        self.ToolFrame.setMinimumSize(QtCore.QSize(400, 100))
        self.ToolFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.ToolFrame.setStyleSheet("font: 75 italic 18pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"background: transparent;")
        self.ToolFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ToolFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ToolFrame.setObjectName("ToolFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ToolFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # create new file button
        self.NewButton = myButton(self.ToolFrame)
        self.NewButton.setObjectName("NewButton")
        self.horizontalLayout_3.addWidget(self.NewButton)

        # delete chosen file button
        self.DeleteButton = myButton(self.ToolFrame)
        self.DeleteButton.setObjectName("DeleteButton")
        self.horizontalLayout_3.addWidget(self.DeleteButton)
        self.horizontalLayout.addWidget(self.ToolFrame)

        # return main button
        self.MainButton = myButton(self.MainFrame)
        self.MainButton.setObjectName("MainButton")
        self.horizontalLayout.addWidget(self.MainButton)

        # to outline button
        self.OutlineButton = myButton(self.MainFrame)
        self.OutlineButton.setObjectName("OutlineButton")
        self.horizontalLayout.addWidget(self.OutlineButton)

        self.horizontalLayout_frame.addWidget(self.MainFrame)
        self.verticalLayout_2.addLayout(self.horizontalLayout_frame)

        self.retranslateUi(BodyForm)
        QtCore.QMetaObject.connectSlotsByName(BodyForm)

    def retranslateUi(self, BodyForm):
        _translate = QtCore.QCoreApplication.translate
        BodyForm.setWindowTitle(_translate("BodyForm", "BodyForm"))
        self.NewButton.setText(_translate("BodyForm", "新建"))
        self.DeleteButton.setText(_translate("BodyForm", "删除"))
        self.MainButton.setText(_translate("BodyForm", "主页"))
        self.OutlineButton.setText(_translate("BodyForm", "大纲"))