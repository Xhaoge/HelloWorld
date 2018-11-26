print("     尼玛")
print("welcome to china")
#随机ｒａｎｄｏｍ
print("来竞猜随机数字(0-100)")
print("游戏开始......")
import random
x=int((random.random())*100)
i=1
while  True:
    xx=int(input('请输入你要猜的数字：'))
    if xx>x:
        print('对不起，你猜出的数字偏大！')
    if xx<x:
        print('对不起，你猜出的数字偏小！')
    if xx==x:
        print('恭喜你！终于猜对了。。。')
        print('然而，没什么卵用')
        break
    i+=1
print('你一共猜了%d次'%i)
#时间睡眠
import time
while True:
    t=time.localtime()
    time.sleep(1)
    print("%02d:%02d:%02d"%t[3:6],end='\r')
#x**y
def fy(n):
    return lambda s:s*n
x=fy(2)
print(x(4))
def fx(x,y):
    if y==1:
        return x
    return x*fx(x,y-1)
print(fx(3,3))
#最小公倍数
def fz(a,b):
    c=min(a,b)
    for i in range(c+1,1,-1):
            if a%i==0 and b%i==0:
                #fz(a,b)
                return i
                #print(i) 
print(fz(54,36))
#杨辉三角
#         [1]
#        [1,1]
#       [1,2,1]
#      [1,3,3,1]
#     [1,4,6,4,1]
#   [1,5,10,10,5,1]
def get_next_line(L):
    line = [1]  # 最左侧的1
    # 计算中间的数字
    for i in range(len(L) - 1):  # i绑定L的索引
        line.append(L[i] + L[i + 1])
    # 在最后放入一个1
    line.append(1)
    return line

def get_yh_list(n):  # n 代表行数:
    L = []
    line = [1]  # 当前是第一行
    for _ in range(n):
        L.append(line)  # 当前行放进行
        # 再算出下一行,准备放入
        line = get_next_line(line)

    return L


def list_to_string(L):
    '''此函数任意给定一个列表,将其转换为字符串
    如: L = [1, 3, 3, 1], 则返回 '1 3 3 1'
    '''
    L2 = [str(x) for x in L]  # L2 = ['1', '3', '3', '1']
    return ' '.join(L2)


# L = [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1]
# ]

L = get_yh_list(6)
print(list_to_string(L))

# 得到最下面一行占几个字符的宽度:
max_char = len(list_to_string(L[-1]))
print(L)
# 居中显示
for line_list in L:
    s = list_to_string(line_list)
    print(s.center(max_char))
#ｔｒｙ－ｅｘｅｃｐｔ
def get_score():
    ss=input('请输入你的成绩：')
    s=int(ss)
    print('你的成绩为%d分'%s)
try:
    get_score()
except ValueError as e:
    print('你的成绩为0分','\n','错误为：',e)
else:
    print('Nima')
finally:
    print('不管怎么样，都被执行')

try:
    try:
        n=int(input('请输入整数：'))
    except ValueError:
        print('try 在内层出现值错误！')
    else:
        print('没有出现问题')
#raise
def get_age():
    ss=int(input('请输入你的年龄：'))
    if ss<=0 or ss>=140:
        raise ValueError
    return ss
try:   
    age=get_age()
    print('用户输入的年龄是：',age)
except ValueError as cc:
    print('用户输入的不是１～１４０的整数，获取年龄失败')
    print('错误是：',cc)
#高空坠落
def hig(m,n,s):
    m=0.5*m
    s=s+2*m
    if n==1:
        return '当前距离地面为：',m,'总共行走的路程为：',s
    else:
        return hig(m,(n-1),s)
print(hig(100,9,100))
#质数函数
def get_sushu(a):
    if a<2:
        return False
    for x in range(2,a):
        if a%x==0:
            return False
    return True
l=[]
n=int(input("请输入一个整数："))
num=n
while n!=1:
    for i in range(2,n+1):
        if n%i==0:
            l.append(i)
            n=n//i
            break
print(l)
print(str(num)+'='+'*'.join(str(x) for x in l))
#yield
L=[2,3,5,7]
def mygun(L):
    for x in L:
        yield x**2+1
gen=mygun(L)
for a in gen:
    print(a)
print('-------')
#enumerate
L=[]
while True:
    line=input('请输入任意行文字，输入空格时结束：')
    if line=='':
        break
    L.append(line)
for x,y in enumerate(L):
    print(x,y)
    print('第%d行：'%x,y)

def get_sushu(a):
    if a<2:
        return False
    for x in range(2,a):
        if a%x==0:
            return False
    return True
def prime(begin,end):
    while begin<=end:
        result=get_sushu(begin)
        if result is True:
            yield begin
        begin+=1
l=[x for x in prime(10,100)]
print(l)
def myrange(start,stop,step=1):
    while start<=stop:
        yield start
        start+=1

l=[x**2 for x in myrange(1,10) if x%2==1]
print(l)
print(sum(l))
#读取文件
def read_info():
    rl=[]
    try:
        f=open('info.txt')
        l=f.readlines()
        for line in l:
            s=line.strip()
            name,age,score=s.split()
            rl.append({'name':name,
                        'age':age,
                        'score':score})
        f.close()
        print('写入成功')
        return rl
    except OSError:
        print('写入失败') 
print(read_info())
#面向对象
class Car():
    def __init__(self,c,b,m):
        self.color=c
        self.brand=b
        self.model=m
    def show_info(self,speed):
        print(self.color,'的',self.brand,self.model,
             '正在以',speed,'公里小时行驶')
a4=Car('hongs','audi','A4')
a4.show_info(199)
class Student():
    def __init__(self,a,b,c=0):
        self.name=a
        self.age=b
        self.score=c
    def set_score(self,c):
        self.score=c
    def show_info(self):
        print(self.name,'的年龄是：',self.age,'成绩为：',self.score)
a1=Student('浩哥　','18','98')
a1.set_score(91)
a1.show_info()
a2=Student('黄哥　','81','19')
a2.show_info()
a3=Student('董大爷','78','58')
a3.show_info()
l=[]
l.append(Student('浩哥','18','98'))
l.append(Student('黄哥','81','19'))
l.append(Student('董jj',78))
l[2].set_score(99)
for x in l:
    x.show_info()
#写入文件
def iput():
    l=[]
    while True:
        n=input('请输入一系列整数：')
        if int(n)<0:
            break
        l.append(n)
    return l
l=iput()
f=open('number.txt','w')
for x in l:
    f.write(x)
    f.write('\n')
f.close()
print('写入成功！')
print(l)
#打开文件
def outp():
    f=open('number.txt')
    l=f.readlines()
    sn=0
    for x in l:
        sn+=int(x)
    f.close()
    print('最大值为：',max(l),'最小值为：',min(l),'和为：',sn)
outp()
#class综合例子
class Human():
    def __init__(self,a,n):
        self.name=a
        self.age=n
        self.money=0
        self.skill=[]
    def teach(self,other,skill):
        print(self.name,'教',other.name,'学',skill)
        other.skill.append(skill)
    def work(self,m):
        print(self.name,'上班赚了',m,'元')
        self.money+=m
    def borrow(self,other,m):
        print(self.name,'向',other.name,'借',m,'元')
        other.money-=m
        self.money+=m
    def show_info(self):
        print('nima!',self.age,'岁的',self.name,'有钱',self.money,'元'
            ,'他学会的技能有','　'.join(self.skill))
zhang3=Human('张三',35)
li4=Human('李四',8)
zhang3.teach(li4,'python')
li4.teach(zhang3,'王者荣耀')
zhang3.work(1000)
zhang3.borrow(li4,200)
zhang3.show_info()
#派生
class Hulist(list):
    def in_append(self,n):
        self.insert(0,n)
        return self
h=Hulist([1,2,3,4,5])
print(h.in_append(99))
#文件的复制
def my_copy():
    from_file=input('请输入要复制的源文件：')
    imp_file=input('请输入复制过后的目标文件：')
    try:
        f=open(from_file,'rb')
        try:
            ff=open(imp_file,'wb')
            try:
                while True:
                    b=f.read(4096)
                    if not b:
                        break
                    ff.write(b) 
                print('复制完成！')               
            finally:
                ff.close()
        except OSError:
            print('打开目标文件失败!')
        finally:
            f.close()
    except OSError:
        print('打开源文件失败!')
my_copy()
#将写入的信息，写入文本文件.txt中；
l=[]
while True:
    n=input('请输入任意文字：')
    if n=='':
         break
    l.append(n)
print(l)
#return l　　将信息存入到ｌ中
def read_filename(lst,filename='input.txt'):#定义函数读取信息
    f=open(filename,'w')
    for s in lst:
        f.write(s)
        f.write('\n')
    f.close()
print('写入成功！')
read_filename(l) 
#文本文件.txt的信息输出到列表
def ouput_file(filename='input.txt'):
    l1=[]
    f=open(filename)
    b=f.readlines()
    for x in b:
        c=x.strip().split()
        l1.append(c)
    print(l1)
    f.close()
    print("读取完成关闭")
ouput_file()
#读取文件打印出来
def get_mas(filename='info.txt'):
    l=[]
    f=open(filename)
    s=f.readlines()
    for ch in s:
        c,b,a=ch.strip().split()
        b=int(b)
        a=int(a)
        l.append({'name':c,'age':b,'score':a})
    f.close()
    for i in l:
        print(i['name'],'今年年龄为：',i['age'],'成绩：',i['score'])
get_mas()
#创建类应用
class Bicycle():
    def run(self,km):
        print("自行车骑行了", km, '公里')
class Ebicycle(Bicycle):
    def __init__(self,bat):
        self.volume=bat
        print('新买的电动车内有%d度电'%bat)
    def fill_charge(self,vol):
        self.volume+=vol
        print('充电%d度'%vol)
    def run(self,km):
        km=int(km)
        self.volume=self.volume-km/10
        if self.volume<0:
            print('行驶了%dkm剩余0度电'
                 '用脚登骑行了%dkm'%(km-abs(self.volume)*10,abs(self.volume)*10))
            self.volume=0
        else:
            print('行驶了%dkm剩余%d度电'%(km,self.volume))
b=Ebicycle(5)
b.run(10)
b.run(100)
b.fill_charge(10)
b.run(50)
#类创建应用
class Hulist():
    def __init__(self,n,a):
        self.name=n
        self.age=a
        #print('被调用')
    def infos(self):
        print('姓名 ',self.name,"年龄 ",self.age)
class Stude(Hulist):
    def __init__(self,n,a,s=0):
        super(Stude,self).__init__(n,a)#调用父类的初始化方法
        self.score=s
        #print('oooo')
    def infos(self):
        super().infos()
        print('成绩：',self.score)
#迭代器
class Hulist():
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __str(self):
        return '%s'%self.data
    def __repr__(self):
        return "'%s'"%self.data
    def __len__(self):
        return len(self.data)
    def __bool__(self):
        return False
    def __iter__(self):
        return mylistiterator(self.data)
class mylistiterator():
    """docstring for mylistiterator"""
    def __init__(self, lst):
        self.data_lst = lst
        self.cur_index=0
    def __next__(self):
        if self.cur_index>=len(self.data_lst):
            raise StopIteration
        r=self.data_lst[self.cur_index]
        self.cur_index+=1
        return r
n1=Hulist([1,23,34,-4,-1])
it=iter(n1)
print(next(it))
for x in n1:
    print(x)
print(next(it))
#Fibonacci可迭代对象
class Fibonacci:
    def __init__(self,n):
        self.num1=0
        self.num2=1
        self.num=n
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count<=self.num:
            self.num1,self.num2=self.num2,self.num1+self.num2
            self.count+=1
            return self.num1
        else:
            raise StopIteration
for x in Fibonacci(10):
    print(x)
#重载运算符
class Mylist:
    def __init__(self,iterable=()):
        self.data=list(iterable)
    def __repr__(self):
        return 'Mylist(%s)'%self.data
    def __add__(self,other):
        v=self.data+other.data
        return Mylist(v)
    def __mul__(self,other):
        return Mylist(self.data*3)
l1=Mylist([1,2,3])
l2=Mylist([4,5,6])
l3=l1+l2
l4=l1*3
print(l3)
print(l4)
#函数重载
class Mylist:
    def __init__(self,iterable=()):
        self.data=list(iterable)
    def __repr__(self):
        return 'Mylist(%s)'%self.data
    def __add__(self,other):
        v=self.data+other.data
        return Mylist(v)
    def __mul__(self,other):
        return Mylist(self.data*3)
    def __rmul__(self,other):
        print('rmul被调用！')
        return Mylist(self.data*3)
    def __contains__(self,e):
        return True if e in self.data else False
    def __getitem__(self,i):
        return self.data[i]
    def __setitem__(self,i,v):
        self.data[i]=v
    def __delitem__(self,i):
        del self.data[i]
l1=Mylist([1,2,3])
l2=Mylist([4,5,6])
l3=l1+l2
l4=l1*3
l5=4*l1
print(l3)
print(l4)
print(l5)
if 2 in l1:
    print('嘿，你在！')
else:
    print('不在！')
l1[2]=99
print(l1)
del l1[0]
print(l1)
#迭代器的应用
class Prime:
    def __init__(self,s,n):
        self.data=s
        self.number=n
        self.count=0
    def __isprime(self,s):
        while True:
            if s<2:
                return False
            for x in range(2,s):
                if s%x==0:
                    return False
            return True  
    def __iter__(self):
        return self
    def __next__(self):
        '''此方法用来实现迭代器协议'''#print('__next__方法被调用')
        if self.count > self.number:
            raise StopIteration
        while self.count<=self.number:
            if self.__isprime(self.data):
                r=self.data
                self.count += 1 
                self.data+=1
                return r  
            self.data+=1           
L=[x for x in Prime(10`,4)]
print(L)
#定义类
class OrderSet:
    def __init__(self,iterable=()):
        self.data=set(iterable)

    def __repr__(self):
        return repr(self.data)

    # def __and__(self,rhs):
    #     return self.data & rhs.data

    def __or__(self,rhs):
        return self.data | rhs.data

    def __xor__(self,rhs):
        return self.data ^ rhs.data
    def __lshift__(self,rhs):
        return self.data < rhs.data

    def __rshift__(self,rhs):
        return self.data > rhs.data
    def __contains__(self,e):
        return True if e in self.data else False

s1 = OrderSet([1, 2, 3, 4])
s2 = OrderSet([3, 4, 5])
print(s1 & s2)  # OrderSet([3, 4])
print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
print(s1 ^ s2)  # OrderSet([1, 2, 5])
if OrderSet([1, 2, 3]) != OrderSet([1, 2, 3, 4]):
    print("不相等")
else:
    print("相等")
if s1 == OrderSet([3, 4, 5]):
    print("s1 == OrderSet([3, 4, 5])")
else:
    print("s1 != OrderSet([3, 4, 5])")
if 2 in s1:
    print('2 in s1　返回真')
if 23 in s1:
    print('23 in s1　返回真')
else:
    print("不在!")
#ｍｙｓｑｌ调用ｐｙｔｈｏｎ
import pymysql

db = pymysql.connect("localhost","root","123456")
cursor = db.cursor()
cursor.execute("create database indexdb;")
cursor.execute("use indexdb;")
cursor.execute("create table t1(id int,name char(20));")
n = 1
name="lucy"
while n <= 2000000:
    cursor.execute("insert into t1 values('%s','%s')" % (n,name+str(n)))
    # n = int(n)
    n += 1