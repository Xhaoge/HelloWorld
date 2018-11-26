
print('          *\n         ***\n        *****\n       *******\n      *********')
print("  welcome to china")
print(" 1*5=5,2*5=10,3*5=35")
a = 1
while a <= 9:
    b = 1
    while b <= 9:
        c = a+b
        print(a, "+", b, "=", c)
        b = b+1
    a = a+1
#

print("wlecome to china")
print("来计算时间，")
a = int(input("请输入６３３２０，来见证奇迹的时刻："))
b = 63320//3600
c = 63320%3600
d = c//60
f = c%60
print(b, "小时", d, "分钟",f, "秒")
#
print("wlecome to china")
print("中国古代的秤是１６俩一斤，")
print("那么，２１６俩是多少斤，")
a = int(input("请输入２１６，来见证奇迹的时刻："))
b = a//16
d = a % 16
print(b, "斤", d, "俩")
#
print("welcome to china")
print("今天是小米２０岁生日，每年有３６５天")
a=365*20
b=(a-4)//7
c=(a-4)%7
print("today is 星期四")
d=c+4
print("过了",b,"个星期天","余数为",d)
print("所以过了",b+1,"个星期天")
#尼玛

print("welcome to china")
a=int(input("请输入你想的小时数字："))
b=int(input("请输入你想的分钟数字(<=60)："))
c=int(input("请输入你想的秒数字(<=60)："))
s=a*3600+b*60+c
print("尼玛","一共",s,"秒")
#

a=int(input("请任意输入一个整数：　"))
if a>100:
    print("这个数大于１００")   
elif a<0:
    print("这个数小于０")
elif a<100 and a>80:
    print("这个数在８０到１００之间")
else:
    print("输入错误")

#尼玛　税收
    print("+----------------------+")
print("  税收标准计算程序")
print("              作者：孙浩")
print("          版权所有")
print("          盗版必究")
print("   welcome to!!!!")
a=float(input("请输入所查金额（元）："))

if a>=3500:
  c=a-3500
  if c<=1500:
     d=c*0.03
     print("你所缴税收为：",d,"元")
  elif c>1500 and c<=4500:
     d=c*0.1-105
     print("你所缴税收为：",d,"元")
  elif c>4500 and c<=9000:
     d=c*0.2-555
     print("你所缴税收为：",d,"元")
  elif c>9000 and c<=35000:
     d=c*0.25-1005
     print("你所缴税收为：",d,"元")
  elif c>35000 and c<=55000:
     d=c*3.0-2755
     print("你所缴税收为：",d,"元")
  elif c>55000 and c<=80000:
     d=c*0.35-5505
     print("你所缴税收为：",d,"元")
  else:
     d=c*0.45-13505
     print("你所缴税收为：",d,"元")
else:
  print("输入错误.....")

#尼玛　
a=int(input("请先输入一个季度（１－４）："))
if a==1:
    print(a,"这个季度包含的月份有１、２、３月")
elif a==2:
    print(a,"这个季度包含的月份有４、５、６月")
elif a==3:
    print(a,"这个季度包含的月份有７、８、９月")
elif a==4:
    print(a,"这个季度包含的月份有１０、１１、１２月")    
else:
  print("输入错误.....")

#尼玛
  print("welcome to china")
a=int(input("请先输入一个月份（１－１２）："))
if a in(1,2,3):
    print("这个",a,"月是１季度")
elif a in(4,5,6):
    print("这个",a,"月是２季度")
elif a in(7,8,9):
    print("这个",a,"月是３季度")
elif a in(10,11,12):
    print("这个",a,"月是４季度")    
else:
  print("输入错误.....")

#尼玛
  money = int(input("请输入商品金额："))
pay=money-20 if money >=100 else money
print("你需要支付",pay,"元")

#尼玛
print("welcome to china")
a=int(input("请输入是一个数："))
if a>=0:
    print("这个数的绝对值是：",a)
else:
    print("这个数的绝对值是：",-a)

#尼玛 条件表达式
print("welcome to china")
a=int(input("请再次输入是一个数："))
a=-a if a<=0 else a
print("这个数的绝对值是：",a)

#尼玛
print("尼玛")
print("welcome to china")
print("北京出租车计价器收费标准：")
a=float(input("请输入你的里程数:"))
if 0<=a<=3:
    print("本次驾驶费用为：１３元")
elif 3<a<15:
    a=round(13+2.3*(a-3),1)
    print("本次驾驶费用为：",a,"元")
elif a>=15:
    a=round(13+2.3*12+(a-15)*3.45,1)
    print("本次驾驶费用为：",a,"元")
else:
    print("输入错误")
#

a=int(input("请输入你科目１成绩(0-100)："))
b=int(input("请输入你科目２成绩(0-100)："))
c=int(input("请输入你科目３成绩(0-100)："))
if a>=b and a>=c:
    print("最高分为：",a)
    if b>=c:
        print("最底分为：",c)
    else:
        print("最底分为：",b)
if b>=a and b>=c:
    print("最高分为：",b)
    if a>=c:
        print("最底分为：",c)
    else:
        print("最底分为：",a)
if c>=b and c>=a:
    print("最高分为：",c)
    if b>=a:
        print("最底分为：",a)
    else:
        print("最底分为：",b)
print("平均分为：",round((a+b+c)/3,1))

#尼玛
print("尼玛")
print("welcome to china")
a=int(input("请输入一个年份："))
if a%4==0 and a%100!=0 or a%400==0:
    print(a,"年为闰年，哈哈")
else:
    print(a,"年为平年，呵呵")
#

print("身体质量指数")
b=float(input("请输入你的身高(m)："))
c=float(input("请输入你的体重(kg)："))
d=round(c/b**2,1)
print(d)
if d<18.5:
    print("呵呵，你的体重过轻....")
elif   18.5<=d<24:
    print("呵呵，你的体重在正常范围....")
else:
    print("呵呵，你的体重过重....")

#２０１８．８．３
print("welcome to china")
s=("fk;lafljjfjf;f;jfpfamsinhao\nsunhaohuanjiahuandongyil3240jfjsdlkfj")
name=input("请输入你的姓名：")
if name in s:
    print("你的名字出现了")
else:
    print("没有你的名字。。。。")
#

a=int(input("请输入矩形宽度："))
b=1
i=1
while b<=a: 
    print(b*"*")
    i=i+1
    b=2*i-1
#

s=input("请输入一个字符串：")
print("第一个字符为：",s[0])
print("最后一个字符为：",s[-1])
a=len(s)
b=int((a+1)/2-1)
if a%2!=0:
    print("中间字符为：",s[b])
else:
    print("偶数")

#
s=input("请输入一个字符串：")
a=len(s)
print("第一个为：",s[0])
print("最后一个为：",s[-1])
print("去掉第一个和最后一个字符为：",s[1:-1:1])
print("判断是否为回文?(回文是指中心对称的文字)")
if s[::1]==s[::-1]:
    print(s,"属于回文")
else:
    print(s,"不属于回文")

#
print("一起来绘制一个*三角形吧！！")
s=int(input("请输入一个边长数字："))
i=1
while i<=s:
   c=(2*i-1)*"*"
   i+=1
   print(" "*(s-len(c)//2),c)
print("距离侧边为：",s//2,"个*号","　哇，perfect")
#

s=input("请随意输入一个字符串：")
b=s.replace(" ","")
c=len(s)
a=len(b)
print("开始输入的字符长度为：",c)
print("处理过后的字符长度为：",a)
print("去除空格后的字符串为：",b)
print("perfect")

#
print("来玩居中排列吧！(只能为英文哟)")
s=input("请随意输入一个字符串1：")
u=input("请随意输入一个字符串2：")
n=input("请随意输入一个字符串3：")
a=len(s)
b=len(u)
c=len(n)
d=max(a,b,c)
print("+","-"*(d+2),"+")
print("|",s.center(d+2),"|")
print("|",u.center(d+2),"|")
print("|",n.center(d+2),"|")
print("perfect!!!!!!!")

#2018/8/16 
#用法颇多
print("     尼玛")
print("welcome to china")
si=input("请输入第一行：")
ui=input("请输入第二行：")
ni=input("请输入第三行：")
ab=str(max(len(si),len(ui),len(ni)))
fmt="%"+ab+"s"
print(fmt)
print(fmt%si+"\n"+fmt%ui+"\n"+fmt%ni)
#

i=1
while i<=20:
    print(i,end=" ")
    if i%5==0:
        print()
    i=i+1
else:
    print()

a=10    
while a>=1:   
    print(a,end=" ")
    a=a-1
else:
    print()

print("     MB")
#
print("     尼玛")
print("welcome to china")
a=int(input("请输入一个计算的数："))
i=1
s=0
while i<=a:
    s=s+i
    i=i+1
print("最终计算和结果为：",s)
#
a=int(input("请输入一个正方形长的数："))
n=1
while n<=a:
    i=1
    while i<=a:
        print(i,end=" ")
        i+=1
    print()  #换行
    n+=1
#
b=int(input("请输入一个正方形长的数："))
s=1
while s<=b:
    w=1
    while w<=b:
      print(s,end=" ")
      w+=1
    print()
    s+=1
#

s=0
while True:
    a=int(input("请输入一个数："))
    if a<0:
        break
    s=s+a    
print("您刚才输入数总和是：",s) 

#
ch=int(input("请输入正方形的*数边长："))
i=1
while i<=ch:
    if i==1 or i==ch:
       print("*"*ch)
    else:
       print("*"+" "*(ch-2)+"*")
    i+=1 
#

mi=int(input("请输入一个多项式的项数："))
end_mi=1/2**mi
print("最后一位数是：",end_mi)
s=round((1-(1/2)**mi)/(1/2),5)
print("最后的和是：",s)
#

lem=int(input("请输入一个多项式的项数："))
i=1
s=0
while i<=lem:
    n=((-1)**(i+1))*1/(2*i-1)
    s+=n
    i+=1
print("最后一项为：",round(n,10))
print("最后的计算结果为：",round(s,10))
print(4*s)

#
print("     尼玛")
print("welcome to china")
sanj=int(input("请输入想要的一边直角*数："))
i=1
while i<=sanj:
    w=1
    if w<=sanj:
        print("*"*i)
        w=w+1
    i=i+1
print()
p=sanj
while p>=0:
    w=1
    if w<=sanj:
        print("*"*p)
        w=w+1
    p=p-1
print()
p=sanj
while p>=0:
    w=1
    if w<=sanj:
        print(" "*(sanj-p)+"*"*p)
        w=w+1
    p=p-1
print()
i=1
while i<=sanj:
    w=1
    if w<=sanj:
        print(" "*(sanj-i)+"*"*i)
        w=w+1
    i=i+1
print()
#
strr=input("请任意输入一段字符串：")
i=0
for w in strr:
    if w== "a":
     i+=1
    print(w)
print("出现ａ的次数为：",i)

#
s=0
for x in range(1,100,2):
    s=s+x
print("for最终计算的结果为：",s)

#
i=1
c=0
while i<=100:
    c=c+i
    i=i+2
print("while最终计算的结果为：",c)

#排列
for x in range(1,100):
    if x*(x+1)%11==8:
        print(x,end=" ")
print()

a=int(input("请输入一个正方形边长整数："))
for s in range(1,(a+1)):
    i=1
    while i<=a:
        print(i,end=" ")
        i+=1
    print()
print("one more:")
for c in range(1,(a+1)):
    for i in range(c,(c+a)):
        print(i,end=" ")
    print() 

#字母转换
i=65
for i in range(65,91):
    print(chr(i),end=" ")
    i+=1
print()
print("once more!")
i=65
for i in range(65,91):
    x=chr(i)
    print(x+x.lower(),end=" ")
    i+=1
print()

#continue
s=0
for i in range(1,101):
    if i%2==0 or i%3==0 or i%5==0 or i%7==0:
        continue
    s=s+i
print("以上所求的式子和为：",s)

#列表创建
l=[]
while True:
    a=input("请输入你想要的字符串：")
    if a=="":
        break
    l=l+[a]
print("L=",l,"\n"+"此列表字符长度为：",len(l)) 

#判断是否为素数
dt=int(input("请随意输入一个数字："))
r=2
for r in (2,dt):
    if dt%r==0:
        print("该数不是素数")
        break
else:
    print("该数是素数")

#圣诞树
s=int(input("请输入想要圣诞树*的高度："))
i=1
w=1
while w<=s:
    print(" "*(s-w)+i*"*")
    i=2*w+1
    w+=1
while s<w<=2*s:    
    print(" "*((2*s-1)//2)+"*")
    w=w+1

#判断是否为水仙花数
for r in range(100,1000):
    y=str(r)
    w=list(y)
    a=int(w[0])
    b=int(w[1])
    c=int(w[2])
    t=r
    if t==a**3+b**3+c**3:
        print(t,"该数为水仙花数")
    else:
        pass

#list
list=[]
i=0
while True:
    l=input("请输入尼玛想要的数：")
    if l=="-1":
        break
    list=list+[l]
    i+=1
print(list)
print("尼玛一共输入了",i,"个有效数")

list1=[]
while True:
    d=int(input("请输入你想要的整数："))
    if d<0:
        break
    list1=list1+[d]
print("当前列表为：",list1)
print("最大的一个数为：",max(list1),"最小的一个数为：",min(list1))
list1.sort(reverse=True)
print("第二大的数为：",list1[1])
list1.remove(min(list1))
print("删除最小的数后：",list1)

begin=int(input("请输入一个整数（较小）:"))
end=int(input("请输入一个整数（较大）:"))
begin=min(begin,end)
end=max(begin,end)
list1=[a for a in range(begin,end) if a%2==0]
print("该偶数列表为：",list1)
list2=[]
while begin<=end:
      if begin%2!=0:
         list2=list2+[begin]
      begin+=1
print("该奇数列表为：",list2)

#100以内的素数
print("welcome to china")
l=[]
for i in range(2,100):
    for n in range(2,i):
       if i%n==0:
          break
    else:
       l=l+[i] 
print("100以内的素数有：",l)

#斐波那契数
l=[1,1]
n=1
while len(l)<=40:
   x=l[-2]+l[-1]
   l=l+[x]
print(l)

#去重复
L=[1,3,2,2,1,6,4,56,67,78,4,4,34,23,23,32,98]
L.sort(reverse=False)
L2=[]
L3=[]
n=0
print(L)
while L[n]<max(L):
    if L[n]==L[(n+1)]:
        L2=L2+[L[n]]
    else:
        L3=L3+[L[n]]
    n=n+1    
print("重复的数有：",L2)
print("去重复后的列表为：",L3+[L[-1]])       
print()

#字典
d={ 1:"春季有１，２，３月",
    2:"夏季有４，５，６月",
    3:"秋季有７，８，９月",
    4:"冬季有１０，１１，１２月"   
}
a = int(input("你想查阅那个季度的月份(1234):"))
print(d[a])
print(d)

#字典
s = input("请输入你想输入的字符串:")
d={}
for ch in s:
    if ch not in d:
         d[ch] = 1
    else:
         d[ch]+= 1
print(d)     
for k,v in d.items():
    print(k,":",v,"次")

#字典
nos = [1001,1002,1005,1008]
names = ['Tom','Jerry','Spike','Tyke']  
d={}
for z in names:
    d[z]=len(z)
print(d)  
f={}
for index in  range(len(nos)):
    print(index,end=" ")
    f[nos[index]]=names[index]
print()
print(f) 
h={}
c=input("请输入:")
c=list(c)
for x in c:
    y=c.count(x)
    h[x]=y
print(h)

#查找
a={"dog":"狗",
   "pig":"猪",
   "cat":"猫",
   "cow":"牛",
   "sheep":"绵羊",
   "snake":"蛇",
   "horse":"马"
}
dictionary=input("请输入你想要查询的动物翻译:")
if dictionary in a:
    print("所查询的单词意思为：",a[dictionary])
else:
    print("没有这个东东")

#学生系统
name=[]
age=[]
score=[]
while True:
    nm=input("请输入姓名:")
    if nm=="":
        break
    else:
        ae=input("请输入年龄:")
        sco=input("请输入成绩:")
        age=age+[ae]
        score=score+[sco]
    name=name+[nm]
print(name)
print(age)
print(score)
print("目前输入完毕！")
d1={"name":name[0],"age":age[0],"score":score[0]}
d2={"name":name[1],"age":age[1],"score":score[1]}
print(d1)
print(d2)
print("+"+"-"*15+"+"+"-"*10+"+"+"-"*20+"+")
print("|"+"name".center(15)+"|"+"age".center(10)+"|"+"score".center(20)+"|")
print("+"+"-"*15+"+"+"-"*10+"+"+"-"*20+"+")
print("|"+name[0].center(15)+"|"+age[0].center(10)+"|"
    +score[0].center(20)+"|")
print("|"+name[1].center(15)+"|"+age[1].center(10)+"|"
    +score[1].center(20)+"|")

#集合
mana={'曹操','刘备','孙权'}
tech={'曹操','刘备','孙权','关羽'}
print('经理有:曹操／刘备／孙权')
print('技术员有:曹操／刘备／孙权／关羽')
print('既是经理又是技术员的有：',mana & tech)
print('是经理但不是技术员的有：',mana-tech)
print('是技术员但不是经理的有：',tech-mana)
print('张飞是经理吗？')
if '张飞' in mana:
    print('   是')
else:
    print('   不是')
print('身兼一职的都有谁？',mana^tech)
print("技术和经理共有多少人？",len(mana|tech))

#函数ｄｅｆ
def p_event(n):
    n=int(n)
    for i in range(n+1):
        if i%2==0:
           print(i,end=" ")
        else:
            continue
    print()
print(p_event(22))

#return
def print_even(a,b):
    return(a+b)
v=print_even    
print('俩个和为：',v(12,34))
def input_number():
    li=[]
    while True:
        a=int(input("来，输入你想要的数字："))
        if a<0:
            break
        li=li+[a]
    return li
v=input_number()
print('最大值为：',max(v),\
        '最小值为：',min(v),\
        '输入的和为：',sum(v))

#def
def fun(n):
    i=1
    sn=0
    while i<=n:
        sn=sn+i**(-1)
        i+=1
    return sn
print('fun(3)=',fun(3))
print('fun(10)=',fun(10))
print()
def fun2(n):
    i=1
    sn=0
    while i<=n:
        sn=sn+(i*(i+1))**(-1)
        i+=1
    return sn
print('fun2(3)=',fun2(3))

#字典
d={}
while True:
    words=input("请输入单词：")
    if words == '':
        break
    trans = input('请输入解释：')
    d[words]=trans
while True:
    words=input('请输入要查找的单词:')
    if words in d:
        print(words+'的解释为：'+d[words])
    else:
        print(words+'单词不存在')

#定义统计中文字符函数
def get_chinese_char_count():
    s=input("请输入中英文混合字符串：")
    num=0
    for i in range(len(s)):
        if ord(s[i])>127:
           num+=1
    return num
print(get_chinese_char_count())

#定义数字是否为素数
def isprime(x):
    if x==1:
        return('1既不是素数，也不是合数,False')
    if x>=2:
        for num in range(2,x):
            if x%num==0:
                return(x,'不是素数,True')
        return(x,'是素数,True')
print(isprime(1))        
print(isprime(5))
print(isprime(9))

#定义范围内数字是否为素数
def prime_m2n(m, n):
    l=[]
    if m==1:
        m=m+1
    for num in range(m,(n+1)):
        for ch in range(2,num):
            if num%ch==0:
                break
        else:
            l=l+[num]
    return(l)
print(prime_m2n(1, 100))
print(prime_m2n(56, 100))

#定义范围内数字素数和
def primes(n):
    l=[]
    if n==1:
        return('１既不是素数，也不是合数')
    for num in range(2,(n+1)):
        for ch in range(2,num):
            if num%ch==0:
                break
        else:
            l=l+[num]
    return(sum(l))
print(primes(10))
print(primes(1))
print(primes(6))

#学生信息的输入
def input_student():
    l=[]
    while True:
        d={}
        na=input('请输入学生姓名：')
        if na=="":
            break
        ag=input('请输入学生年龄：')
        sco=input('请输入学生成绩：')
        d['name']=na
        d['age']=ag
        d['score']=sco
        l.append(d)
    return l
#print(input_student())
L=input_student()

#学生信息的打印
def output_student(L):
    print("+"+"-"*15+"+"+"-"*10+"+"+"-"*20+"+")
    print("|"+"name".center(15)+"|"+"age".center(10)+"|"+"score".center(20)+"|")
    print("+"+"-"*15+"+"+"-"*10+"+"+"-"*20+"+")
    for x in L:
        n=x['name']
        a=x['age']
        s=x['score']
        return('|%s|%s|%s|'%(n.center(15),
                              a.center(10),
                               s.center(20)))
    print("+"+"-"*15+"+"+"-"*10+"+"+"-"*20+"+")
print(output_student(L))

#将俩个数之间的数按照５个一排打印；
a=int(input('请输入第一个数：'))
b=int(input('请输入第二个数：'))
a=min(a,b)
b=max(a,b)
i=1
for ch in range(a,(b+1)):
    if ch==a+5*i:
       print("\n")
       i=i+1
    print(ch,end=' ')
print()

#九九乘法表
i=1
ch=1
for i in range(1,10):
    for ch in range(1,10):
        if i<ch:
            print()
            break
        else:
            print(ch,'×',i,'=',i*ch,end=" ")
print()

#定义我的范围
def myrange(start,stop=None,step=1):
    print(start,stop,step)
    if stop is None:
        stop=start
        start=0 
    l=[]
    i=start
    if step<0:
        while i>stop:
           l.append(i)
           i+=step
    elif step>0:
        while i<stop:
           l.append(i)
           i+=step
    return l
print(myrange(5))
print(myrange(10,0,-2))

#仿造ｍａｘ函数
def mymax(arg1,*args):
    if not args:
        mx=arg1[0]
        for ch in arg1:
            if ch>=mx:
                mx=ch
        return mx
    else:
        mx=arg1
        for ch in args:
            if ch>=mx:
                mx=ch
        return mx
print(mymax([12,23,234,2345,34654,646,757,5]))
print(mymax(1,23,3,342))

# 定义0-a的和
def mysum(a):
    s=0
    for i in range(1,(a+1)):
         s=s+i
    return s
print(mysum(100))

#定义函数
def mysum(x,y):
    return x+y
def mysub(x,y):
    return x-y
def mymul(x,y):
    return x*y
def get_fun(s):
    if s =='加' or s =='+':
        return mysum
    if s =='乘' or s =='*':
        return mymul
    if s =='减' or s =='-':
        return mysub
    else:
        print('输入错误')
def main():
    while True:
        s=input("请先输入计算公式：")
        L=s.split()
        a=int(L[0])
        b=int(L[2])
        print(L,a,b)
        fn=get_fun(L[1])
        print('结果是：',fn(a,b))
main()
def ppp(x,y):
    return x**y
for c in map(ppp,range(1,10),range(9,0,-1)):
    print(c)

#递归应用
def mysum(n):
    if n==1:
        return 10
    return 2+mysum(n-1)
print(mysum(5))

#n!
def n_(x):
    s=1
    for i in range(1,x+1):
        s=s*i
    return s
print(n_(5))

#n!和
def m_(x):
    sn=0　　　#return sum(map(n_,range(1,n+1))
    for ch in range(1,x+1):
        sn=sn+n_(ch)
    return sn
print(m_(3))
print(m_(20))

#打印出列表数字和
l=[[3,5,8],10,[[13,14],15,18],20]
def digui(l):
    for x in l:
        if type(x) is list:
            digui(x)
        else:
            print(x)
print(digui(l))
def print_list(lst):
    s=0
    for x in lst:
        if type(x) == list:
            for ch in x:
                if type(ch) == list:
                    for i in ch:
                        if type(i) == list:
                            s=s+int(str(i))
                        else:
                            s=s+int(str(i))
                else:
                    s=s+int(str(ch))
        else:
            s=s+int(str(x))
    return s
lst=[[12,34,45],34,66]
l=[[3,5,8],10,[[13,14],15,18],20]
print(print_list(lst))
print(print_list(l))

#import time计算你的出生天数
print('程序开始...')
y=int(input('请输入你的出生年：'))
m=int(input('请输入你的出生月：'))
d=int(input('请输入你的出生日：'))
s=time.time()
print('当前秒数为：',s)
v=time.mktime((y,m,d,0,0,0,0,0,0))
print('出生时秒数为：',v)
u=s-v
cc=u //(24*60*60)
ss=time.gmtime(v)
print(ss)
print(cc)

#ｌｉｓｔ转换成字符串
l=[[12,23,23,2344,34],[1001,23,45,67,78,45]]
l1=[str(x) for x in l]
print(l)
print(l1)
print(' '.join(l1))
