import random

money = random.randint(1, 200000000000)

if money > 10**9:
    print("Welcome to Forbes List!")
elif money > 10**8:
    print("Welcome to the Forbes up incomers")
elif money > 10**7:
    print("Do you like your ferraris?")
elif money > 10**6:
    print("Multimillionaire, still pretty good")
elif money > 10**5:
    print("six figure net work, decent")
elif money > 10**4:
    print("Technically not poor")
else:
    print("I am sorry")

if money< 10**4:
    print("poor")
    elif money< 10**5 and money > 10**4:
