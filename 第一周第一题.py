# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# fp = open("学生数据库（未按名字排好序）.txt", "w")
# student = "null"
# fp.write("姓名 \t年龄 \t性别 \t班级 \t学号\n")
# while student != "":
#     student = input("请输入学生的姓名、年龄、性别、班级、学号\
#     用空格分隔各项信息，输入完毕，直接按回车键结束输入。\n")
#     if student == "":
#         break
#     else:
#         student = student.split(" ")
#         student = " \t".join(student)
#         student += "\n"
#         fp.write(student)
# fp.close()
import numpy as np
import matplotlib.pyplot as plt

n = 100
r = np.random.uniform(-50, 50, size=2*n)
r = np.copy(np.reshape(r, (2, n)))
fig = plt.figure(dpi=250)
plt.scatter(r[0, :], r[1, :], s=5)
plt.tight_layout()
plt.show()



