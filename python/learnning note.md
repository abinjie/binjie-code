# Python learning note


- [Python learning note](#python-learning-note)
  - [Object oriented programming](#object-oriented-programming)
    - [method 调用方法：](#method-调用方法)
    - [下面的写法有严重的错误](#下面的写法有严重的错误)
    - [继承](#继承)
    - [实例属性和类属性](#实例属性和类属性)


## Object oriented programming
```python
class student:
    def __init__(self,name,score):
        """
        初始化类的属性
        """
        self.name = name
        self.score = score

    def print_score(self):
        """
        类中的函数称为 method(方法)
        """
        print("%s: %s" %(self.name,self.score))
```
### method 调用方法：
```python
binjie = student('binjie',100)
student.print_score(binjie) 
```
若属性前加__ 可以使变量变为私有变量，内部能访问，外部不行
```__score```为私有变量。 
如：

```python
class student:
    def __init__(self,name,score):
        """
        初始化类的属性
        """
        self.name = name
        self.__score = score

    def print_score(self):
        """
        类中的函数称为 method(方法)
        """
        print("%s: %s" %(self.name,self.__score))
```
只能使用（内部函数）```student.print_score(binjie) ```调用

不能使用```print(binjie.__score)```调用

### 下面的写法有严重的错误
```python
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
```
```python
liu = Student("liu",90)

liu.get_name()
Out[40]: 'liu'

liu.__name= 'chaung'

liu.__name
Out[42]: 'chaung'

liu.get_name()
Out[43]: 'liu'
```
设置```__name``` 的时候，虽然没有报错，但实际上这个```__name```变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。内部原有的并没有改变。

### 继承
定义某个新的 class 的时候，可以从现有的 class 继承，新的 class 称为子类 subclass；被继承的class 称为 父类或者超类(base class,Super class)

子类继承了父类所有的属性和方法，同时定义自己的属性和方法
```python
class Animal(object):
    def run(self):
        print('Animal is running...')
```
编写了一个 Animal 的类
之后我们再编写 dog 或者 cat 类的时候，就可以直接从 Animal 之中继承
```python
class Dog(Animal):
    pass

class Cat(Animal):
    pass
```
```python
dog = Dog()

dog.run()
Animal is running...
```
首先 dog 继承了 Animal的 所有功能。
其次，dog 类还可以加入自定义的功能
```python
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
```
```python
dog = Dog()

dog.run()
Dog is running...
```
重写父类,
观察上面，父类 Animal 和子类 Dog 都存在 run() method 的时候，子类的方法会覆盖掉父类。运行的时候，运行的是子类的 run().

### 实例属性和类属性
实例属性和类属性的主要区别在于它们的保存位置和调用对象。实例属性只属于特定的实例对象，而类属性则属于类对象及其所有实例对象。

定义一个类属性之后，属性归类所有，类的所有实例都可以访问。
```python
class Student(object):

  name = 'Student'

  liu = Student()

liu.name
Out[68]: 'Student'

liu.name = 'Chuang'. # 上文的分析 直接给实例绑定属性

liu.name              # 实例属性优先级高于类属性，会屏蔽到类属性
Out[70]: 'Chuang'

del liu.name    #。删除实例属性

liu.name     # 类属性还存在
Out[72]: 'Student'
```
```pyhton
class car(object)
