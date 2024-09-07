#例2.4.2 逆序字符串

# s=input()
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end='')


# s = input()
# s = list(s)
# n = len(s)
# for i in range(n//2):#8//2=4 7//2=3
#     s[i],s[n-1-i]=s[n-1-i],s[i]
# res = "".join(s)
# print(res)

# s=list(input())
# s.reverse()
# s="".join(s)
# print(s)

# n=input()
# m=n[3]+n[2]+n[1]+n[0]
# print(m)

# a,b=map(float,input().split())
# fa=a-int(a)
# fb=b-int(b)
# c=int(b)+fa
# d=int(a)+fb
# print("%.2f %.2f"%(c,d))

# n=input()
# c=len(n)
# print(c)

# a,b=map(int,input().split())
# if a>b:
#     print(a)
# else:
#     print(b)

# n=int(input())
# a=list(map(int,input().split()))
# max=a[0]
# for i in range(1,n):
#     if a[i]>max:
#         max=a[i]
# print(max)

# z=0
# p=0
# n=0
# a=int(input())
# b=list(map(int,input().split()))
# for i in b:
#     if i==0:
#         z+=1
#     if i>0:
#         p+=1
#     if i<0:
#         n+=1
# print("z={} p={} n={}".format(z,p,n))

# k=int(input())
# s=1
# n=1

# while(s<=k):
#    n+=1
#    s+=1/n

# print(n)
    
# a=list(map(int,input().split()))
# b=int(input())
# b+=30
# n=0
# for i in a:
#     if(i<=b):
#         n+=1
# print(n)

# l,m=map(int,input().split())
# thetree=[0 for i in range(l+1)]
# for i in range(m):
#     num=input().split()
#     start=int(num[0])
#     end=int(num[1])
#     for i in range(start,end):
#         thetree[i]=1
# treenumber=thetree.count(0)
# print(treenumber)

# import math
# a=int(input())
# b=[]
# for i in range(1,sqrt(a)):
#     if(a%i==0):
#         b.append(i)
# c=max(b)
# print(c)

# day=0
# max=0
# for i in range(7):
#     a,b=map(int,input().split())
#     s=a+b
#     if(s>max and a+b>8):
#         max=s
#         day=i

# print(day)

# n,k=map(int,input().split())
# tou=n
# while(tou>=k):
#     s=tou/k
#     tou=int(s)
#     n=int(s)+n
# print(n)

# n,k=map(int,input().split())
# ans=0
# d=0
# while(n>0):
#     ans+=1
#     n-=1
#     d+=1
#     if(d==k):
#         d=0
#         n+=1
# print(ans)

# k=int(input())
# d=0
# for i in range(10000,30001):
#     b1=int(i/100)
#     b2=int((i/10)%1000)
#     b3=int(i%1000)
#     if(b1%k==0 and b2%k==0 and b3%k==0):
#         print(i)
#         d=1
# if(d==0):
#     print("No")

# try:
#     while True:
#         cnt=0
#         n=int(input())
#         print(n,end=':')
#         for i in range(6,n+1):
#             sum=0
#             for j in range(1,i//2+1):
#                 if(i%j==0):
#                     sum+=j
#             if sum==i:
#                     cnt+=1
#                     print('',i,end='')
#         if cnt==0:
#             print("NULL")
#         else:
#             print()
# except EOFError:pass

# dic = {'i':1,
#        'v':5,
#        'x':10,
#        'l':50,
#        'c':100,
#        'd':500,
#        'm':1000}
# s="iv"
# print(dic[s[1]])
# print(len(s))
# num=0
# last_num=0
# for i in range(len(s)):
#     if dic[s[i]] <=last_num:
#         num = num + dic[s[i]]
#     else:
#         num = num + dic[s[i]] - 2*last_num
#     last_num = dic[s[i]]
# print(num)

# nums = [1,2,6,7,8]
# target=9
# dic = {}
# for i in range(len(nums)):
#     if target - nums[i] not in dic:
#         dic[nums[i]] = i
#     else:
#         print( [dic[target -nums[i]],i] )

# numlist=[1,2,5,7,8,9]
# def numadder(numlist):
#     if len(numlist) == 1:
#         return numlist[0]
#     else:
#         return numlist[0] + numadder(numlist[1:])
# print(numadder(numlist))
# bj='name'
# dict = {}
# dict[bj]=1
# print(dict)

# print("{:-^30b}".format(123))
# dict = {"小明":13,"小妹":10}
# print(dict[0]) #字典不能通过整数索引

# a = 1
# b = 5
# if a>b:max=a
# print(max)


# import numpy as np
# s = np.array(10)
# print(s)



# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# sum = 0
# for i in range(2,21,2):
#     sum+=factorial(i)
# print(sum)