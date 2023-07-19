import random

op = ["rock","paper","scissor"]
emoji={ "rock":"✊",
    "paper":"✋",
    "scissor":"✌️"
}

choice = input("Enter yor choice from rock, paper and scissor : ")
comp = random.choice(op)

print(emoji[choice],emoji[comp])

if choice == comp :
    print("Tie!")
elif (choice == "rock" and comp == "scissor") or (choice == "paper" and comp == "rock") or (choice == "scissor" and comp == "paper"):
    print("You Win!")
else:
    print("Computer Wins!")