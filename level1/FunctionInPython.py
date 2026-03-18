# simple function in python def is the keword to define the function the greet is method name then ( ) are the paramaters we did't passed anything then the method body after : our method start  greet() is calling the method

def greet():
    print("hello python")

greet()

# function with parameters

def hello(name):
    print("hello ",name)

hello("python")

# function with return keyword

def getname(name):
    return name

print(getname("chetan"))

# default parameter 

def priorlang(name="java"):
    print(name)

priorlang()


# multiple return value 

def operation(a,b):
    return a+b , a-b

add , sub = operation(1,3)
print(add,sub)

# order matters 

def fullname(name, surname ,age):
    return name , surname ,age

print(fullname("chetan" ,32 , "there")) #order matters


# *Args (same like var args in java) we can pass multiple value of same type
# internally its a tuple

def nums(*a):
   print(a)

nums(1,2,3,4)

# **kwargs
# works with dictionary

def emp_data(**data):
    print(data)

emp_data(name="chetan",age=21)


# lambda function
# in java we use -> in python instead of that we use 'lambda' keyword

add = lambda a,b : print(a + b) 

add(1,2)
