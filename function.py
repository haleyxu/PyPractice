#函数的定义
def SayHello():
    print("Hello")
#函数的调用
SayHello()

#函数的位置实参
#函数的关键字实参
def func(One, Two, Three):
    print("顺序是:" + One + Two + Three)

func(One = "Haley", Three = " Sttch", Two = " Like")

#参数的默认值
def func1(site1, site2 = "Jiangxi"):
    print("Haley in " + site2 + ", but he work in " + site1)

func1("JiLin")
func1("JiLin", site2 = "Yancheng")
#列表的传递
list1 = ["a", "b", "c"]
def changelist(listarg):
    print(listarg)
    listarg.pop()
    print(listarg)

changelist(list1)
print(list1)
    #如果只是想进行列表的值传递可以 changelist(list1[:])

#参数列表使用任意数量的参数
def manyarg(*tup):
    print(tup)

manyarg("Haley", "Marry", 1, 2.3)


"""任意参数和位置参数和结合使用
    需要将任意参数的形参放在参数列表的最后"""
def siteandarg(num, *names):
    print("have " + str(num) +
    "people" + str(names))
siteandarg(3, "Haley", "Marry", "Jack")


"""位置参数和任意关键字参数
    需要将任意参数的形参放在参数列表的最后"""
def keyvalue(arg1, **content):
    print("Book name is " + arg1)
    for key, value in content.items():
        print(key + "->" + value)

keyvalue("Xinhuazidian", Black="white", High="Low")



