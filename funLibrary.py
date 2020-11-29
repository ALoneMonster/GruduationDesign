# encoding: utf-8
"""
@author: XLYF
@file: funLibrary.py
@time: 2020/11/24 14:30
@desc:
"""
# 公共功能函数
import re
import os
from PyQt5.QtWidgets import QWidget

# 中文数字比较排序, 仅针对第XX卷、章：XXXX格式
def cmp(one, two):
    number_dict = {
        '一': 1,
        '二': 2,
        '三': 3,
        '四': 4,
        '五': 5,
        '六': 6,
        '七': 7,
        '八': 8,
        '九': 9,
        '十': 10,
        '百': 100,
        '千': 1000,
        '万': 10000
    }
    if len(one) < len(two):
        return -1
    elif len(one) > len(two):
        return 1
    else:
        number_temp_one = one[1:-1]
        number_temp_two = two[1:-1]
        for i in range(len(number_temp_one)):
            if number_dict[number_temp_one[i]] < number_dict[number_temp_two[i]]:
                return -1
            elif number_dict[number_temp_one[i]] > number_dict[number_temp_two[i]]:
                return 1
        return 0


# 针对中文数字字符串的排序，小说版，字符串格式：“第XX章：XXXX”
def story_cmp(fileone, filetwo):
    # 章节排序
    if fileone.endswith(".docx") and filetwo.endswith(".docx"):
        temp_one = fileone.split("：", 1)[0]
        temp_two = filetwo.split("：", 1)[0]
        return cmp(temp_one, temp_two)
    elif "." not in fileone and "." in filetwo:
        return -1
    elif "." in fileone and "." not in filetwo:
        return 1
    elif "." in fileone and "." in filetwo:     # 角色、剧情、杂项文件，无排序
        return 0
    else:
        return cmp(fileone, filetwo)    # 文件夹排序


# 去除文件后缀, map返回值是Iterable
def clear_suffix(filename):
    if "." in filename:
        return filename.split('.')[0]
    else:
        return filename


# 判断是否是正文分卷文件夹名
def is_volumes(filename):
    # f分卷角色、剧情、杂项模式
    p0 = r"第.+卷(?!角色).*"
    p1 = r"第.+卷(?!剧情).*"
    p2 = r"第.+卷(?!杂项).*"
    pattern0 = re.compile(p0)
    pattern1 = re.compile(p1)
    pattern2 = re.compile(p2)
    if re.match(pattern0, filename) and re.match(pattern1, filename) and re.match(pattern2, filename):
        return True
    else:
        return False

# 判断是否是角色文件，角色文件格式以”角色开头“
def is_role(filename):
    p = r"角色.+"
    pattern = re.compile(p)
    if re.match(pattern, filename):
        return True
    else:
        return False

# 确认小说文件夹存在
def story_exist(spath):
    if not os.path.exists(spath):
        try:
            os.makedirs(spath)
            os.mkdir(spath+"/"+"角色")
            os.mkdir(spath+"/"+"剧情")
            os.mkdir(spath+"/"+"杂项")
        except Exception as e:
            print(e)
            print("创建文件夹失败")


# 判断窗口状态, 返回数字
# normal 0
# mini 1
# max 2
# fullscreen 3
def windowstate(win: QWidget) -> int:
    if win.isMinimized():
        return 1
    elif win.isMaximized():
        return 2
    elif win.isFullScreen():
        return 3
    else:
        return 0


# 窗口尺寸变化快捷键绑定的方法
def window_size_change(win: QWidget) -> None:
    change = {
        0: lambda x: x.showMaximized(),
        2: lambda x: x.showFullScreen(),
        3: lambda x: x.showNormal()
    }
    change[windowstate(win)](win)