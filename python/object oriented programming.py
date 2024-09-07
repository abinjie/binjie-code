# class student:
#     def __init__(self,name,score):
#         """
#         初始化类的属性
#         """
#         self.name = name
#         self.__score = score

#     def print_score(self):
#         """
#         类中的函数称为 method(方法)
#         """
#         print("%s: %s" %(self.name,self.__score))
    
#     def set_score(self,score):
#         if 0 <= score <=100:
#             self.__score = score
#         else:
#             raise ValueError("score不在范围内")

# binjie = student('binjie',100)
# student.print_score(binjie) #method 调用方法
# #属性前加__ 可以使变量变为私有变量，内部能访问，外部不行
# student.set_score(binjie,90)
# student.print_score(binjie)

# class Animal:
#     def run(self):
#         print("Animal is running...")

# class Dog(Animal):
#     pass

# dog = Dog()
# dog.run()
# a = list()
# b = Animal()
# c = Dog()
# print(isinstance(c,Animal))


