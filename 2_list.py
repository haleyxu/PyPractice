alist = [1,2,3,4,5,6]


#使用for来遍历列表
for num in alist:
    print(num)

#range()函数的使用
numbers = list(range(1,1000,2))


for i in numbers:
    print(i)


#简单的统计计算的函数
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#列表解析
items = [value ** 2 for value in range(1, 101)]
print(items)


#练习
for i in range(1, 21):
    print(i)
#3 - 30的3的倍数
emptylist = []
for i in range (3, 31):
    if i % 3 == 0:
        emptylist.append(i)
print(emptylist)

emptylist2 = [i for i in range(3, 31, 3)]
print(emptylist2)

#in ;  not in 的用法要注意
#列表的空和非空可以用作判断
#print 的多行使用
#字典是无序的，在使用for循环时也无法保证遍历顺序按照初始化的来
print("help"+
        "ye")
