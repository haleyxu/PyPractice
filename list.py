listofcolor = ["red", "blue", "green", "yellow"]

#列表的打印会自带方括号，输出形式和赋值的样式一致
print(listofcolor)
#下标索引,特别的支持负值索引
print(listofcolor[0])
print(listofcolor[-2])


#列表的操作 增、删、改、查
#改
listofcolor[0] = "black"
print(listofcolor)
#增：尾部追加
listofcolor.append("brown")
print(listofcolor)
#增：插入
listofcolor.insert(0, "orange")
print(listofcolor)
#删:del 语句
del listofcolor[0]
print(listofcolor)
#删:pop(),会返回弹出的值
popelement = listofcolor.pop()
print(listofcolor)
print(popelement)
popelement = listofcolor.pop(1) #弹出blue
print(listofcolor)
print(popelement)

#新建一个list
fruit = ["apple", "banana", "orange", "apple"]
#删:remove 根据名字删除
print(fruit)
fruit.remove("apple")
print(fruit)

"""
总结：
增加：append(element); insert(index, element)
删除：del list[index]; pop(index); remove(element)
"""


#练习
vipname = ["a1", "a2", "a3"]
print("邀请参加宴会\n")
print("邀请的名单为：" + str(vipname))
print("很遗憾 (" + vipname[0] + ")无法到达 ")
print("邀请到了 a0和a4和a5")
vipname.insert(0, "a0")
vipname.insert(-1, "a4")
vipname.append("a5")
print(vipname)


"""
这里是一些关于列表顺序的操作
"""
numlist = [7,9,12,0,4]
print(numlist)
#更改性排序
numlist.sort()
print(numlist)
numlist.sort(reverse=True)
print(numlist)
#临时排序“函数”,同样拥有reverse 参数
print(sorted(numlist))
print(numlist)
#reverse方法
numlist.reverse()
print(numlist)

