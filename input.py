name = input("What is your name? ")
print("nice to meet you", name)

Age = input("What is your age? ")
try:
    Age = int(Age)
    print("Thus you were born in", 2025-Age)
except ValueError:
    # In case someone adds something that is not an age, this message will come back
    print("that is not a proper age/number")
#     No limit
    print("Do not be smart with me")
except NameError:
    print("You are misspelling something")
    # Incase you have something like print mispelled in code, and it tells you
except:
    print("This will catch all other exceptions")
else:
    print("Thanks for playing fair")
          #prints if no errors occur
finally:
    print("Good bye")
    # This will always happen regardless of exception or no exception