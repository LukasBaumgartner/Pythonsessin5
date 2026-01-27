#if and else
import random

number = random.randint(1,10)
print("random number is", number)
# check for odd, note that == 1 is not necessary
if not number % 2 ==1:
    print("number", number, "is even")
else:
    print("number", number, "is odd")