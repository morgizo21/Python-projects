## Morgan Ntare
## Intro To Programming I
## 12/2/2024
## Re-do of homeworkGrandma-Ninja-Tiger Game orginally due on 11/25/2024. 

import random

def welcomeMessage():
    #welcome the user. 
    print("Welcome to the Grandma-Ninja-Tiger Game!")
    print("Rules:")
    print("Grandma beats Ninja, Ninja beats Tiger, Tiger beats Grandma.")
    print("First to win the required number of rounds wins the match! Lets get started.")

def numberOfRounds():
    #ask user for number of rounds needed to win.
    rounds = int(input('how many rounds are needed to win this game? Enter integer only.'))
    return rounds

def userChoice():
    #get user choice.
    print("\nChoose your move:")
    print("1 = Grandma")
    print("2 = Ninja")
    print("3 = Tiger")

    choice = int(input("Enter 1, 2, or 3: "))
    return choice

def computerChoice():
    #get choice for computer. 
    return random.randint(1, 3)

def determineWinner(human_choice, comp_choice):
    # Determine the winner of a round based on the game rules.
    if human_choice == comp_choice:
        return "Tie"
    elif (human_choice == 1 and comp_choice == 2):  # Grandma beats Ninja
        return "Human"
    elif (human_choice == 2 and comp_choice == 3):  # Ninja beats Tiger
        return "Human"
    elif (human_choice == 3 and comp_choice == 1):  # Tiger beats Grandma
        return "Human"
    else:
        return "Computer"

def main():
    # Instruct the game flow.
    welcomeMessage()
    rounds_needed = numberOfRounds()
    
    human_wins, computer_wins, ties = 0, 0, 0

    while human_wins < rounds_needed and computer_wins < rounds_needed:
        human_choice = userChoice()
        comp_choice = computerChoice()

        result = determineWinner(human_choice, comp_choice)
        if result == "Human":
            human_wins += 1
            print("You win this round!")
        elif result == "Computer":
            computer_wins += 1
            print("Computer wins this round!")
        else:
            ties += 1
            print("It's a tie!")

        print(f"Score: Human {human_wins}, Computer {computer_wins}, Ties {ties}\n")

        if human_wins == rounds_needed:
            print("Congratulations! You won the match!")
        elif computer_wins == rounds_needed:
            print("Computer wins the match! Better luck next time.")
        else:
            print("Keep playing. You might win.")

    
# Run the game
main()
