## Morgan Ntare
## IT 261 Course Project - Iteration 04: Implementation of Milestone 2
## Second code update
## Date: 12/04/2024
## Change log:
## - 12/13/2024: Code looks good from Iteration 4. No updated code.

#Function to display a welcome message
def welcome_user():
    print("Welcome to the Soccer League Management System!")
    print("Here, you can register new teams, input match results, and view league standings.\n")

#Function to register a new team
def register_team(teamslist):
    print("\nRegister a new team")
    team_name = input("Enter the team name: ")
    teamslist = teamslist + [team_name]  # Add the team name to the list
    print(f"Your team '{team_name}' has been registered!")
    return teamslist  # Return the updated list

#Function to view all registered teams
def view_teams(teamslist):
    print("\nRegistered Teams:")
    if teamslist == []:  # Check if the list is empty
        print("No teams registered yet.")
    else:
        for team in teamslist:
            print(f"- {team}")

#Function to input match results
def input_match_results(teamslist, league_standings):
    print("\nInput Match Results")
    if teamslist == []:  #Check if there are fewer than two teams
        print("Not enough teams to record match results. Please register at least two teams.")
        return league_standings

    print("\nEnter the match details:")
    team1 = input("Enter the first team: ")
    team2 = input("Enter the second team: ")
    score1 = int(input(f"Enter the score for {team1}: "))
    score2 = int(input(f"Enter the score for {team2}: "))

    #if the team is not in league.
    if team1 not in league_standings:
        league_standings[team1] = {"Points": 0, "Goals Scored": 0, "Goals Against": 0}
    if team2 not in league_standings:
        league_standings[team2] = {"Points": 0, "Goals Scored": 0, "Goals Against": 0}
        
    #Adds goals scored respectively. 
    league_standings[team1]["Goals Scored"] += score1
    league_standings[team1]["Goals Against"] += score2
    league_standings[team2]["Goals Scored"] += score2
    league_standings[team2]["Goals Against"] += score1

    #adds points for a win and 1 point for draws/ties.
    if score1 > score2:
        league_standings[team1]["Points"] += 3
    elif score1 < score2:
        league_standings[team2]["Points"] += 3
    elif score1 == score2:
        league_standings[team1]["Points"] += 1
        league_standings[team2]["Points"] += 1

    print("Your match results have been recorded.")
    return league_standings

#Function to view league standings
def view_league_standings(league_standings):
    print("\nLeague Standings:")
    if league_standings == {}:  #Check if the standings are empty
        print("No match results recorded yet.")
    else:
        for team in league_standings:  #Loop through the team names
            stats = league_standings[team]  #Get the stats for each team
            print(f"Team: {team}")
            print(f"  Points: {stats['Points']}")
            print(f"  Goals Scored: {stats['Goals Scored']}")
            print(f"  Goals Against: {stats['Goals Against']}")
            print()  #Add a blank line for better readability
            

#Main program logic
def main():
    teamslist = []  #List to store team names
    league_standings = {}  #Dictionary to store league standings
    welcome_user()  #Display the welcome message

    while True:
        print("\nChoose an option:")
        print("1. Register a team")
        print("2. View registered teams")
        print("3. Input match results")
        print("4. View league standings")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            teamslist = register_team(teamslist)  #Update the list with the new team
        elif choice == "2":
            view_teams(teamslist)  #Pass the list to display the teams
        elif choice == "3":
            league_standings = input_match_results(teamslist, league_standings)
        elif choice == "4":
            view_league_standings(league_standings)
        elif choice == "5":
            print("Goodbye! Thank you for using the Soccer League Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the program
main()
