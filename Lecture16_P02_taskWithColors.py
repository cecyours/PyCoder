
import random as r
from clrprint import *

clrs = ['r','g','y','p','m','b']
code = ["\u3023","\u2863","\u2764","\u4728","\u26BD"]

for i in range(2000):
    x = r.choice(code)
    c = r.choice(clrs)
    clrprint(x,clr=c,end=" "*(i%10))

