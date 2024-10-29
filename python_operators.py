"""
1. Operators are used for performing some operation on operands.
2. In python we have 7 types of operator such as Assignment operator,Arithmetic operator,logical operaror,Relational operator,
   Bitwise operator,membership operator,identity operator.
Arithmetic Operator
====================

"""
a='sasank'
b=3
#print(a+b)Error
c='3'
print(a+c)#cdt + cdt concardination
print([45,25,36,32]+[78,45,23])
print((45,23,650)+(45,78))
#print({12,56}+{13,89})error addition between two set can not be performed.
#print({'name':'sasank'}+{'age':25}) addition between two dict won't perform.

# substracton between two set
s={78,56,23}
s2={45,55,23}
print(s-s2)#based on base set op will be returned

#print('sasank'-5)Error
#print('sasank'-'lucky')Error

#multiplication num*cdt = concardinate
print(b*a)
print(a*b)
print([78,12]*2)
print((56,23,12)*3)
#print({45,23}*3)error
#print({'name':'sasank'}*2)Error
#set and dict can not be performed
#** power operator
a=4
b=2
print(a**b)#4**2
print(a/b)#4/2
print(a//b)#4//2  eleminate decimal value from op
print(a%b)# reminder
#some Questions
a=4.5
b=2
print(a/b)
print(a//b)
print(a%b)


