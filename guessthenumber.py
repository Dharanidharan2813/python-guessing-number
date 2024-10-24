import random
def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100) # getting the random number from the computer
    attempts = 5  # An limitted attempts
    while attempts!=0:
            guess = int(input("Enter your guess: ")) # Getting the Number from User 
            attempts-=1  # Reducing the attempts by 1
            if guess < random_number: 
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.""\U0001F929")
                break
    else:
        print("sorry you lost the attempts""\U0001F614")
guess_the_number()
