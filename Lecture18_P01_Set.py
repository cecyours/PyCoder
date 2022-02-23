
# sorted, unique
string = "{:2} : {}"

s = {100,50,250,150,300,200}
print(string.format(1,s))

s.add(500)
print(string.format(2,s))

s1 = {1,2,4,5,6,7} 
s2 = {1,3,4,8,6,9,2}

s3 = s1.difference(s2) # display content which is not present in s2
print(string.format(3,s3))

s1.difference_update(s2);
print(string.format(4,s1))

print(string.format(5,s))
s.discard(501)
print(string.format(6,s))

s1 = {1,2,4,5,7,8}
s2 = {4,1,4,3,5,7}
s3 = s1.intersection(s2) 
print(string.format(7,s3))

s1 = {1,2,4,5,7,8}
s2 = {4,1,4,3,5,7}
s1.intersection_update(s2) 
print(string.format(8,s1))

s1 = {1,2,4}
s2 = {8,7,3}
x = s1.isdisjoint(s2)
print(string.format(9.1,x))

s1 = {1,2,5,19}
s2 = {1,2,3,4,5,6,7,8,9,0}
x = s1.issubset(s2)
print(string.format(9,x))

s1 = {5,2,1,5,1}
s2 = {2,1,5}
x = s1.issuperset(s2)
print(string.format(10,x))

s1 = {1,2,3,4,5,6,7,8,9,0}
s1.pop() #index
s1.pop() #index
print(string.format(11,s1))

s1 = {1,2,3,4,5,6,7,8,9,0}
s1.remove(7) #element
print(string.format(12,s1))

s1 = {1,2,3,9,0}
s2 = {5,2,1,5,1,7}
s3 = s1.symmetric_difference(s2);
print(string.format(13,s3))

s1 = {1,2,3,9,0}
s2 = {5,2,1,5,1,7}
s1.symmetric_difference_update(s2);
print(string.format(14,s1))

s1 = {1,2,3,5,6,7,8}
s2 = {99,88,3,55,60,77,8}
s3 = s1.union(s2)
print(string.format(15,s3))

s1 = {2,4,2,4,2}
s1.update(s2)
print(string.format(16,s1))

















