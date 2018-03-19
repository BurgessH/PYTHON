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

def test(x,y)
    x.replace("c", "C")
    y.append(10)
    print("x变量的内存地址为：%s"%id(x))
    print("x变量的内存地址为：%s"%id(y))

a="abcdef"
b=[1,2,3]
print("a变量指向内存地址为：%s"%id(a))
print("a变量指向内存地址为：%s"%id(b))
test()

## 函数封装：
print("="*30)
print("学生管理系统".center(30))
print("输入1： 添加学生")
print("输入2： 查找学生")
print("输入3： 修改学生")
print("输入4： 删除学生")
print("输入5： 查看所有学生")
print("输入6： 退出")

#一个学生包含多个信息，一个学生一个字典。学生列表用列表存储。
stus=[]
while True:
    operate = input("请输入你想要的操作：")
    if operate=="1":
        name = input("请输入添加学生的姓名：")
        age  = int(input("请输入学生的年龄："))
        qq   = input("请输入学生的QQ号:")

#一个学生包括三个信息，这三个信息存到一个字典中。
        stu = {}        #申明一个字典变量；
        stu["name"] = name
        stu["age"]  = age
        stu["qq"]   = qq
        stus.append(stu)
        print("添加成功")

    if(operate=="2"):
        name = input("请输入要查找学生的姓名：")
        for item in stus:
            if item["name"]==name.strip(): #判断字典中有包含查询学生
                print("%s 学生存在，年龄为：%s, QQ号为：%s" %(item["name"], item["age"], item["qq"]))
                break
            else:
                print("学生%s没有找到"%name)

    if(operate=="3"):
    if(operate=="4"):
        name = input("please input name:")
    if(operate=="5"):
        
    