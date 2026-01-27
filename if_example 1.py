
# simplest if, has to lead to an expression leading to true or false
import random
# From random library
number = random.randint(1,10)
print("random number is", number)
# check for odd, note that == 1 is not necessary
if number % 2 ==1:
    print("number", number, "is odd")
# or if even, you can also code it, note that == 0 is not necessary
# if not number %2 == 0:
#     print("number", number, "is even")