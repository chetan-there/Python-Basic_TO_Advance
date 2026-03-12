# Arithmatic operators 
# + - % * / this are the arithmatic operators
a , b = 10 ,20 
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)

# Comparison operators
# == != >= <= > < this are the comparison operators
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

# Logical Operators
# and or not

a, b = 10, 20

print(a < b and b > 5)   # both conditions true
print(a > b or b > a)    # one condition true
print(not a == b)        # reverse result

# Assignment Operators
# = += -= *= /= %= **= //=

a = 10

a += 5   # a = a + 5
print(a)

a -= 3   # a = a - 3
print(a)

a *= 2   # a = a * 2
print(a)

a /= 4   # a = a / 4
print(a)

a %= 3   # a = a % 3
print(a)

# Bitwise Operators
# & | ^ ~ << >>

a = 5   # 101
b = 3   # 011

print(a & b)   # AND
print(a | b)   # OR
print(a ^ b)   # XOR
print(~a)      # NOT
print(a << 1)  # Left shift
print(a >> 1)  # Right shift

numbers = [1,2,3,4,5]

print(3 in numbers)
print(10 in numbers)

print(3 not in numbers)