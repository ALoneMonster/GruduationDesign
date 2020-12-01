# encoding: utf-8
"""
@author: XLYF
@file: Controller.py
@time: 2020/11/17 14:16
@desc:
"""
from AllWindow import *
from funLibrary import windowstate


class Controller:
    state = {
        0: lambda x: x.showNormal(),
        1: lambda x: x.showMinimized(),
        2: lambda x: x.showMaximized(),
        3: lambda x: x.showFullscreen()
    }

    state_number = 0

    def __init__(self):
        self.STORY_ROOT_PATH = "D:/document/story/testroot"
        self.STORY_MAIN_PATH = self.STORY_ROOT_PATH

    def show_main(self):
        self.mainw = MainWindow()
        self.mainw.main_to_Body.connect(self.mto_body)
        self.mainw.main_to_outline.connect(self.mto_outline)
        self.state[self.state_number](self.mainw)

    def show_body(self, chosenPath):
        self.bodyw = BodyWindow(chosenPath)
        self.bodyw.body_to_main.connect(self.bto_main)
        self.bodyw.body_to_outline.connect(self.bto_outline)
        self.state[self.state_number](self.bodyw)

    def show_outline(self, chosenPath):
        self.outlinew = OutlineWindow(chosenPath)
        self.outlinew.outline_to_main.connect(self.oto_main)
        self.outlinew.outline_to_body.connect(self.oto_body)
        self.state[self.state_number](self.outlinew)

    # main switch
    def mto_body(self):
        if self.mainw.FileEndPathText.text() != "":     # 判断尾路径是否为空
            self.STORY_MAIN_PATH = self.STORY_ROOT_PATH+"/"+self.mainw.FileEndPathText.text()
            self.state_number = windowstate(self.mainw)
            self.mainw.close()
            self.show_body(self.STORY_MAIN_PATH)

    def mto_outline(self):
        if self.mainw.FileEndPathText.text() != "":     # 判断尾路径是否为空
            self.STORY_MAIN_PATH = self.STORY_ROOT_PATH + "/" + self.mainw.FileEndPathText.text()
            self.state_number = windowstate(self.mainw)
            self.mainw.close()
            self.show_outline(self.STORY_MAIN_PATH)

    # body switch
    def bto_main(self):
        self.state_number = windowstate(self.bodyw)
        self.bodyw.close()
        self.show_main()

    def bto_outline(self):
        self.state_number = windowstate(self.bodyw)
        self.bodyw.close()
        self.show_outline(self.STORY_MAIN_PATH)

    # outline switch
    def oto_main(self):
        self.state_number = windowstate(self.outlinew)
        self.outlinew.close()
        self.show_main()

    def oto_body(self):
        self.state_number = windowstate(self.outlinew)
        self.outlinew.close()
        self.show_body(self.STORY_MAIN_PATH)