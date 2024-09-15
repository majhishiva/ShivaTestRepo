# class Test():
#     a=5
#     b=100
#     c=20
# obj1=Test()
# print(obj1.a,obj1.b)

# obj1.a=10
# obj1.b=200
# print(obj1.a,obj1.b)

# obj1.a='shiva'
# obj1.b='kumar'
# obj1.c='majhi'
# print(obj1.a,obj1.b,obj1.c)




# class Test2():
#     name='broadway'
#     subject='python'
    
#     def fun(self):
#         print(f'i am studing python at broadway')
        
# obj1=Test2()
# print(obj1.fun())

class Test2():
    name='broadway'
    subject='python'
    
    # def __str__(self) -> str:
    #     return "this is test class"
    
    def fun(self):
        print(f'i am studing {self.subject} at {self.name}')
        
        
    def __str__(self) -> str:
        return "this is test class"
        
# obj1=Test2()
# print(obj1)
# print(obj1.fun())


# class test3():
    
    
#     def __init__(self,a,b) -> None:
#         print('hi i am here')
#         self.a=a
#         self.b=b
        
#     def test(self):
#         return self.a
    
# obj2=test3('hello','world')
# print(obj2.test())    
    
    
class Math:
    
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
        
    def add(self):
        return self.a + self.b
    
    def diff(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b

obj = Math(6, 7)
print(obj.add())
print(obj.diff())
print(obj.mul())


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
        
# class Parent():
#     def add(self):
#         return'hello '
#     def diff(self):
#         return 'world'
#     def _init_(self):
#         self.a=22
# class Child(Parent):
#     def mul(self):
#         return 'shiva'
#     def div(self):
#         return 'majhi'
#     def _init_(self):
#         self.d=12
#         super()._init_(self)
    
# obj = Child()
# print(obj.add())
# print(obj.diff())
# print(obj.)




