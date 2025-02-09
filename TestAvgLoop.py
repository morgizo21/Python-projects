# Morgan Ntare
# IT 261 – Introduction to Computer Programming I homework
# 10/27/2024
# This program calculates the average of multiple test scores entered by the user.
# Change Log:
# 09/20/2024 - Created a program that calculates the average of 3 test scores.
# 10/27/2024 - Modified the program to allow any number of test scores, added input validation, and used loops.

# Display a welcome message to the user
print("Welcome to the test average calculator!!!\n")
print("You can enter as many test scores as you want.")
print("Enter '999' to finish entering scores.\n")

# Initialize variables
total_scores = 0
score_count = 0
test_score = 0

# Start the loop to collect test scores
while True:
    # Input: Prompt the user to enter a test score
    test_input = input("Please enter a test score between 0 and 100 (or '999' to stop): ")
    
    # Check if the input is numeric and convert it to an integer
    if test_input.isnumeric():
        test_score = int(test_input)
        
        # Check for the sentinel value to stop the loop
        if test_score == 999:
            break
        
        # Validate that the score is between 0 and 100
        if 0 <= test_score <= 100:
            total_scores = total_scores + test_score
            score_count += 1
        else:
            print("Error: Test score must be between 0 and 100. Please try again.")
    else:
        print("Error: Please enter a valid number.")

# Check if any valid scores were entered
if score_count > 0:
    # Processing: Calculate the average of the entered scores
    average_score = total_scores / score_count
    
    # Output: Display the number of test scores and the average, rounded to two decimal places
    print(f"\nYou entered {score_count} valid test scores.")
    print(f"The average of the test scores is: {average_score:.2f}")
else:
    print("\nNo valid test scores were entered.")

# End of the program
print("\nThank you for using the test average calculator!")
