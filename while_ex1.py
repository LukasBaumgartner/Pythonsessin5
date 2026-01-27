number =1
while number <= 100:
    print(number)
    number += 1
    # Same as number = number +1


# Infinite loop with escape mechanism

number = 1
while True:
    print(number)
    number = number +1
    if number > 100:
        break

# You can even do for nymber of time repeated
number = 1
counter = 0
while true:
    print(number)
    counter = counter + 1
    if counter == 5:
        break