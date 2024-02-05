# Write a python program using while loop that counts down from 5 to 1 ?

a = 5
while a >= 1:
    print (a)
    a = a -1

# Write a python program using while loop that prints a triangle pattern of stars?

height = 5
line = 1
while line <= height:
    print(' ' * (height - line) + '*' * (2 * line - 1))
    line += 1

# Research about Break and Continue in While Loops and give examples of how they are used?
    # Break
    # Break is used to terminate from the loop