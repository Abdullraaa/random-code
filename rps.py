import random

# This file is a collection of Python learning examples.
# Run this file in your terminal to see the output of each section.

#print("--- Section 1: Variables and Type Casting ---")
# The round() function rounds a number to the nearest integer.
# The float() function converts the result to a floating-point number.
#number_example = float(round(10.8))
#print(f"Value: {number_example}, Type: {type(number_example)}") # Expected: 11.0, <class 'float'>
#print("-" * 20)


#print("--- Section 2: String Manipulation ---")
#greeting = "how are you doing my boyyy"

# The len() function returns the number of characters in a string.
#print(f"The length of '{greeting}' is: {len(greeting)}")

# String Slicing: string[start:stop:step]
#s = "whats you name bro?"
#print(f"Original string: '{s}'")
# Slice from index 0 to 8 with a step of 2
#print(f"Sliced [0:9:2]: '{s[0:9:2]}'") # Expected: 'was o'
# Slice from index 15 to the beginning, stepping backwards
#print(f"Sliced [15::-1]: '{s[15::-1]}'") # Expected: 'orb eman uoy st'
#print("-" * 20)


#print("--- Section 3: User Input and F-Strings ---")
# The input() function prompts the user and reads a line of text.
# Note: We've commented this out so the whole file can run without stopping.
# verb = input("Type in a verb: ")
# print(f"I can {verb} better than you could ever!!! B")
# print((verb + " ") * 5)
#print("Input examples are commented out to prevent pausing.")
#print("-" * 20)

#print("--- Section 4: Conditional Logic (if/elif/else) ---")
#secret_number = 8
#user_guess = 7 # Let's pretend the user guessed 7
#print(f"Secret number is {secret_number}. User guessed {user_guess}.")

#if user_guess < secret_number:
#    print("Result: Your guess is too low.")
#elif user_guess == secret_number:
#    print("Result: You are correct!")
#elif user_guess > secret_number:
#    print("Result: Your guess is too high.")
#print("-" * 20)


#print("--- Section 5: While Loops ---")
#print("Countdown from 5:")
#n = 5
#while n > 0:
#    print(n)
#    n = n - 1 # or n -= 1
#print("Done with countdown.")
#print("-" * 20)


#print("--- Section 6: For Loops ---")
#print("Printing a pattern with a for loop:")
# range(4, 0, -1) will generate numbers 4, 3, 2, 1
#for i in range(4, 0, -1):
#    print("$" * i)

#print("\nCalculating a sum with a for loop:")
#mysum = 0
#start = 3
#end = 6 # range(3, 6) will include 3, 4, 6 becuase of the +1
#for i in range(start, end+1):
#    mysum += i
#    print(f"i = {i}, current sum = {mysum}")
#print(f"Final sum from {start} to {end} is {mysum}")
#print("-" * 20)

#print("All examples finished. Good luck with the Rock, Paper, Scissors game!")

# The tkinter GUI code from the original file is omitted as requested.
# import tkinter
# window = tkinter.Tk()
# window.title("game")
# window.mainloop()


#task 1
#rock, paper, scissors game

playerwin = 0
computerwin = 0
ties = 0


def check_win(player, computer):
    # Use a combination of 'and' and 'or' to check for winning conditions
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "win"
    else:
        return "loss"

# --- Main Game Loop ---
# A while loop keeps the game running until the user wants to quit.
while True:
    # 1. Get choices
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    options = ["rock", "paper", "scissors"]

    # Input validation
    if user_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue # 'continue' skips the rest of the loop and starts over

    computer_choice = random.choice(options)

    # 2. Determine the winner
    result = check_win(user_choice, computer_choice)
    
    # 3. Update and display the score based on the 'result'
    print(f"You chose {user_choice}, computer chose {computer_choice}.")
    
    if result == "win":
        playerwin += 1
        print("You win! 🎉")
    elif result == "loss":
        computerwin += 1
        print("You lose. 😞")
    else:
        ties += 1
        print("It's a tie!")

    # Print the current score after each round
    print(f"Score: Player: {playerwin}, Computer: {computerwin}, Ties: {ties}")
    print("-" * 20) # A separator for readability

    # 4. Ask to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break # 'break' exits the while loop

# 5. Print the final score summary
print("\n--- Final Score ---")
print(f"Player Wins: {playerwin}")
print(f"Computer Wins: {computerwin}")
print(f"Ties: {ties}")
print("Thanks for playing!")