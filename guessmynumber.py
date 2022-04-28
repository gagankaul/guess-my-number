#Guess My Number App
import random

print("Welcome to the Guess My Number App")

name = input("What is your name: ").title().strip()
print("Hello, " + name + ". I am thinking of a number between 1 and 20. Can you guess the number?")

#Generate a random integer between 1 and 20
number = random.randint(1,20)
count = 0

#Guess the number 5 times
for i in range(5):
    count += 1
    guess = int(input("Take a guess (" + str(count) + "/5): "))
    if guess > number:
        print("Your guess " + str(guess) + " is high")
    elif guess < number:
        print("Your guess " + str(guess) + " is low")
    else:
        break

#The game is over. Recap winning or losing
if guess == number:
    print("\nCongratulations, " + name + "! You guessed my  number in " + str(count) + " tries!")
else:
    print("\nGame Over! I was thinking of " + str(number) + ".")
