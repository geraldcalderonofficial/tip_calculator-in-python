# Tip Calculator

# initialize the variables as empty strings, since input() returns strings
base_bill = ""
percentage = ""
people = ""

print("Welcome to the Tip Calculator.")

# get the base bill without tip
while True:
    print("What was the total bill?")
    base_bill = input("> ₱")
    # check if it can be converted to a float
    try:
        float(base_bill)
        # check if it's not a negative number
        # zero is fine, as they might be eating for free... not much sense asking for the other inputs then though
        if float(base_bill) < 0:
            print("The bill can't be negative. Please enter a valid amount.")
        # otherwise it should be fine
        else:
            break
    # if not, ask again
    except ValueError:
        print("Please enter a valid amount.")

# get the percentage
while True:
    print("What percentage tip would you like to give? 10, 12, or 15?")
    percentage = input("> ")
    # list of acceptable choices
    # make sure the input is one of them
    if percentage not in choices_list:
        print("Please enter 10, 12 or 15.")
    else:
        break

# get the number of people
while True:
    print("How many people to split the bill?")
    people = input("> ")
    # make sure it's a non-zero natural number
        print("Please enter a valid number of people (1,2,3, etc.)")
    else:
        break





# using a uniform message, even if there was just a single person
print(f"Each person should pay: ₱{split_bill}")

