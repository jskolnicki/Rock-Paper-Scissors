import random

computer = ("Rock","Paper","Scissors")

seriesWins = 0
seriesLosses = 0

Wins = 0
Ties = 0
Losses = 0

rock = ("Rock","rock","R","r")
paper = ("Paper","paper","P","p")
scissors = ("Scissors","scissors","S","s")

def game_reset():
    Wins = 0
    Losses = 0
    Ties = 0

print("Welcome to RPS!")

name = input("Enter Your Name: ")

print("Welcome, " + str(name) + "! Let's set the ground rules!")


for a in range(100):
    score = input("What score do you want to play to? ")
    if score.isdigit():
        score = int(score)
        print("")
        break
    else:
        print("")
        print("Please enter a valid number.")
        
for b in range(100):
    series = input(("How many series of " + str(score) + " do you want to play to? "))
    if series.isdigit():
        series = int(series)
        print("Lets Begin!")
        print("______________________________________________________")
        break
    else:
        print("")
        print("Please enter a valid number")
        
for c in range(10):
    comChoice = random.choice(computer)
    myChoice = input("Enter Your Move: ")
    
#Wins
    if (myChoice in rock and comChoice == "Scissors") or (myChoice in paper and comChoice == "Rock") or (myChoice in scissors and comChoice == "Paper"):
        Wins += 1
        print("The computer picked " + str(comChoice) + ". You WIN!")

#Losses
    elif (myChoice in rock and comChoice == "Paper") or (myChoice in paper and comChoice == "Scissors") or (myChoice in scissors and comChoice == "Rock"):
        Losses += 1
        print("The computer picked " + str(comChoice) + ". You LOSE.")
#Tie
    elif (myChoice in rock and comChoice == "Rock") or (myChoice in paper and comChoice == "Paper") or (myChoice in scissors and comChoice == "Scissors"):
        Ties += 1
        print("The computer also picked " + str(comChoice) + ". You Tied.")
#Jargon
    else:
        print("You have typed an incorrect response. Please Try Again.")

#After Action
    print("")
    print("Updated Score")
    print("My Series Wins: " + str(seriesWins) + "  Computer Series Wins: " + str(seriesLosses))
    print("Wins = " + str(Wins) + "  Losses = " + str(Losses) + "  Ties = " + str(Ties))
    print("______________________________________________________")
    
