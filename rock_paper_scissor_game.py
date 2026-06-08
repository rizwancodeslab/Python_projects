"""
WorkFLow of Project....
1- Input from User(Rock,Paper, Scissor)
2- Computer Choice (Computer will Choose randomly not conditionally)
3- Result Print

Cases:
A - Rock 
Rock - Rock = tie
Rock - Paper = Paper Win
Rock - Scissor = Rock Win

B -  Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C - Scissor 

Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
"""


import random
item_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter Your Move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer Choice = {comp_choice}.")

if user_choice == comp_choice:
    print("Both Chooses same : = Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock, So Computer Win.")
    else:
        print("Rock smashes Scissor, So You Win.")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor Cuts Paper, So You win")
    else:
        print("Rock Smashes Scissor, So Computer Win.")            


