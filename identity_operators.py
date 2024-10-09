"""
Identity Operator
=================
 1.Identity operators are used for returning boolean value as output.
 2.we have "is" and "is not" operator in identity operator.
 3.These operator is used for comparing with memory address.
 4.There is one proccess called optimization to reduce the memory usage.
  it means,
  whenever we create multiple variable with same integer value in same code block,
  python will reuse the same object in memory.even if the value is outside cache reange of 
  small integers.
 5.Integers from -5 to 256 are cached as singletones in python.
 6.Singletone means,creating one object and use it again and again.
 7.if we create integers in separate code block, python won't cache them,'a' is 'b' will return 'False'
 even if they have same value.
"""
b=200#these  are in same code block
c=200#these  are in same code block
a=200#these  are in same code block
print(a is b) #True
print(a is c) #True
print(a is not b) #False
print(a is not c)#False
print(id(a))
print(id(b))
print(id(c))#bcz it won't create another memory address instead of reusage the memory
s='hiiiiiiiiiiiiiiiiiiiiiiiii'
s1='hiiiiiiiiiiiiiiiiiiiiiiiii'
print(id(s),id(s1))
print(s is s1)
l=[123,234,345]# bcz of mutable, memory address will be different.
l1=[123,234,345]# bcz of mutable, memory address will be different.
print(id(l),id(l1))
print(l is l1)
t=('haii',1.2,20,50,60)
t1=('haii',1.2,20,50,60)
print(id(t),id(t1))
print(t is t1)
t4=('haii',1.2,20,50,60,[45,60])#here, we storing mutable into tuple
t5=('haii',1.2,20,50,60,[45,60])#here, we storing mutable into tuple
print(id(t4),id(t5))
print(t4 is t5)

a=-6
b=-6
print(a is b) #True

k=400
def fun():# python constant folding optimaization still running
    n=400
    return (n is k)
f=fun()
print(f,'fffff')


a=257
from assignment_operator import bhim # here we are importing another module to here and got to know that difference

print(id(a),id(bhim))
print(a is bhim )

