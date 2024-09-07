# Stack 判断括号
# from functions import Stack

# def parChecker(symbolString):
#     s = Stack()
#     balanced=True
#     index = 0
#     while index<len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol  =="(":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced=False
#             else:
#                 s.pop()

#         index = index+1
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False
    

# print(parChecker("((()))"))

#热土豆问题
# from functions import Queue
# def hotPotato(namelist,num):
#     simqueue =Queue()
#     for name in namelist:
#         simqueue.enqueue(name)
    
#     while simqueue.size()>1:
#         for i in range(num):
#             simqueue.enqueue(simqueue.dequeue())

#         simqueue.dequeue()

#     return simqueue.dequeue()


#Printer tesk

# class Printer:
#     def __init__(self,ppm):
#         self.pagerate = ppm
#         self.currentTask = None
#         self.timeRemaining = 0

#     def tick(self):
#         if self.currentTask != None:
#             self.timeRemaining = self.timeRemaining-1
#             if self.timeRemaining <= 0:
#                 self.currentTask = None

#     def busy(self):
#         if self.currentTask != None:
#             return True
#         else:
#             return False
        
#     def startNext(self,newtask):
#         self.currentTask = newtask
#         self.timeRemaining = newtask.getPages() \
#                             *60/self.pagerate
        

# import random
# class Task:
#     def __init__(self,time):
#         self.timestamp = time
#         self.pages = random.randrange(1,21)


#     def getStamp(self):
#         return self.timestamp
    
#     def getPages(self):
#         return self.pages
    
#     def waitTime(self,currenttime):
#         return currenttime - self.timestamp       
    
# from functions import Queue
# import random

# def simulation(numSeconds, pagesPerMinute):

#     labprinter = Printer(pagesPerMinute)
#     printQueue = Queue()
#     waitingtimes = []

#     for currentSecond in range(numSeconds):
        
#         if newPrintTask():
#             task = Task(currentSecond)
#             printQueue.enqueue(task)

#         if(not labprinter.busy()) and \
#                             (not printQueue.isEmpty()):
#             nexttask = printQueue.dequeue()
#             waitingtimes.append(nexttask.waitTime(currentSecond))

#         labprinter.tick()

#     averageWait=sum(waitingtimes)/len(waitingtimes)
#     print("Average Wait %6.2f secs %3d tasks remaining."\
#           %(averageWait,printQueue.size()))
    
# def newPrintTask():
#     num = random.randrange(1,181)
#     if num == 180:
#         return True
#     else:
#         return False
        
# for i in range(10):
#     simulation(3600,  5)



from functions import Deque
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual
print(palchecker("DOGOD"))