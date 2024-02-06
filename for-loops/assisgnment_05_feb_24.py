# 1. Create a For loop that iterates over the list ["Uganda", "Tanzania", "Kenya"] and searches for “Kenya” in the list?

countries = ["Uganda", "Tanzania", "Kenya"]
for country in countries:
    if country == "Kenya":
        print("Kenya.")
        

# 2. Write a Python program to print a list in a reversed order using For Loop?

a = 20 
while a >= 1:
    print (a)
    a = a -1

# 3. Create a for loop that iterates over the list [-1, 2, 3, 0, -4] and checks whether each number is positive or 
#    negative?

numbers = [-1, 2, 3, 0, -4]
for number in numbers:
    if number > 0:
        print(f"{number} is positive.")
    elif number < 0:
        print(f"{number} is negative.")
    else:
        print(f"{number} is zero.")

# 4. Write a Python program using For Loop to display numbers from -10 to 1.?

for number in range(-10, 2):  
    print(number)

# 5. Write a python program using For Loop to iterate through a list of colors and prints each color?
    
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)


# 6. Research about the break and continue in For Loop
    # In Python, 'break' and 'continue' are two control statements that can alter the flow of a standard 'for' or 
    # 'while' loop. These are used to offer more flexibility in your loops, allowing you to skip parts of a loop when 
    # certain conditions are met or to exit a loop entirely.

    # Break Statement
    # The 'break' statement is used to exit a loop prematurely, stopping the iteration altogether and moving the flow
    # of control to the first statement following the loop. It's commonly used when searching for an item in a collection
    # and you want to stop  the search once the item is found. Here's a simple example:

    # Example using break
for i in range(1, 10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i) # This will print numbers 1 to 4 and then stop
    #  In this example, the loop will print numbers 1 through 4. When `i` equals 5, the `break` statement is executed, 
    # causing the loop to terminate immediately, and thus, numbers 5 through 9 will not be printed

    # Continue Statement
    # The `continue` statement is used to skip the rest of the code inside the loop for the current iteration only. 
    # Loop does not terminate but continues on with the next iteration. This is particularly useful when you want to 
    # skip certain elements or conditions in a loop. Here's an example:

    # Example using continue
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(i) # This will print only odd numbers between 1 and 9

    # In this example, the loop will print only the odd numbers between 1 and 9. When `i` is an even # number, the 
    #`continue` statement is executed, which skips the `print(i)` statement for that iteration and # proceeds directly 
    # to the next iteration of the loop.
