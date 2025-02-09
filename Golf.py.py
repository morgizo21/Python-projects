## Morgan Ntare
## HMWK 01 GolfScoreCard
## Description: Python console application to track and analyze a round of golf scores.
## change log:
## 1/26/2025: Program creation
## 2/9/2025: Added lists to store the scores.

def main():
    #Initialize a list to store scores
    scores = []

    #Explain what the program does
    print("Welcome to the Golf Scorecard Program!")
    print("You will enter golf scores for 18 holes.")

    #Collect scores for 18 holes
    for hole in range(1, 19):
        valid_score = False
        while not valid_score:
            try:
                score = int(input(f"Enter score for hole {hole}: "))
                if score > 0:  #Score must be greater than 0
                    if score > 10:
                        score = 10  #Limit the score to 10
                    scores.append(score)  #Store the score in the list
                    valid_score = True
                else:
                    print("Score must be greater than 0. Try again.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    #Calculate the total score
    total_score = 0
    for score in scores:
        total_score += score

    #Find the minimum and maximum scores
    min_score = min(scores)
    max_score = max(scores)

    #Compare the total score to par (72)
    print("\n--- Golf Scorecard Summary ---")
    print("Scores entered:", scores)
    print("Minimum score:", min_score)
    print("Maximum score:", max_score)
    print("Total score:", total_score)

    # Display how the score compares to par
    if total_score == 72:
        print("Congratulations on shooting even par!")
    elif total_score > 72:
        over_par = total_score - 72
        print(f"You shot {over_par} over par.")
    else:
        under_par = 72 - total_score
        print(f"Great job! You shot {under_par} under par.")


# Run the program
if __name__ == "__main__":
    main()
