"""
python 回顾练习
"""
#使用和学习string的库和语法
#字面的string有"xx"和'xx'两种方式 
FirstName = 'Haley'
LastName = "Xu"

name = "haley xu"

HaveSpaceStr = " String "

name = name.upper()
changename = name.upper()

Name =  FirstName + " " +LastName

NoSpaceStr = HaveSpaceStr.strip()
RSpaceStr = HaveSpaceStr.rstrip()
LSpaceStr = HaveSpaceStr.lstrip()


print(name)
print(changename)
print(Name)
#打印输出常用的转换字符 \n \t
#这里出现一个需求：name不要字符而要对应的变量
print("name \n\t Name")
#查看strip函数,用于剥除字符串首尾空格,r-和l-
print("|" + HaveSpaceStr + "|")
print("|" + NoSpaceStr + "|")
print("|" + RSpaceStr + "|")
print("|" + LSpaceStr + "|")

"""
课后习题
"""
#2.3
username = "Haley xu"
print(username + " like programming!")
#2.4
#upper name
print(username.upper())
#lower name
print(username.lower())
#title name
print(username.title())


