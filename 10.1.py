#函数：
##1.0.局部变量和全局变量()
# a = 400 #全局变量，可以在后面的代码中使用。
# def test1():
#     a = 200 #局部变量只能在该函数中使用；作用域为函数体内；
#     a += 50
#     print("test1中a的值为： %s"%a)  
#     return a

# def test2(a):
#     #a = 300  
#     print("test2函数中a的值为： %s"%a)

# a = test1() #如果函数的局部变量和全局变量的名字一样，优先使用的是局部变量。
# test2(a)
# print(a)

##2.0.在函数中全局变量修改:如果是可变类型可以执行修改变量的值；
# 不可变类型值是不能修改：本质上来说不可变类型值的修改，只是修改了引用。

names = ["one", "two", "three"] #列表
student = {"name":"onex"}       #字典
a = "miss"                      #字符串
b = 200

def test3():
    print("原始全局变量为： %s"%names)
    names[2] = "four"              #修改全局变量
    student["age"] = 23
    global a
    a = "toyota"                
    b =b + 1

test3()

print("现在列表的元素：%s"%names)
print("现在元祖的元素：%s"%student)
print("现在字符串的元素：%s"%a)
print("现在常量的元素：%s"%a)

    