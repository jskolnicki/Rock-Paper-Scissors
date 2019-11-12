import random
computer = ["Rock","Paper","Scissors"]
Wins = 0
Losses = 0
Ties = 0

Rock = ["Rock", "rock", "R", "r"]
Scissors = ["Scissors", "scissors", "S", "s"]
Paper = ["Paper", "paper", "P", "p"]

print("Enter your name:")

# name = input()
name = "Jared"

print("Hello, " + name + "!")
print("Let's play Rock, Paper, Scissors!")
print("")
print("What score do you want to play to?")

# score = int(input())
score = 3

print("")
print("Enter your first move:")



for i in range(1000):
    y = random.choice(computer)
    i = input()
    if (i in Rock and y == "Scissors") or (i in Scissors and y == "Paper") or (i in "Paper" and y == "Rock"):
        Wins += 1
        print("Your opponent picked " + str(y))
        if Wins == score:
            print("You win!!")
            print("Wins = " + str(Wins) + "  Losses = " + str(Losses) + "  Ties = " + str(Ties))
            print("")
            print("Congratulations, " + str(name) +  ", you have won the series!")
            break
        else:
            print("You Win!!")
    elif (i in Rock and y == "Paper") or (i in Scissors and y == "Rock") or (i in Paper and y == "Scissors"):
        Losses += 1
        print("Your opponent picked " + str(y))
        if Losses == score:
            print("You lose")
            print("Wins = " + str(Wins) + "  Losses = " + str(Losses) + "  Ties = " + str(Ties))
            print("")
            print("Sorry, " + str(name) +  ", you have lost the series.. Better luck next time!")
            break
        else:
            print("You lose")   
    elif (i in Rock and y == "Rock") or (i in Scissors and y == "Scissors") or (i in Paper and y == "Paper"):
        Ties += 1
        print("Your opponent also picked " + str(y))
        print("You tied.")
    else:
        print("You typed an Incorrect response. Choose 'Rock', 'Paper','Scissors'")
    
    print("Wins = " + str(Wins) + "  Losses = " + str(Losses) + "  Ties = " + str(Ties))
    print("")
    print("Enter your next move:")