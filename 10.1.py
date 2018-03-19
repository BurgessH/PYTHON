#函数：
##1.0.局部变量和全局变量()
a = 400 #全局变量，可以在后面的代码中使用。
def test1():
    a = 200 #局部变量只能在该函数中使用；作用域为函数体内；
    a += 50
    print("test1中a的值为： %s"%a)  
    return a

def test2(a):
    #a = 300  
    print("test2函数中a的值为： %s"%a)

a = test1() #如果函数的局部变量和全局变量的名字一样，优先使用的是局部变量。
test2(a)
print(a)

##2.0.在函数中全局变量修改:如果是可变类型可以执行修改变量的值；
# 不可变类型值是不能修改：本质上来说不可变类型值的修改，只是修改了引用。
    ## 不可变类型：字符串；元祖
    ##可变类型：列表、字典

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

#3.0.函数返回多个值：
def test1():
    a = 1
    b = 2
    return a,b

x, y=test1()
print(x, y)

x=test1()
print(x) #返回元祖  

##1.缺省参数：
def test1(x,y,z=10): #带有默认值的参数一定要位于参数列表的最后面
    return x+y+z
print("sum = %s"%test1(5,6))

##2.不定长参数:
def test2(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)
    sum = x
    for i in args:
        sum+=i
    for i in kwargs.values():
        sum+=i
     print("sum = %s"%sum)

test2(2, 3, 4, 5, 6, num1=5, num2=6) #字典表示

##3.集合的拆包：
    names = [3,4]
    names2 = {"num1":5, "sdf":6} 
    test2(2, *names, **names2)  ##拆包
