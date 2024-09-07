# sum = 0
# m =10
# while m > 0:
#     sum = sum + m
#     m = m - 1
# print(sum)

# str= 'python'
# for s in str:
#     if s=='o':
#         break
#     print(s)

# str ='python'
# for s in str:
#     if s =='o':
#         continue
#     print(s)

# x = 15
# y = 2
# s = pow(x,y)
# print(s)

# import random
# x=random.uniform(1,10)
# print(x)

# str = 'Python'
# print('str[0] str][-6]=',str [0],str[-6])
# print('str[5] str[-1]=',str [5],str[-1])


# str = 'Python'
# print(str[:3])
# print(str[3:])
# print(str[:])

# l= [1024,0.5,'python']
# l[1]=5
# print(l)
# l.append('hellow')
# del l[0]
# print(l)

# print('1[0]  ',l[0])
# print('1[1:]',l[1:])

# t = (1024,0.5,'python')
# print(t)
# t = (384,322)
# print(t)

# d ={'name' : '小明','age':'18'}
# print(len(d))
# print(d.get('age'))



# s = set(['a','b','c'])
# s.remove('a')
# print(len(s))
# print(s)

# import time
# t = time.localtime()
# print(t)

# import datetime
# print(datetime.date.today())

# import math

# r = 3
# print('半径为3的圆的面积:%.2f' %(math.pi*r**2))

# from math import pi
# r = 3
# s = r**2*pi
# print(s)


# import math
# print(math.pi)
# print(math.sin(1.6))

#print('五福临门','十全十美',sep='*')

# height = 191
# print('小明的身高:%d'%height)
# print('{}今年{}岁了'.format("王小明",18))

# num = 1.82743
# print("num={:.3f}".format(num))

# num1=9.2344
# print("num1={:.3f}".format(num1))
# num2=524.12344
# print("num2={:.3f}".format(num2))
# company="ai company"
# year=18
# print("{}以成立{}年".format(company,year))
# print("{0}已成立{1}年".format(company,year))

# age = input("请输入你的年龄:")
# print("你的年龄为:\n%s"%age)

# price=int(input("请输入产品价格："))
# a=int(input("涨幅:"))
# float(a)
# result=(a*0.01+1)*price
# print("最终价格:%.2f"%result)

# num=int(input("请输入金额:"))
# hundred=num//100
# fifty=(num-hundred*100)//50
# ten=(num-hundred*100-fifty*50)//10
# one=(num-hundred*100-fifty*50-ten*10)
# print("100有%d张,50有%d张,10有%d张,1有%d张"%(hundred,fifty,ten,one))

# score=int(input("分数:"))
# if 70>score>=60:
#     print("及格")
# if score>=70:
#     print("良好")
# else:
#     print("不及格")


# F=float(input("请输入华氏温度:"))
# C=5/9*(F-32)
# print("华氏温度%5.1f转换为摄氏温度为%3.1f"%(F,C))



# x=float(input("输入一个数字:"))
# if(x%2)==0:
#     print("偶数")
# else:
#     print("奇数")

# score=float(input("请输入分数："))
# if 85>score>=60:
#     print("及格")
# elif score>=85:
#     print("优秀")
# else:
#     print("不及格")

# print("请输入年份:")
# year=int(input())
# if year%4==0 and year%100 !=0:
#     print("%d年为闰年"%year)
# elif year%400==0:
#     print("%d年为闰年"%year)
# else:
#     print("%d年不是闰年"% year)

# x="abcdefghijklmnopqrstuvwxyz"
# for i in x:
#     print(i,end='')

# x=['tycx','hyx','lx','cyh']
# print("我有几个好朋友：")
# for friend in x:
#     print(friend.title()+"是我的好朋友")

# n=int(input("请输入数字："))
# for i in range(n):
#     print("$",end=" ")

# product=1
# for i in range(1,11):#range生成了10个数，i要取10次
#     product*=i
# print("product:%d"%product)i

# sum = 0
# n1 = 1
# n=int(input("请输入任意一个整数："))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         n1*=j
#     sum+=n1;
#     n1=1
# print("{0}!+{1}!+{2}!+...+{3}!=%d".format(n-(n-1),n-(n-2),n-(n-3),n)%sum)


# total=0
# money=-1
# while money!=0:
#     money=float(input("请输入金额："))
#     total+=money
#     print("累计:%.2f" % total)

# print("总金额=%.2f"% total)

# print("求两数的最大公约数")
# print("请输入两个正整数：")
# Num1=int(input())
# Num2=int(input())
# if Num1<Num2:
#     tmpnum=Num1
#     Num1=Num2
#     Num2=tmpnum
# while Num2!=0:
#     tmpnum=Num1%Num2
#     Num1=Num2
#     Num2=tmpnum
# print("最大公因数为：%d"%Num1)

# for x in range(1,10):
#     if x==5:
#         break
#     print(x,end=' ')

# for i in range(1,10):
#     for j in range(1,10):
#         print('{0}*{1}={2:2d}'.format(i,j,i*j),sep='\t',end=' ')
#         if j>7:
#             break
#     print('\n-----------------------\n')

# a=int(input("输入数字："))
# for b in range(a):
#     for c in range(b+1):
#         print(c,end='')
#     print()

# i = 1
# password=3388
# while i<=3:
#     a=int(input("请输入密码:"))
#     if a==password:
#         print("密码正确")
#         break
#     else:
#         print("密码错误请重新输入")
#         i+=1
#         continue
# if i>3:
#     print("密码错误超过三次,取消登录")

# def blessings():
#     print("一元复始,万象更新!")
# blessings()
# def blessings(str1):
#     print(str1)
# blessings('恭贺新禧,财源滚滚')

# def func(a,b):
#     x=a*b
#     print(x)
# func(4,3)

# def factorial(*arg):
#     product=1
#     for n in arg:
#         product*=n
#     return product
# ans1 = factorial(5)
# ans2 = factorial(2,3)
# ans3 = factorial(2,5,4)
# print(ans1,ans2,ans3)

# def payment():
#     price=float(input("产品单价:"))
#     num=int(input("产品数量:"))
#     money=price*num*0.35
#     return price*num,money
# x,y=payment()
# print("总销售额：{0}\n奖金:{1}".format(x,y))

# a=lambda x,y:2*x+4*y
# print(a(3,4))

# def fun():
#     var=100
#     print(f"{locals()}")
# fun()
# print({'var'in locals()})
# a =10
# name ='binjie'
# print(globals())

# a=int(input("请输入一个数字"))
# f=1
# for i in range(1,a+1):
#     f*=i
# print(f)

# def factorial(n):
#     if n>0:
#         return n*factorial(n-1)
#     else:
#         return 1
# print(factorial(5))


# import math
# print("math.pow(3,4)=",math.pow(3,4))

# import math as m
# print("floor(10.6)=",m.floor(10.6))

# import random as r
# for j in range(6):
#     print(r.randint(1,42),end=' ')
# print()
# for j in range(3):
#     print(r.uniform(1,10),end=', ')


# import this

# class person:
#     pass
# p1 = person()
# print("p1是person类的对象:",isinstance(p1,person))
# print(p1)

# class person:
#     def __init__(self,name,gender,age):
#         self.name=name
#         self.gender=gender
#         self.age=age
#         #print(f'一个名为{self.name}的人类对象诞生了')
# Tom=person('Tom','男生',16)
# Rose=person('Rose','female',17)
# Jack=person('Jack','male',30)
# print(f"大家好，我叫{Tom.name},今年{Tom.age}岁了，我是{Tom.gender}")

# class person:
#     def __init__(self,name,gender,age):
#         self.name=name
#         self.gender=gender
#         self.age=age
#         print(f'一个名为{self.name}的人类对象产生了')
#     def eat(self,food):
#         print(f'{self.name}在吃{food}')
#     def run(self):
#         print(f'{self.name}在跑')
# p1=person('Tom','男',19)
# p1.run()
# p1.eat("牛奶巧克力")
# print(getattr(p1,"sex","属性不存在"))
# print(hasattr(p1,'birthday'))

# class person:
#     def __init__(self,name,gender,age):
#         self.__name=name
#         self.__gender=gender
#         self.__age=age
#         print(f'一个名为{self.__name}的人类对象产生了')
#     def say(self):
#         print(f'我是{self.__name}')
# class student(person):
#     def __init__(self,name,gender,age,num):
#         person. __init__(self,name,gender,age)
#         self.__num=num
#         print(f'一个学号为{self.__num}的学生对象诞生了')
#     def say(self):
#         super().say()
#         print(f'我的学号是{self.__num}')
# s1=student("binjie","男",19,23384201)
# s1.say()

# import tkinter as tk
# for x in range(3):#决定有几个窗口
#     top = tk.Tk()
#     top.title("第一个tkinter窗口")
#     top.mainloop()

# import tkinter as tk
# top=tk.Tk()
# top.geometry('300x200')
# top.title("第一个tkinter窗口")
# btn=tk.Button(top,text="一个按钮")
# btn.pack()
# top.mainloop()

# a=int(input("请输入起始数："))
# b=int(input("请输入中止数："))
# c=0
# d=0
# temp=0


# for x in range(a,b+1):
#     temp=x
#     sum=0
#     n=0
#     while(x!=0):
#         x=x//10
#         n+=1
#     x=temp
#     while(x!=0):
#         c=x%10
#         sum=sum+pow(c,n)
#         x=x//10
#     x=temp
#     if(x==sum):
#         print(sum)

# class Wage:
#     def __init__(self,h=80):
#         self.__hour=h

#     def gethour(self):
#         return self.__hour
    
#     def pay(self):
#         return hour_fee*self.__hour
    
# hour_fee=200
# obj1=Wage(100)
# print("每小时基本工资:",hour_fee,'元')
# print("总共工作小时：",obj1.gethour())
# print("要付给这位员工的薪水:",obj1.pay(),"元")

# class mobilephone:
#     def touch(self):
#         print("我能提供屏幕触控操作的功能")
    
# class HTC(mobilephone):
#     def touch(self):
#         mobilephone.touch(self)
#         print("我也能提供多点触控的操作方式")

# u11=HTC()
# u11.touch()

# class Weekday():
#     def display(self,pay):
#         self.price=pay
#         print("欢迎来购物")
#         print("购买总金额{:,}元".format(self.price))

# class Holiday(Weekday):
#     def display(self,pay):
#         super().display(pay)
#         if self.price>=15000:
#             self.price*=0.8
#         else:
#             self.price
#         print("8折{:,}元".format(self.price))

# monday=Weekday()
# monday.display(25000)

# Christmas=Holiday()
# Christmas.display(18000)

# class Animal():
#     def __init__(self):
#         print("我属于动物类")

# class Human(Animal):
#     def __init__(self):
#         super().__init__()
#         print("我也属于人类")

# man=Human("黄种人")

# class Animal:  
#     def __init__(self):  
#         print("我属于动物类")  
  
# class Human(Animal):  
#     def __init__(self,name):  
#         super().__init__()  
#         print("我也属于人类")  
  
# man = Human('huang')  # 创建一个Human对象，不会传递任何参数

# class Book:
#     def __init__(self,name,price,type):
#         print("这是{:,}".format(name))

# name='钢铁是怎样炼成的'

# import tkinter as tk
# win=tk.Tk()
# win.geometry("400x400")
# win.title("这是我的第一个用python写的窗口")
# win.mainloop()

# import tkinter as tk
# win=tk.Tk()
# win.geometry("600x100")
# win.title("pack的布局示范")

# plus=tk.Button(win,width=20,text="加法示例")
# plus.pack(side="left")

# minus=tk.Button(win,width=20,text="减法示例")
# minus.pack(side="left")

# multiple=tk.Button(win,width=20,text="乘法示例")
# multiple.pack(side="left")

# divide=tk.Button(win,width=20,text="除法示例")
# divide.pack(side="left")

# win.mainloop()

# def bless():
#     btnvar.set("心想事成,天天开心")

# def changecolor():
#     btn2.config(bg="green")

# import tkinter as tk
# win=tk.Tk()
# win.title("按钮控件(Button)")

# btnvar=tk.StringVar()
# btn1=tk.Button(win,textvariable=btnvar,command=bless)
# btnvar.set("单机我会有祝福语")
# btn1.pack(padx=20,pady=10)

# btn2=tk.Button(win,text="单击我会改变按钮背景颜色",command=changecolor)
# btn2.pack(padx=20,pady=10)

# win.mainloop()


#消息框
# from tkinter import*
# from tkinter import messagebox
# win=Tk()
# win.title('消息框控件(messagebok)')
# win.geometry('300x120+20+50')

# def answer():
#     messagebox.showerror('显示类消息框控件',
#                          '这是messagebox.showerror的消息框控件')
    
# def callback():
#     messagebox.askyesno('询问类消息框控件',
#                         '这是messagebox.askyesno的消息框控件')
    
# Button(win,text='显示询问消息框控件的外观',command=
#        callback).pack(side='left',padx=10)
# Button(win,text='显示错误消息框控件的外观',command=
#        answer).pack(side='left')
# win.mainloop()

# n=int(input("计算到第几项:"))
# a=0
# b=1
# for i in range(n):
#     print(b)
#     a,b=b,a+b

# import math 
# print("math.gcd(72,48)=",math.gcd(72,48))

# with open("phrase.txt","r")as file1:
#     for line in file1:
#         print(line,end="")

# import os
# import sys
# b=0
# for i in range(1,2022):
#     a=str(i).count("2")
#     b+=a
# print(b)

# a=[1,2,3,4,5,6,7,8,9,'w','w',]
# for i in range(len(a)):
#     print(i+1)

# n=int(input())
# s=list(map(int,input().split()))
# max_num=0
# for i in range(n-1):
#   for j in range(i+1,n):
#     max_num=max(max_num,abs(j-i)+abs(s[j]-s[i]))
# print(max_num)

# import datetime
# start =datetime.date(1900,1,1)
# end = datetime.date(9999,12,31)

# def get_num(n):
#     return sum([int(i) for i in str(n)])
# cnt = 0
# while start < end:
#     y,m,d = start.year,start.month,start.day
#     if get_num(y) == get_num(m) + get_num(d):
#         cnt+=1
#     start+=datetime.timedelta(days=1)
# print(cnt)
# f=float(input())
# c=5*(f-32)/9
# print("%.2f" %c)
# f=float(input())
# c=5*(f-32)/9
# print("%.2f"%c)
# print('c={0:.2f}'.format(c))


# ans=0
# for i in range(1,2021):
#     ans+=(str(i).count("2"))
# print(ans)

# try:
#     while True:
#         a,b=input().split()
#         c=int(a)+int(b)
#         print(c)
# except EOFError:pass

# a,b=input().split()
# c=int(a)*int(b)
# print("%s*%s=%s"%(a,b,c))

# a,b=input().split()
# a=int(a)
# b=int(b)
# c=a*b
# print("{0}*{1}={2}".format(a,b,c))

# a,b=input().split(",")
# a=int(a)
# b=int(b)
# c=a*b
# print("%d*%d=%d"%(a,b,c))
# a=int(input())
# b=len(a)
# c=a//10*b

# def sum_digit():
#     a=0
#     n=input()
#     for i in str(n):
#         i=int(i)
#         a+=i
#     return a
# print(sum_digit())
# a=1
# b=2
# a,b=b,a
# print(a,b,sep=' ')
# m,n=input().split()
# m=int(m)
# n=int(n)
# s=input()
# ans=s[m:m+n]
# print(ans)

# s=input()
# s=list(s)
# n=len(s)
# for i in range(n//2):
#     s[i],s[n-1-i]=s[n-1-i],s[i]
# res="".join(s)
# print(res)

# a,b=map(int,input().split())
# c=a*b
# print(c)

# def last_vowel(s):  
#     vowels = ['a', 'e', 'i', 'o', 'u']  
#     for i in range(len(s)-1, -1, -1):  
#         if s[i] in vowels:  
#             return s[i]  
#     return None  
  
# s = input()  
# print(last_vowel(s))

# def convert(n):  
#     # 如果n是0，返回0  
#     if n == 0:  
#         return 0  
#     # 如果n小于0，返回错误  
#     if n < 0:  
#         return "Error: Input should be a non-negative integer."  
#     # 计算n的所有非零数字的乘积  
#     product = 1  
#     while n > 0:  
#         digit = n % 10  
#         if digit != 0:  
#             product *= digit  
#         n //= 10  
#     # 如果product小于10，返回product  
#     if product < 10:  
#         return product  
#     # 如果product大于等于10，进行下一次转换  
#     else:  
#         return convert(product)  
  
# # 获取用户输入的整数  
# n = int(input("请输入一个整数："))  
# # 进行转换并输出结果，直到结果小于10为止  
# result = convert(n)  
# while result != None:  
#     print(result)  
#     result = convert(result)
#约数
# import math  
  
# def count_divisors(n):  
#     count = 0  
#     for i in range(1, int(math.sqrt(n)) + 1):  
#         if n % i == 0:  
#             if i == (n / i):  
#                 count += 1  
#             else:  
#                 count += 2  
#     return count  

# print(count_divisors(777714))

# def convert_number(n):  
#     while n >= 10:  
#         digits = [int(d) for d in str(n) if d != '0']  
#         n = int(''.join(map(str, digits)) * len(digits))  
#         print(n)  
          
# n = int(input())  
# convert_number(n)


# f =lambda :"Hello world!"
# print(f())

# numbers= [1,2,3,4,5]
# squared = list(map(lambda x:x**2,numbers))
# print(squared)

# from functools import reduce
# numbers = [1,2,3,4,5]
# product = (reduce(lambda x,y:x*y,numbers))
# print(product)


