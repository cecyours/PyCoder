
# indexing : only one element -> all we seen
# slicing : multi element


s = "0123456789"

print(s[2])
print(s[2:])

# [start:end:step] -> slice
# [0:-1:1] -> defAULT
# varients 
print(s[2:7:1])
print(s[3:])
print(s[:5]) # till 5 index.
print(s[::2]) # all value
#------------------
# positive  left -> right : 0
# -ve : right -> left : -1
s = "0123456789"
print(s[-5])
print(s[-1:5:-2])
print(s[-1::-1])

s = reversed(s)
print(str(s))









