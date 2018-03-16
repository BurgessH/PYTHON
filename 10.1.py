#函数：
#1.0.局部变量和全局变量()
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


# 可变变量，不可变变量
# #函数返回多个结果
# def test():
#     a = 1
#     b = 2
#     return a, b

# #函数传参:
# def test1(x, y):
#     x.replace("c", "C")  
#     y.append(10)
#     printf("x变量指向内存地址为：%s"%id(x))
#     printf("y变量指向的内存地址为：%s"%id(y))

# a="abcdef"
# b=[1, 2, 3]
# printf("a变量指向的内存地址为：%s"%id(a))
# printf("b变量指向的内存地址为：%s"%id(b))

# test1(a, b)
# 封装函数：学生管理系统
# 递归函数：



# 经常使用：
#     cd ls pwd touch mkdir chmod
#     cp mv rm
#     cat more less head tail 
#     ln:   建立连接文件
#     wc:     统计文件行数、字符数、单词数
#     whatis: 命名简单说明
#     whereis: 命令的源程序或手册位置
#     which: 可执行程序的路径和它的别名

# 压缩与解压
#     tar\tar.gz文件解压及压缩
#     tar xvf test.tar
#     tar xvf test.tar /dir1 /dir2 file3
#     tar xzvf linux.tar.gz
#     tar czvf test.tar.gz /dir1 /dir2 file3

#     .gz/ .z/ .Z/ .tgz格式文件
#     gzip file1 file2
#     gzip -d file1.gz
#     gzip -r /dir1
#     gzip -rd /dir

# 系统相关
#     time, data, uname, lsb_release
#     du: 统计文件和目录所占磁盘空间
#     dmesg: 显示内核状态信息
#     uptime: 显示时间、系统运行时间、用户连接、负载；
#     who/w: 查看登录用户
#     whoami\hostname
#     cal\bo:日历、计算器


    