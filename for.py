i =0
while i < 10:
    print (i)
    i=i+1
print()
for i in range(10): #The whole thing is with range
    print(i)

    for i in range(0,100,7): #Multiples of 7, less than 100
        print(i)


        for j in range(20):
            print(7*j)

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()
# Only half is unique
# First iteration, all 1* are unique
# second interation, all but 2*1 are unique
# Third iteration, all but 3*2, 3*2 are unique
#continues until, 10 multipicaiton, only 10*10 is needed
# To remove repeat

for i in range(1,11):
    for j in range(i,11): # counter of previous one
        print(f"{i} * {j} = {i*j}")
    print()


    # Self attempt

    for k in range(1,20):
        for l in range(k,20):
            print(f"{k} * {l} = {k*l}")
            print()

