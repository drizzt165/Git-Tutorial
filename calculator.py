def add(x,y):
    return(x+y)

def subtract(x,y):
    return(x-y)

def divide(x,y):
    return(x/y)

def multiply(x,y):
    return(x*y)

x = input("Enter a number: ")
y = input("Enter another number: ")
print(f'{x} * {y} = {multiply(x,y)}')