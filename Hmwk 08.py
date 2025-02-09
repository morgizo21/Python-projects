#Morgan Ntare
#12/11/2024
#Intro to Programming 1 - HMWK 08 – Simple Web Page Generator

#Function that displays the splash screen
def display_splash_screen():
    try:
        #Open the welcome message file in read mode
        WelcomeMsgFile = open('WPGeneratorSplashScreen.txt', 'r')
        #Read and print the content to the console
        splash_screen_text = WelcomeMsgFile.read()
        print(splash_screen_text)
        WelcomeMsgFile.close()  #Close the file after reading
        return True  #Return True if file is successfully read
    except FileNotFoundError:
        #Executes if the file is not found
        print("Error: The splash screen file was not found. Please check if its correct file name and path.")
        return False  #Return False if file is not found

#function to get user input
def get_user_input():
    user_name = input("Enter your name: ")  #Ask for the user's name
    user_description = input("Enter a sentence that describes you: ")  #Ask for a user description
    return user_name, user_description  #Return the user inputs

#Function to generate and save HTML content
def generate_html_file(user_name, user_description):
    #Write the HTML structure with dynamic content
    html_content = f"""
    <html>
    <head>
        <title>{user_name}'s Page</title>
    </head>
    <body>
        <h1>Welcome, {user_name}!</h1>
        <p>{user_description}</p>
    </body>
    </html>
    """
    #Open the HTML file in write mode
    html_file = open('UserInfoWebPage.html', 'w')
    html_file.write(html_content)
    html_file.close()  #Close the file after writing
    print("HTML file has been generated successfully.")

#Main function to coordinate the program flow
def main():
    if display_splash_screen():  #First check to see if the splash screen was successfully displayed
        user_name, user_description = get_user_input()  #Get user input
        generate_html_file(user_name, user_description)  #Generate and save the HTML page

#Calling the main function
main()
