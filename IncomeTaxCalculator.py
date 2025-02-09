## Morgan Ntare
## 10/05/2024
## HMWK 04 INTRO TO PROGRAMMING 1
## Income Tax Program

# Display welcome message
print("Welcome to the Income Tax Calculator")

# Get taxable income from user
user_income = input("Please enter your taxable income: ")

# Validate if the input is numeric
if user_income.isnumeric():
    income = int(user_income)
    
    # Calculate tax based on income brackets
    if income <= 20000:
        tax = 0.02 * income
    elif income <= 50000:
        tax = 400 + 0.025 * (income - 20000)
    else:
        tax = 1150 + 0.035 * (income - 50000)
    
    # Display the income and calculated tax
    print(f"Your taxable income is: ${income:.2f}")
    print(f"Your tax amount is: ${tax:.2f}")
else:
    # Invalid input message
    print("Error: Invalid taxable income entered. Please enter a numeric value.")
