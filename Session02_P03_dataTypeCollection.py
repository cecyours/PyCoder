
print("#----------- str ---------------")

name = "PyCoder"
x = type(name)
print(name,x,sep=" = ")

print("#----------- list ---------------")

list = [1,2,3,"Hello","9.2"]
x = type(list)
print(list,x,sep=" = ")

list[0] = "------"
print(list)

print("#----------- set ---------------")
set = {3,5,1,7,8,1,2,5,5}
x = type(set)
print(set,x,sep=" = ")

print("#----------- tuple ---------------")
tuple = (2,4,2,5,7,"Hello");
x = type(tuple)
print(x)

print("#----------- dict ---------------")
dict = {"pyCoder":93, "java":10}
x = dict["php"];
print(x)

