# -*- coding:utf-8 -*-
"""
@author: xcld
@file: hw.py
@time: 2022-12-26 17:08
"""
# 1题
# li = ["lex", "WuSi", "ruantian", "barry", "wenzhou"]
# print("1.1 li长度为：", len(li))
# li.append('seven')
# print("2)列表中追加元素' seven ',并输出添加后的列表li:", li)
# li.insert(0, 'Tony')
# print("3)请在列表的第1个位置插⼊元素Tony,并输出添加后的列表:", li)
# li.insert(1, 'kelly')
# print("4)请在列表的第2个位置插⼊元素kelly,并输出添加后的列表:", li)
# print("5)……每⼀个元素添加到列表li中，⼀⾏代码实现，不允许循环添加:", li + [1,"a",3,4,"heart"])
# # s = "qwert"
# # li.extend(s)
# # print(li)
# print("6)请将字符串s = qwert 的每⼀个元素添加到列表li中，⼀⾏代码实现，不允许循环添加。:", li + list({}.fromkeys("qwert").keys()))
# li.remove("lex")
# print("7)请删除列表中的元素\"eric\"(这里搞错了吧，我随便删一个比如lex吧),并输出添加后的列表:", li)
# li.pop(1)
# print("8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表:", li)
# del li[1:4]
# print("9)请删除列表中的第2⾄4个元素，并输出删除元素后的列表:", li)
# li.reverse()
# print("10)请将列表所有得元素反转，并输出反转后的列表:", li)
# # print(":",)
# print("11)请计算出\"seven\"元素在列表li中出现的次数，并输出该次数。:", li.count("seven"))

# 2题

# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# print("1)通过对li列表的切⽚形成新的列表l1,l1 = [1,3,2]:", li[:3])
# # print(":",)
# print("2)通过对li列表的切⽚形成新的列表l2,l2 = [\"a\",4,\"b\"]:", li[3:6])
# l3 = li[:3] + li[3:7]
# l3.remove("a")
# l3.remove("b")
# l3.remove(3)
# # l3 = filter(str.isdigit, [list(ll) for ll in li])
# print("3)通过对li列表的切⽚形成新的列表l3,l3 = [\"1,2,4,5]:", l3)
# l4  =  []
# l4.append(li[1])
# l4.append(li[3])
# l4.append(li[5])
# print("4)通过对li列表的切⽚形成新的列表l4,l4 = [3,'a','b']:", l4)
# l5 = list(li[-1])
# print("5)通过对li列表的切⽚形成新的列表l5,l5 = [\"c\"]:", l5)
# l4.reverse()
# l6 = l4
# print("6)通过对li列表的切⽚形成新的列表l6,l6 = [\"b\",\"a\",3]:", l6)

# 3题

# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# print("1）法一：", lis[3][2][1][0].upper(), "1）法二：", lis[-3][-2][1][0].upper())
# lis[1] = 100
# lis[3][2][1][1] = 100
# print("2)法一：", lis)
# lis2 = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis2.remove(3)
# lis2[2][2][1].remove(3)
# lis2.insert(1, 100)
# lis2[3][2][1].insert(1, 100)
# print("2)法二：", lis2)
# lis3 = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis3[3][2][1][2] = 101
# print("3)法一：", lis3)
# lis3[3][2][1].remove(101)
# lis3[3][2][1].insert(2, 101)
# print(lis3)
# lst = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [11, 22, 33]]
# lis1 = [j for i in lst for j in i]
# print(lis1)
# print("1)将列表lis中的\"tt\"变成⼤写（⽤两种⽅式）:", lis[3][2][1][0].upper())
# print(":",)

# 第4题：
# li = ["lex", "eric", "rain"]
# su1 = "_"
# print(su1.join(li))

# 第5题
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for key in range(len(li)):
#     print("key:", key)

# 第6题
# lst = []
# for Num in range(1, 100):
#     if Num % 2 == 0:
#         lst.append(Num)
# print(lst)

# 第7题
# lst = []
# for Num in range(1, 51):
#     if Num % 3 == 0:
#         lst.append(Num)
# print(lst)

# 第8题
# lst = []
# for Num in range(100, 0, -1):
#         lst.append(Num)
# print(lst)

# 第9题
# lst = []
# for Num in range(100, 9, -1):
#     if Num % 2 == 0:
#         lst.append(Num)
# print(lst)
# lst = [Num for Num in range(100, 9, -1) if Num % 2 == 0]
# lst =[Num for Num in range(100, 0, -1)]
# print(lst)


# 第10题：
# lst =[Num for Num in range(1, 31)]
# for key, value in enumerate(lst):
#     if value % 3 == 0:
#         lst.remove(value)
#         lst.insert(key, "*")
# print(lst)


# 第11题：
# li1 = []
# li = ["TaiBai ", "le xC", "AbC ", "egon", " ri TiAn", "WuSir", " aqc"]
# for value in li:
#     value2 = value.split(" ")
#     value1 = "".join(value2)
#     if value1.startswith("A") or value1.startswith("a") or value1.endswith("c"):
#         li1.append(value1)
# print(li1)

# 第12题
## 法1(集合实现)：
# li1 = []
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# se1 = set(li)
# ca = input("请输入评论内容：")
# kk = set()
# kk.add(ca)
# # uu = se1 & kk
# if se1 & kk:
#     li1.append("*"*len(ca))
# else:
#     li1.append(ca)
# print(se1)
# print(kk)
# print(li1)
#
# ## 法2（列表实现）：
# ca1 = input("请输入评论内容2：")
# li3 = [ca1]
# li4 = []
# if ca1 in li:
#     li4.append("*"*len(ca1))
# else:
#     li4.append(ca1)
# print(li4)

# 第13题
# li = [1, 3, 4, "lex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
#
# # co = [su if type(su) != list else su1 for su1 in su for su in li]
#
# for su in li:
#     if type(su) != list:
#         print(su)
#     else:
#         for su1 in su:
#             print(su1)


# 第14题
# Sum1 = []
# while True:
#     score = input("请输入您的姓名和成绩格式如：张三_44,输入完毕输#号结束：")
#     if score == "#":
#         break
#     else:
#         Sm = int("".join(list(filter(str.isdigit, score))))
#         Sum1.append(Sm)
# print("数学考试平均分为：", sum(Sum1)/len(Sum1))

# 第15题
# Qqn = int(input("请输入一个敲7数字："))
# lst = [Num for Num in range(1, Qqn)]
# for key, value in enumerate(lst):
#     if value % 7 == 0:
#         lst.remove(value)
#         lst.insert(key, "咣")
# print(lst)

# 第16题
nlis = []
nlis1 = []
nlis2 = []
i = 10
j = 3
k = 1
while i:
    name = input("请依次输入十位心仪女生姓名：")
    nlis.append(name)
    i -= 1
for key, value in enumerate(nlis):
    print("女生名字为：", value, "序号为：", key)
while j:
    index = int(input("请依次选择三位心仪女生序号输入："))
    # if i >= index >= 0:
    nlis1.append(nlis[index])
    # else:
    #     print("请输入正确序号!")
    j -= 1
for key, value in enumerate(nlis1):
    print("女生名字为：", value, "序号为：", key)
while k:
    index1 = int(input("请最终选择一位心仪女生序号输入："))
    # if j >= index1 >= 0:
    nlis2.append(nlis1[index1])
    # else:
    #     print("请输入正确序号!")
    k -= 1
for key, value in enumerate(nlis2):
    print("用户心动的女生是", value)
# 第15题




# print(type(li))

# lst2 = [num for num in lst if num % 4 == 0]
# print(lst2)

# list_1 = [x for x in range(1, 10) if x % 2 == 0]
# print(list_1)
