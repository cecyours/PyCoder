# # -> 0
# s = "HelloMe"
# # <- -1

# # starting : 0
# # endting : -1
print(s[-1]) # 
print("-----------")

# [start:end:step]
# start : 0
# end : -1
# step : 1, !0
s = "1234567890"
print(s[-1:3:-1])

query = "Welcome {1}, to {2}, we are here for {1}"
print(query.format("Abhishek","pyCoder","Python3.10"))
#                      0          1        2

print(" {:7} : {:6} : {}".format("PyCoder","Coder","293.2"))
print(" {:7} : {:6} : {}".format("Python","Java","293.2"))
print(" {:7} : {:^6} : {}".format("PHP","1","293.2"))
