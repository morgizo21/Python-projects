## Morgan Ntare
## Intro to programming II - HMWK 04


# Function to process student responses
# Correct answer key
correct_scores = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

# Function to process student responses
def grade_exam():
    try:
        with open("StudentResponses.txt", 'r') as file:
            for line in file:
                data = line.strip().split(',')  # Split line into a list using commas
                student_name = data[0]  # First item is the student's name
                student_answers = data[1:]  # Remaining items are answers
                
                # Initialize counters and incorrect questions tracker
                correct_count = 0
                incorrect_count = 0
                incorrect_questions = []

                # Compare student answers with correct answers
                for i in range(len(correct_scores)):
                    if i < len(student_answers):  # Ensure the answer exists
                        if student_answers[i] == correct_scores[i]:
                            correct_count += 1
                        else:
                            incorrect_count += 1
                            incorrect_questions.append(i + 1)  # Store question number

                # Determine pass/fail status
                if correct_count >= 15:
                    result = "PASSED"
                else:
                    result = "FAILED"

                # Print student summary
                print(f"\nStudent: {student_name}")
                print(f"Correct Answers: {correct_count}")
                print(f"Incorrect Answers: {incorrect_count}")
                print(f"Questions Incorrect: {incorrect_questions}")
                print(f"Result: {result}")

    except FileNotFoundError:
        print(f"Error: The file 'StudentResponses.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run grading function with the provided file
grade_exam()
