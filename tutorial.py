def tutorial_greeting():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    tutorial     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("\n\nHello! Welcome to the tutorial")
    print("Which category do you need help with?")
    print("1. Logging In/Signing Up")
    print("2. My workout")
    print("3. Exit")

    help = input("Enter the number of the category here: ")
    if help == "1":
        login_help()

    if help == "2":
        workout_help()

    if help == "3":
        return


def login_help():
    print("\nSIGNUP\n")
    print("The signup option will allow you to create a new account or to change the "
          "password of your account if you already have one. \nTo change your password, enter '1' when prompted "
          "'Your email or username is already registered with an account! Would you like to create a new account or log"
          "in?'"
          "\nIf you already have a registered email and do NOT wish to change your password, enter option '2' at the pr"
          "ompt"
          "and you will return to the login homepage where you can select the LOGIN option (option 2)."
          )
    print("\nLOGIN\n")
    print("Enter your email and password. If you email doesn't match, check for typos or create a new account with the"
          "SIGNUP option.\n If your password doesn't match, check for typos or select the SIGNUP option and enter your"
          "email. You will see the prompt: 'Your email or username is already registered with an account! Would you lik"
          "e to create a new account or login?'"
          "To change your password, enter '1' and then type in your new password. Then you can proceed to login.")
    return_or_exit()


def return_or_exit():
    print("Would you like to return to the tutorial options or return to the program?")
    print("1. Go to tutorial option page")
    print("2. Return to program")
    user_input = input("Enter your option here: ")
    if user_input == "1":
        tutorial_greeting()

    if user_input == "2":
        return


def workout_help():
    print("After entering your information, your workout will be outputted. When prompted, you can select to regenerate"
          "movements in your workout or regenerate the whole thing. If the exercises shoe 'None' or if you get the"
          "message 'Unable to connect to bodybuilding.com right now', try again later!. This means your connection is"
          "unstable or the server is not working. \n You may have also received the message: 'Network error. Workout "
          "will be "
          "generated from cache.' This means that there was a network error, the program was unable to connect. Your"
          "workout will be generated from a small repository of exercises built in to the program. They may not be "
          "style"
          "or level accurate, so you may choose to try again later or regenerate. ")
    return_or_exit()



