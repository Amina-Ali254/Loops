# Write a short guessing game programm using a while loop. The user should be prompted to guess a number, you tell them 
# whether their guess was correct or wrong after each guess. The loop should keeping running until the user guesses
# the number correctly.

target = 4
guess = int(input('guess a number:'))
while guess != target:
    print ("wrong guess")
    guess = int(input ("try again:"))
print ("you are right!")
