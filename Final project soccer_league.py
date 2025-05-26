## Morgan Ntare
## IT 262
## Date: 02/23/2025
## Change Log:
## - 02/23/2025: Added save and load functionality to store league data in a text file.
## - 03/15/2025: Removed save and load functionality, simplified to single session. Added match limits and auto-winner.
## - 04/07/2025: Reduced matches per team to 3 for quicker demo. Added early season end logic.
## - 04/21/2025 Added match count display in standings.

# Function to show a welcome message
def welcome_user():
    print("🏆 Welcome to the Soccer League! 🏆")
    print("Each team will play 3 matches. The team with the most points wins!\n")

# Function to register exactly 5 teams
def register_teams():
    teams = []
    print("📋 Register 5 Teams:")
    while len(teams) < 5:
        team_name = input(f"Enter name for team {len(teams) + 1}: ").strip()
        if team_name == "":
            print("❌ Team name cannot be empty. Try again.")
        elif not team_name.isalpha():
            print("❌ Team name should only contain letters. Try again.")
        elif team_name in teams:
            print("❌ This team is already registered. Enter a different name.")
        else:
            teams.append(team_name)
            print(f"✅ Team '{team_name}' has been registered!\n")
    print("🎉 All 5 teams are registered! You can now enter match results.\n")
    return teams

# Function to show all registered teams
def view_teams(teams):
    print("\n📋 Registered Teams:")
    for team in teams:
        print(f"- {team}")

# Function to record match results
def input_match_results(teams, standings, match_counts):
    print("\n⚽ Enter Match Results")

    team1 = input("Enter the first team: ").strip()
    team2 = input("Enter the second team: ").strip()

    if team1 not in teams or team2 not in teams:
        print("❌ One or both teams are not registered. Try again.")
        return standings, match_counts
    if team1 == team2:
        print("❌ A team cannot play against itself. Try again.")
        return standings, match_counts
    if match_counts[team1] >= 3:
        print(f"❌ {team1} has already played 3 matches.")
        return standings, match_counts
    if match_counts[team2] >= 3:
        print(f"❌ {team2} has already played 3 matches.")
        return standings, match_counts

    try:
        score1 = int(input(f"Enter the score for {team1}: "))
        score2 = int(input(f"Enter the score for {team2}: "))
    except ValueError:
        print("❌ Invalid score. Enter numbers only.")
        return standings, match_counts

    # Initialize if needed
    if team1 not in standings:
        standings[team1] = {"Points": 0, "Goals Scored": 0, "Goals Against": 0}
        match_counts[team1] = 0
    if team2 not in standings:
        standings[team2] = {"Points": 0, "Goals Scored": 0, "Goals Against": 0}
        match_counts[team2] = 0

    # Update scores
    standings[team1]["Goals Scored"] += score1
    standings[team1]["Goals Against"] += score2
    standings[team2]["Goals Scored"] += score2
    standings[team2]["Goals Against"] += score1

    if score1 > score2:
        standings[team1]["Points"] += 3
    elif score1 < score2:
        standings[team2]["Points"] += 3
    else:
        standings[team1]["Points"] += 1
        standings[team2]["Points"] += 1

    match_counts[team1] += 1
    match_counts[team2] += 1

    print(f"✅ Match recorded: {team1} {score1} - {score2} {team2}\n")

    # Check if season is over
    if all(count >= 3 for count in match_counts.values()):
        print("\n🏁 The season is over! All teams have played 3 matches.")
        declare_winner(standings)
    else:
        remaining_teams = [team for team in teams if match_counts[team] < 3]
        if len(remaining_teams) < 2:
            print("\n⚠️ No more valid matchups available.")
            print("🏁 Ending the season early.")
            declare_winner(standings)

    return standings, match_counts

# Function to view the league standings
def view_league_standings(standings, match_counts):
    print("\n📊 League Standings:")
    if not standings:
        print("No match results recorded yet.")
    else:
        print(f"{'Team':<15}{'Points':<10}{'Scored':<10}{'Against':<10}{'Played':<10}")
        print("-" * 60)
        for team, stats in standings.items():
            played = match_counts.get(team, 0)
            print(f"{team:<15}{stats['Points']:<10}{stats['Goals Scored']:<10}{stats['Goals Against']:<10}{played:<10}")

# Function to determine the winner
def declare_winner(standings):
    highest_points = 0
    winner = ""
    for team in standings:
        if standings[team]["Points"] > highest_points:
            highest_points = standings[team]["Points"]
            winner = team
    print(f"\n🏆 The Winner of the Season is **{winner}** with {highest_points} points!\n")

# Main program function
def main():
    welcome_user()
    teams = register_teams()
    standings = {}
    match_counts = {team: 0 for team in teams}

    while True:
        print("\n📌 Menu:")
        print("1️⃣ View registered teams")
        print("2️⃣ Enter match results")
        print("3️⃣ View league standings")
        print("4️⃣ Exit")

        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            view_teams(teams)
        elif choice == "2":
            standings, match_counts = input_match_results(teams, standings, match_counts)
        elif choice == "3":
            view_league_standings(standings, match_counts)
        elif choice == "4":
            print("👋 Goodbye! Your data will be lost when the program closes.")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
