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



    



