####Recursion

# def fun():
#     for i in range(1,5):
#         print(i)
#     fun()
# fun()

## factorial using recursion

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n * fact(n-1)
# print(fact(5))


# a = [1,2,[4,1[1,[1,[1[4]]]]]]

# a = isinstance(a,list)
# print(a)


n = int(input("Please enter the number:"))
def total(n):
    for i in range(n):
        sum = n + total(n-1)
        return sum
    print(total(5))


