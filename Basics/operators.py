# Arithmetic operators
from operator import truediv
from time import process_time

a=9
b=4
mod=9%4
add=a+b
sub=a-b
mul=a*b
div=a/b
div1=a//b
power=a**b
print(mod)
print(add)
print(sub)
print(mul)
print(div)
print(div1)
print(power)

#assignment operator
x=5
x*=3
print(x)

#comparision operator
a=100
b=20
c=100
print('a is greater than b',a>b)
print('b is less than c',b<c)
print('a is not equal to c',a!=b)

#logical operator
x = True
y = False
print(x and y)# it returns true if both operands are true
print(x or y)# it returns true if either of the operands is true
print(not x)# it returns false if operand is true

#identity operator
num1 = 20
num2 = 20
num3 = 30
print("is operators =",num1 is num2)
print("is not operators =",num1 is not num3)