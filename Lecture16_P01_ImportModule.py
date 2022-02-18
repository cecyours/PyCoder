
# normal way #1
import Lecture16_P01_UserModule
 
Lecture16_P01_UserModule.display()
Lecture16_P01_UserModule.sum(30,20)

# # syntax import module as alias #rename

import Lecture16_P01_UserModule as Pycoder # rename module
Pycoder.display();
Pycoder.sum(2,3)

# # syntax from module import subModule # specific import

from Lecture16_P01_UserModule import display,sum;
display()
sum(10,2)
sum(2)

# # Syntax  from Lecture16_P01_UserModule import *
from Lecture16_P01_UserModule import *
display()
sum(3,2)
fun(3,2)
table(5)

