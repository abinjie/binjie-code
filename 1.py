import numpy as np
import matplotlib.pyplot as plt
#1
# the_array = np.array([49,7,44,27,13,35,71])#创建一个数组
# an_array = np.where(the_array > 30,0, the_array)
# print(an_array)

#2
# the_array = np.array([49,7,44,27,13,35])
# an_array =  np.where(the_array > 40, the_array + 5, the_array)
# print(an_array)

#3
# the_array = np.array([49,7,44,27,13,35,71])
# an_array = np.asarray([0 if val < 25 else 1 for val in the_array])
# print(an_array)

#4
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr.ndim)
# arr = np.array([[1,1,1,0],[0,5,0,1],[2,1,3,10]])
# print(arr.ndim)
# arr = np.array([[[1,1,1,0],[0,5,0,1],[2,1,3,10]]])
# print(arr.ndim)

#5
# the_array = np.array([1,2,3,4,5,6,7,8,9])
# filter_arr = np.logical_and(np.greater(the_array, 3), np.less(the_array, 8))
# print(the_array[filter_arr])

#6
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(4,3)
# print(newarr)
# column_sums = newarr[:,0].sum()
# print(column_sums)

#7
# the_arr = np.array([[0,1,2,3,5,6,7,8],
#                     [4,5,6,7,5,3,2,5],
#                     [8,9,10,11,4,5,3,5]])
# print(the_arr[:,1:5])

#8
# the_array = np.array([[1,2],[3,4]])
# print(the_array)
# the_array = np.delete(the_array,[1,2])
# print(the_array)

#1
# x = [1,2,3,4,5,6]
# y = [3,5,1,7,9,12]
# plt.plot(x,y)
# plt.show()

#2
# x = [1,2,3,4,5]
# y1 = [1, 2, 3, 4, 5]
# y2 = [2, 4, 6, 8, 10]
# y3 = [3, 6, 9, 12, 15]
# plt.plot(x, y1, color="g",linestyle="-",marker="o",markerfacecolor="g",markersize=3)
# plt.plot(x, y2, color="r",linestyle=":",marker="D",markerfacecolor="r",markersize=3)
# plt.plot(x, y3, color="b",linestyle="-.",marker="s",markerfacecolor="b",markersize=3)
# plt.show()

#3
# N = 10
# y = np.zeros(N)
# x1 = np.linspace(0, 10, N, endpoint=True)
# x2 = np.linspace(0, 10, N, endpoint=False)
# plt.plot(x1, y, 'or')
# plt.plot(x2, y + 0.5, '*b')
# plt.ylim([-0.5, 1])
# plt.show()

#4
# x = np.linspace(0,2*np.pi, 100)
# y = np.sin(x)
# plt.plot(x, y,c='r',ls="-", lw=3, label="sin")
# plt.legend()
# plt.show()

#5
# t=np.arange(12)
# x=t.reshape((4,3))
# y=np.random.randint(2,9,size=[4,3])
# plt.plot(x,y)
# plt.show()

#6
# x = [1,2,3,4,5,6]
# y = [3,5,1,7,9,12]
# plt.plot(x,y)
# x = [1,2,3]
# y = [2.0,3.5,4.6]
# plt.plot(x,y)
# plt.show()

# Example 7 请说明下列代码的作用
# x = [1,2,3,4,5,6]
# y = [3,5,1,7,9,12]
# figure1 = plt.figure()
# plt.plot(x,y)
# x = [1,2,3]
# y = [2.0,3.5,4.6]
# figure2 = plt.figure()
# plt.plot(x,y)
# plt.show()

# Example 8 请说明下列代码的作用
# x = [1,2,3,4,5,6]
# y = [3,5,1,7,9,12]
# figure = plt.figure()
# axes1 = figure.add_subplot(2,1,1)
# plt.plot(x,y)
# x = [1,2,3]
# y = [2.0,3.5,4.6]
# axes2 = figure.add_subplot(2,1,2)
# plt.plot(x,y)
# plt.show()

# # Example 9 请说明下列代码的作用
# figure = plt.figure()
# axes1 = figure.add_subplot(1,2,1)
# axes2 = figure.add_subplot(1,2,2)
# x = [1,2,3,4,5,6]
# y = [3,5,1,7,9,12]
# axes1.plot(x,y)
# axes2.set_title('Title')
# axes2.set_xlabel('X')
# axes2.set_ylabel('Y')
# #设置坐标轴范围
# axes2.set_xlim(0,5)
# axes2.set_ylim(0,10)
# #设置绘制的线型和颜色及标注内容
# plot1=axes2.plot(x,y,marker='o',color='r',label='1')
# plot2=axes2.plot(x,y,linestyle='--',color='b',label='2')
# axes2.legend(loc='upper left') #在指定位置显示标注
# #显示网格绘制子图2
# axes2.plot(x,y)
# plt.savefig('tu1.jpg',dpi=300) #保存图形
# plt.show()

# Example 10 请说明下列代码的作图类型及特点
# import numpy as np
# import matplotlib.pyplot as plt
# data = np.random.randn(1000)
# plt.hist(data, bins=30)
# plt.show()

# Example 11 请说明下列代码的作图类型及特点
import matplotlib.pyplot as plt
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Example 12 请说明下列代码的作图类型及特点(散点图)
# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.scatter(x, y)
# plt.show()


# arr = np.arange(0,18)
# new_arr = arr.reshape(3,6)
# print(new_arr)