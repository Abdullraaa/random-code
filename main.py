import random

player_score = 0
attempts = 0

while True:
    user_name = input("What is your name?: ")
    random_num = [1,2,3,4,5,6,7,8,9,10]
    final_num = random.choice(random_num)
    fav_num = int(input("Whats your fav number 1-10?: "))


    if fav_num == final_num:
        player_score += 1
        print(f"you chose {fav_num} and the correct {final_num}")
        print("nice guess")
    elif fav_num < final_num:
        print(f"you chose {fav_num} and the correct {final_num}")
        print("too low try again")
    elif fav_num > final_num:
        print(f"you chose {fav_num} and the correct {final_num}")
        print("too high try again")
    

    attempts += 1
    
    play_again = input("play again?:")
    if play_again == "yes":
        continue
    else:
        break

print(f"you scored {player_score} out of {attempts} attemnts.")   
print("Thank you for playing better luck next time")