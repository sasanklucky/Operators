"""
Membership operator
=====================
1.Membership operator is used for returning boolean value as output.
2.It checks whether a value is present in a sequence or not.
3.we have "in" and "not" in opearator.
4.These operator will check whether specified value is present in given collection or not.


"""
#print(1 in 123)#error
#print('1' in 123)error
print(1 in [1,2,3])#True
print('1' in [1,2,3])#False
print('1' in '123')#True
print('s' in '123')
print([1] in [1,2,3])
print([1] in [1,2,3,[1],4])
print('1' not in '123')
print([1] not in [1,2,3])
print('1' not in [1,2,3])
print(2 in {'name':'sasank','age':2})#2 value check a key name as 2
print(3 in {'age':3})
print('sasank' not in {'name':'sasank','age':5})
print('name'in {'name':'sasank','age':3})
print(2 in {2:'sasank'})