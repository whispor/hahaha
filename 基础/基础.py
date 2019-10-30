# names = ("haha", "heihie", "hoho", "hehe")
# ages = (18, 23, 29, 10)
# jobs = ("老师", "程序员", "公务员")
# for name, age, job in zip(names, ages, jobs):
#     print("{0}——{1}——{2}".format(name,age,job))

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# result = factorial(int(5))
# print(result)

# class A:
#     def say(self):
#         print("A:",self)

# class B(A):
#     def say(self):
#         super().say()
#         print("B:",self)

# B().say()


#多态
# class Man:
#     def eat(self):
#         print("饿了，吃饭了！")

# class Chinese(Man):
#     def eat(self):
#         print("中国人用筷子吃饭")

# class English(Man):
#     def eat(self):
#         print("英国人用叉子吃饭")

# class Indian(Man):
#     def eat(self):
#         print("印度人用右手吃饭")

# def manEat(m):
#     if isinstance(m,Man):
#         m.eat()
#     else:
#         print("不能吃饭")

# manEat(Chinese())
# manEat(English)


# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def __add__(self, other):
#         if isinstance(other, Person):
#             return "{0}——{1}".format(self.name, other.name)
#         else:
#             return "不是同类对象，不能相加"

#     def __mul__(self, other):
#         if isinstance(other, int):
#             return self.name*other
#         else:
#             return "不是同类对象，不能相乘"

# p1 = Person("haha")
# p2 = Person("jojo")

# x = p1+p2
# print(x)
# print(p2*30)

# #使用继承实现代码的复用
# class A1:
#     def say_a1(self):
#         print("a1,a1,a1")

# class B1(A1):
#     pass

# b1 = B1()
# b1.say_a1()

# #使用组合实现代码的复用
# class A2:
#     def say_a2(self):
#         print("a2,a2,a2")

# class B2:
#     def __init__(self,a):
#         self.a = a

# a2 = A2()
# b2 = B2(a2)
# b2.a.say_a2()

import copy

class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calculate(self):
        print("算你个12345")
        print("cpu对象:", self)

class Screen:
    def show(self):
        print("显示一个好看的画面，亮瞎你的狗眼")
        print("screen对象：",self)

c1 = CPU()
c2 = c1
print(c1)
print(c2)
print("测试浅复制")

s1 = Screen()
m1 = MobilePhone(c1,s1)
m2 = copy.copy(m1)
print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)

print("测试深复制")
m3 = copy.deepcopy(m1)
print(m1, m1.cpu, m1.screen)
print(m3, m3.cpu, m3.screen)