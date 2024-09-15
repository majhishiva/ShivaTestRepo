def add():
    a = 5+5
    lst = []
    for i in range(1,5):
        lst.append(i)
    return lst

print(add())


### arguments

# def myinfo(name,age):
#     print(f'my name is {name} and age is {age}')
    
# myinfo('shiva',26)



# def kantipur(title,content,author):
#     print(title)
#     print(content)
#     print(author)
    
# print(kantipur('war','sdfafdd','shiva'))


def kantipur(title,content,author):
    return title,content,author

print(kantipur('war','adfadf','shiva'))


def test(a,b,c,):
    print("hello")
    
test(1,2,3)



def keyword_arg(surname,name):
    print(name,surname)
    
keyword_arg(name = "shiva",surname = 'majhi')


def test2(*args):
    total = 0
    for i in args:
        total = total + i
    return(total)

a = test2(1,2,3,4,5,6,7,8,9)
print(a)

    



def sum(a,b,c):
    sum = a + b + c
    print(f"sum is: {sum}")
    
sum(1,2,3)


def test3(**data):
    print(data)
    test = list(data)
    return(test)
    
a = test3(name = 'shiva', surname = 'majhi', a = 3)
print(a)

    

def hello(*args,**kwargs):
    print("positional",args)
    print("kwargs",kwargs)
    return args, kwargs
print(hello(1,2,2,3,name='hello'))


###Recursion

def test5():
    def nested():
        print('hello')
    print('python')
    nested()
test5()

