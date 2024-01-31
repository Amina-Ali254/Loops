# Write a short guessing game programm using a while loop. The user should be prompted to guess a number between 
# 1 and 100,, you should tell them whether their guess was too high or too low after each guess. The loop 
# should keeping running until the user guesses the number correctly

target = 30
guess = int(input('Guess a number:'))
while guess != target:
    if guess >= target:
        print ("Too high")
    else:
        print ("Too low")
    guess = int(input("Guess again!"))
print ("You guessed correctly!")
