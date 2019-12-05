# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from xpinyin import Pinyin  # 导入解决中文名字排序的问题的包
try:
    fp = open("学生数据库（未按名字排好序）.txt", "r")
except FileNotFoundError:
    print("文件不存在")
else:
    head = fp.readline()
    students = fp.readlines()
    fp.close()
    students = [a[:-1] for a in students]
    count1 = " ".join(students).count("男")
    print("全部同学一共有{0}人，男生有{1}人，女生有{2}人。".format(len(students),
                                                count1, len(students) - count1))
print("未排好序前的文件")
print(head)
for i  in range(len(students)):
    print(students[i])


def find_space(str1):
    # 找到第一个空格的索引，索引用index1存储
    index1 = 0
    for i in range(len(str1)):
        if str1[i] != " ":
            index1 = i
        if str1[i] == " ":
            break
    return index1


def paixu(lis):  # 输入一个名字的列表，按照拼音来排序
    pin = Pinyin()
    result = []
    for item in lis:
        result.append((item, pin.get_pinyin(item[:find_space(item) + 1])))
        # 加入拼音
    result.sort(key=lambda x: x[1])  # 对拼音排序
    result = [x[0] for x in result]
    return result


students = paixu(students)
fp = open("学生数据库（按名字排好序）.txt", "w")
fp.write("姓名 \t年龄 \t性别 \t班级 \t学号\n")
for i in range(len(students)):
    students[i] += "\n"
    fp.write(students[i])
fp.close()


