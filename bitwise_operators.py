"""
Bitwise Operators
=================
1.Bitwise operators are used for performing operation on binary value of given number.
2.We have Bitwise '&' ,'|' and '^'.
Bitwise & state that returns 1 if both operands are 1.
Bitwise | state that returns 0 if both operands are 0.
Biytwise ^ state that returns 0 if both are same.

"""
a=10
b=12
print(a & b)
print(0b1000)
print(bin(8))
print(20 & 30)#Bitwise & state that returns 1 if both operands are 1.
print(20 | 30)#Bitwise | state that returns 0 if both operands are 0.
print(20 ^ 30)#Biytwise ^ state that returns 0 if both are same.

#Bitwise ~ , it perform 2's compliments ~n=-(n+1)
print(~5)
print(~-50)
print(~-6)
#Bitwise Left shipt << and right shipt >>

print(15>>2)
print(6<<2)
