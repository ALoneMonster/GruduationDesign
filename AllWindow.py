# encoding: utf-8
"""
@author: XLYF
@file: AllWindow.py
@time: 2020/11/17 13:43
@desc:
"""

from ui.Main import *
from ui.Body import BodyForm
from ui.Outline import OutlineForm
from functools import partial
from functools import cmp_to_key
from funLibrary import *
from MyButton import myButton
import time
from threading import Thread

class MainWindow(QtWidgets.QWidget, MainForm):
    main_to_Body = QtCore.pyqtSignal()
    main_to_outline = QtCore.pyqtSignal()
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.BodyButton.clicked.connect(self.goBody)
        # self.OutlineButton.clicked.connect(self.goOutline)
        self.BodyButton.openSingal.connect(self.goBody)
        self.OutlineButton.openSingal.connect(self.goOutline)
        # 窗口尺寸变化快捷键
        self.window_shc = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_R), self.FileEndPathText)
        self.window_shc.setContext(QtCore.Qt.ApplicationShortcut)
        self.window_shc.activated.connect(self.window_size_change)

    # 窗口尺寸变化方法
    def window_size_change(self):
        change = {
            0: lambda x: x.showMaximized(),
            2: lambda x: x.showFullScreen(),
            3: lambda x: x.showNormal()
        }
        change[windowstate(self)](self)

    def goBody(self):
        self.main_to_Body.emit()

    def goOutline(self):
        self.main_to_outline.emit()


class BodyWindow(QtWidgets.QWidget, BodyForm):
    # 信号
    body_to_main = QtCore.pyqtSignal()
    body_to_outline = QtCore.pyqtSignal()

    _translate = QtCore.QCoreApplication.translate

    # 内部参数
    chosen_dir = ""
    before_dir = ""
    fname_number = -1
    name_end_number = 0
    clickedPath = ""

    def __init__(self, chosenPath):
        super(BodyWindow, self).__init__()
        # 保证路径存在
        story_exist(chosenPath)
        # 初始化
        self.chosen_dir = chosenPath
        self.before_dir = self.chosen_dir
        self.setupUi(self)
        self.MainButton.clicked.connect(self.goMain)
        self.OutlineButton.clicked.connect(self.goOutline)
        self.NewButton.clicked.connect(self.new)
        self.DeleteButton.clicked.connect(self.delete)
        # 载入目录
        self.reload(self.chosen_dir)
        # 窗口尺寸变化快捷键
        self.window_shc = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_R), self.scrollArea)
        self.window_shc.setContext(QtCore.Qt.ApplicationShortcut)
        self.window_shc.activated.connect(self.window_size_change)

    # 窗口尺寸变化方法
    def window_size_change(self):
        change = {
            0: lambda x: x.showMaximized(),
            2: lambda x: x.showFullScreen(),
            3: lambda x: x.showNormal()
        }
        change[windowstate(self)](self)

    # 前往主页面信号发送
    def goMain(self):
        self.body_to_main.emit()

    # 前往大纲界面信号发送
    def goOutline(self):
        self.body_to_outline.emit()

    # 资源管理界面新建文件
    def new(self):
        self.newfile_nameedit = QtWidgets.QLineEdit()
        self.newfile_nameedit.setObjectName("NewFileNameEdit")
        self.verticalLayout.addWidget(self.newfile_nameedit)
        self.newfile_nameedit.setText(self._translate("BodyForm", "新文件名"))
        self.newfile_nameedit.selectAll()
        self.newfile_nameedit.setFocus()
        self.newfile_nameedit.returnPressed.connect(self.create_file)

    # 回车创建文件并载入,判断文件类型
    # 创建文件时使用open，不能使用os.mknod()，因为window没有节点的概念，Linux可以使用mknod()
    def create_file(self):
        print("绑定成功")
        new_file_name = self.newfile_nameedit.text()
        if new_file_name == "新文件名":
            pass
        else:
            new_file_path = self.chosen_dir+"/"+new_file_name
            if not os.path.exists(new_file_path):
                if is_volumes(new_file_name):
                    os.mkdir(new_file_path)
                    self.reload(self.chosen_dir)
                else:
                    new_file_path = new_file_path+".docx"
                    open(new_file_path, "w+")
                    fname = "file" + str(self.name_end_number)
                    setattr(self, fname, myButton())
                    exec("self." + fname + ".setObjectName(new_file_name)")
                    exec("self.verticalLayout.addWidget(self." + fname + ")")
                    exec("self." + fname + ".setText(self._translate(\"BodyForm\", new_file_name))")
                    exec("self." + fname + ".clicked.connect(partial(self.whichClicked, new_file_path))")
                    exec("self." + fname + ".clicked.connect(partial(self.checkedChange, self.name_end_number))")
                    exec("self." + fname + ".openSingal.connect(partial(self.open, new_file_path))")
                    self.name_end_number += 1
        self.newfile_nameedit.deleteLater()


    # 正文open方法，与outline类有所差异
    def open(self, fpath):
        if os.path.isdir(fpath):
            if fpath != self.before_dir:
                self.before_dir = self.chosen_dir
            self.chosen_dir = fpath
            self.reload(fpath)
        else:
            os.startfile(fpath)

    # 得到选中路径
    def whichClicked(self, fpath):
        self.clickedPath = fpath

    # 不删除文件夹
    def delete(self):
        if self.clickedPath != "" and not os.path.isdir(self.clickedPath):
            os.remove(self.clickedPath)
            self.clickedPath = ""
            exec("self.file"+str(self.fname_number)+".deleteLater()")
            self.fname_number = -1

    # 充值关键参数
    def reset(self):
        self.fname_number = -1
        self.name_end_number = 0
        self.clickedPath = ""

    # 载入目录下文件并显示绑定点击方法
    def reload(self, dpath):
        # 删除原按钮
        for i in range(self.name_end_number):
            exec("self.file" + str(i) + ".deleteLater()")
        self.reset()
        # 读取文件名称
        fdir = os.listdir(dpath)
        fpath = []
        # 正文文件夹处理， 并确保角色、剧情、杂项文件夹存在
        for i in ["角色", "剧情", "杂项"]:
            try:
                fdir.remove(i)
            except Exception as e:
                last_path =self.chosen_dir.split("/")[-1]
                if not is_volumes(last_path):       # 避免在分卷文件夹中创建角色、剧情、杂项文件夹
                    os.mkdir(dpath+"/"+i)
        # 名称排序
        if len(fdir) > 1:
            fdir = sorted(fdir, key=cmp_to_key(story_cmp))
        # 创建路径对映字典
        for f in fdir:
            f = self.chosen_dir + "/" + f
            fpath.append(f)
        fdir = list(map(clear_suffix, fdir))
        fileDict = dict(zip(fdir, fpath))
        # 添加返回上级按钮
        if self.chosen_dir != self.before_dir:
            fdir.insert(0, "上一级")
            fileDict["上一级"] = self.before_dir
        # 添加对应按钮
        for f in fdir:
            fname = "file" + str(self.name_end_number)
            setattr(self, fname, myButton())
            exec("self." + fname + ".setObjectName(f)")
            exec("self.verticalLayout.addWidget(self." + fname + ")")
            exec("self." + fname + ".setText(self._translate(\"BodyForm\", f))")
            exec("self." + fname + ".clicked.connect(partial(self.whichClicked, fileDict[f]))")
            exec("self." + fname + ".clicked.connect(partial(self.checkedChange, self.name_end_number))")
            exec("self." + fname + ".openSingal.connect(partial(self.open, fileDict[f]))")
            self.name_end_number += 1

    # 选中后效果， 预修改
    def checkedChange(self, name):
        if self.fname_number != -1:
            exec("self.file"+str(self.fname_number)+".setStyleSheet(\"background: transparent\")")
        exec("self.file"+str(name)+".setStyleSheet(\"background-color: rgb(85, 255, 255)\")")
        self.fname_number = name


class OutlineWindow(QtWidgets.QWidget, OutlineForm):
    # 信号
    outline_to_main = QtCore.pyqtSignal()
    outline_to_body = QtCore.pyqtSignal()
    # 内部参数
    chosen_dir = ""
    before_dir = ""
    fname_number = -1
    name_end_number = 0
    clickedPath = ""
    # 自动保存线程
    autosave_thread = Thread()
    auto_wait_flag = True   # 线程等待标志位
    # 翻译函数
    _translate = QtCore.QCoreApplication.translate

    def __init__(self, chosenPath):
        super(OutlineWindow, self).__init__()
        # 保证路径存在
        story_exist(chosenPath)
        self.chosen_dir = chosenPath
        self.before_dir = self.chosen_dir
        self.setupUi(self)
        self.MainButton.clicked.connect(self.goMain)
        self.BodyButton.clicked.connect(self.goBody)
        self.NewBUtton.clicked.connect(self.new)
        self.DeleteButton.clicked.connect(self.delete)
        self.SaveButton.clicked.connect(self.save)
        self.SaveButton.setEnabled(False)       # 禁用保存按钮，避免误存
        # 设置快捷键
        # 保存快捷键
        self.shc = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL+QtCore.Qt.Key_S), self.InputArea)
        self.shc.setContext(QtCore.Qt.WidgetShortcut)
        self.shc.activated.connect(self.save)
        # 窗口尺寸变化快捷键
        self.window_shc = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL+QtCore.Qt.Key_R), self.InputArea)
        self.window_shc.setContext(QtCore.Qt.ApplicationShortcut)
        self.window_shc.activated.connect(self.window_size_change)
        # 自动保存线程初始化并启动
        self.autosave_thread = Thread(target=self.auto_save, name="AutoSaveThread", daemon=True)
        self.autosave_thread.start()
        # 载入目录
        self.reload(self.chosen_dir)

    # 窗口尺寸变化方法
    def window_size_change(self):
        change = {
            0: lambda x: x.showMaximized(),
            2: lambda x: x.showFullScreen(),
            3: lambda x: x.showNormal()
        }
        change[windowstate(self)](self)

    # 前往主页面信号发送
    def goMain(self):
        self.outline_to_main.emit()

    # 前往正文页面信号发送
    def goBody(self):
        self.outline_to_body.emit()

    # outline新建文件方法， 通过QlineEdit组件
    def new(self):
        self.newfile_nameedit = QtWidgets.QLineEdit()
        self.newfile_nameedit.setObjectName("NewFileNameEdit")
        self.verticalLayout.addWidget(self.newfile_nameedit)
        self.newfile_nameedit.setText(self._translate("BodyForm", "新文件名"))
        self.newfile_nameedit.selectAll()
        self.newfile_nameedit.setFocus()
        self.newfile_nameedit.returnPressed.connect(self.create_file)

    # 回车创建文件并载入,判断文件类型
    # 创建文件时使用open，不能使用os.mknod()，因为window没有节点的概念，Linux可以使用mknod()
    def create_file(self):
        print(self.chosen_dir)
        print("绑定成功")
        new_file_name = self.newfile_nameedit.text()
        if new_file_name == "新文件名":
            pass
        else:
            new_file_path = self.chosen_dir + "/" + new_file_name
            if not os.path.exists(new_file_path):
                # 是角色分卷文件夹
                if not is_role(new_file_name):
                    os.mkdir(new_file_path)
                    self.reload(self.chosen_dir)
                # 是角色文件txt
                else:
                    new_file_path = new_file_path + ".txt"
                    print(new_file_path)
                    open(new_file_path, "w+")
                    fname = "file" + str(self.name_end_number)
                    setattr(self, fname, myButton())
                    exec("self." + fname + ".setObjectName(new_file_name)")
                    exec("self.verticalLayout.addWidget(self." + fname + ")")
                    exec("self." + fname + ".setText(self._translate(\"BodyForm\", new_file_name))")
                    exec("self." + fname + ".clicked.connect(partial(self.whichClicked, new_file_path))")
                    exec("self." + fname + ".clicked.connect(partial(self.checkedChange, self.name_end_number))")
                    exec("self." + fname + ".openSingal.connect(partial(self.open, new_file_path))")
                    # exec ("self." + fname + ".setFocusPolicy(QtCore.Qt.StrongFocus)")
                    self.name_end_number += 1
        self.newfile_nameedit.deleteLater()

    # 正常保存内容至self.clickpath
    def save(self):
        if self.clickedPath != "":
            contents = self.InputArea.toPlainText()
            try:
                with open(self.clickedPath, "w") as f:
                    f.write(contents)
            except Exception as e:
                print(e)

    # 定时将文本域内容保存至指定路径文件中,保存间隔为一分钟
    def auto_save(self):
        while True:
            if self.auto_wait_flag == True:
                continue
            else:
                time.sleep(60)
                if self.auto_wait_flag != True:
                    self.save()

    # outline类open方法
    def open(self, fpath):
        # 打开文件夹
        if os.path.isdir(fpath):
            if fpath != self.before_dir:
                self.before_dir = self.chosen_dir
            self.chosen_dir = fpath
            self.reload(fpath)
        else:
            # 打开文件
            self.InputArea.clear()
            with open(fpath, encoding='utf-8') as f:
                try:
                    # utf-8格式读取
                    self.InputArea.append(f.read())
                except Exception as e:
                    # gb18030格式读取
                    with open(fpath, encoding='gb18030', errors='ignore') as f:
                        self.InputArea.append(f.read())
            self.SaveButton.setEnabled(True)        # 文件已打开，激活保存按钮
            self.InputArea.setFocusPolicy(QtCore.Qt.StrongFocus)    # 鼠标和tab获取焦点, 仅在打开文件时可获得焦点，闭面快捷键误存
            # 自动保存线程等待
            self.auto_wait_flag = False

    # 得到选中路径
    def whichClicked(self, fpath):
        self.clickedPath = fpath
        self.SaveButton.setEnabled(False)   # 选中路径已更改，禁用保存按钮, autosave_Thread线程随之结束
        self.auto_wait_flag == True         # 自动保存线程等待
        self.InputArea.setFocusPolicy(QtCore.Qt.NoFocus)  # 无焦点，不可编辑,闭面快捷键误存

    # 不删除文件夹路径
    def delete(self):
        if self.clickedPath != "" and not os.path.isdir(self.clickedPath):
            os.remove(self.clickedPath)
            self.clickedPath = ""
            exec("self.file"+str(self.fname_number)+".deleteLater()")
            self.fname_number = -1

    # 重置关键参数
    def reset(self):
        self.fname_number = -1
        self.name_end_number = 0
        self.clickedPath = ""

    # 载入目录下文件并显示绑定点击方法
    def reload(self, dpath):
        # 删除原按钮
        for i in range(self.name_end_number):
            exec("self.file" + str(i) + ".deleteLater()")
        self.reset()
        # 获取目录
        fdir = os.listdir(dpath)
        fpath = []
        #  除去正文卷
        temp_list = fdir[:]
        for f in temp_list:
            if is_volumes(f):
                fdir.remove(f)
        # 名称排序
        if len(fdir) > 1:
            fdir = sorted(fdir, key=cmp_to_key(story_cmp))
        # 创建路径对映字典
        for f in fdir:
            f = self.chosen_dir + "/" + f
            fpath.append(f)
        fdir = list(map(clear_suffix, fdir))
        fileDict = dict(zip(fdir, fpath))
        # 添加返回上级按钮
        if self.chosen_dir != self.before_dir:
            fdir.insert(0, "上一级")
            fileDict["上一级"] = self.before_dir
        for f in fdir:
            fname = "file" + str(self.name_end_number)
            setattr(self, fname, myButton())
            exec("self." + fname + ".setObjectName(f)")
            exec("self.verticalLayout.addWidget(self." + fname + ")")
            exec("self." + fname + ".setText(self._translate(\"BodyForm\", f))")
            exec("self." + fname + ".clicked.connect(partial(self.whichClicked, fileDict[f]))")
            exec("self." + fname + ".clicked.connect(partial(self.checkedChange, self.name_end_number))")
            exec("self." + fname + ".openSingal.connect(partial(self.open, fileDict[f]))")
            self.name_end_number += 1

    # 选中后效果，预修改
    def checkedChange(self, name):
        print("clicked")
        if self.fname_number != -1:
            exec("self.file"+str(self.fname_number)+".setStyleSheet(\"background: transparent\")")
        exec("self.file"+str(name)+".setStyleSheet(\"background-color: rgb(85, 255, 255)\")")
        self.fname_number = name