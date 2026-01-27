# Boolean: True or False

print(True or False)
print(True and False)

# Almost all units in python are true, this is inclusive of values
print(5 or 7)

# False is considered: 0, 0.0, False, None, "", etc.

print(None or False or 11 or 12 or 0)
# 12 is printed
#  They read the first true print

print(None or False or 0 or 0.0)
# 0.0 is last value checked, thus it is the one outputted eventhough it is all false
# First true value in or is result, if none are true, then its the last value,
# for and functions if all match it is the last value

print("not 7 is", not 7)
# not 7 is False

print("not False is", not False)

