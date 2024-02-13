import time
import sys
import os
from inputimeout import *
from login import *
from scraper import *

# don't have tutorial implemented
# decided to keep out goals for now

def intro():
    """Prints the intro stuff to the console and returns the value of continue or see tutorial"""
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n                        Welcome to </strong>\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n</strong> is a CLI interface that generates workouts for its strong nerd users!")

    start = input("\n Enter 1 to get started or enter 2 to see the tutorial: ")
    return start


def get_login():
    """Prompts the user for login"""
    print("\nAwesome! This whole process should take around 3 minutes. But don't worry!"
          " I'll walk you through the whole process!")
    print("\nRemember at any time you can type 'back' to go to a previous step in the process."
          "You can type 'exit' to return to the home page or 'help' to view the tutorial!\n")

    time.sleep(3)
    print("\nReady? Let's begin! \n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Let's start by logging in or signing up if you are a new user! ")
    print("Enter 'Y' if you would like to login or signup or enter N to skip this step. ")
    user_continue = input("\nWould you like to login/signup? (Y/N): ")
    if user_continue == "y" or user_continue == "Y":
        ret = login_process()
        return ret                  #this will return 0 if everything is good to continue and 1 if the user wanted to exit and go back home
    else:
        return


def experience_level():
    """User picks their experience level"""
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Perfect! Now we can get started with the customization.\n")
    print("How experienced ar you in the gym?")
    print("1. Beginner - I am new and excited!")
    print("2. Intermediate - I know my way around, but I am still unsure at times")
    print("3. Expert - I know that place like the back of my hand!")
    while True:
        level = input("\n Enter a number option: ")
        if level == "1" or level == "2" or level == "3":
            return level
        else:
            if level == 'exit' or level == 'Exit':
                return 1
            if level == 'back' or level == 'Back':
                return -1
            else:
                print("Oops! Looks like you have an invalid input. Please enter a number option 1-3 or "
                  "enter 'help' for a tutorial.")



def workout_style():
    """Users can set their workout style"""
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Awesome! Now it is time to pick the style of your workout!")
    print("1. Bodybuilding/strength")
    print("2. Powerlifting")
    print("3. Olympic Lifting")
    print("4. Strongman")
    print("5. Yoga/Stretching")
    print("6. Cardio")
    print("7. Totally random!")
    while True:
        style = input("\nEnter a number option: ")
        if style == "1" or style == "2" or style == "3" or style == "4" or style == "5" or style == "6" or style == "7":
            return style
        else:
            if style == 'exit' or style == 'Exit':          # user wants to exit process
                return 1
            if style == 'back' or style == 'Back':          # user wants to go back a step
                return -1
            else:
                print("Oops! Looks like you have an invalid input. Please enter a number option 1-7 or "
                  "enter 'help' for a tutorial.")


def time_set():
    """Users can set the time for their workout"""
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Ok! How much time do you have for your workout?")
    print("1. 30 - 45 minutes")
    print("2. 45 minutes - 1 hours")
    print("3. 1 hour - 1.5 hours")
    print("4. 1.5 hours - 2 hours")
    print("5. 2+ hours")
    while True:
        wk_time = input("\nEnter a number option: ")
        if wk_time == "1" or wk_time == "2" or wk_time == "3" or wk_time == "4" or wk_time == "5":
            return wk_time
        else:
            if wk_time == 'exit' or wk_time == 'Exit':          # user wants to exit process
                return 1
            if wk_time == 'back' or wk_time == 'Back':          # user wants to go back a step
                return -1
            else:
                print("Oops! Looks like you have an invalid input. Please enter a number option 1-5 or "
                  "enter 'help' for a tutorial.")


def set_muscles():
    """Users can pick the muscle groups to target"""
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Last step! Which muscle groups would you like to target?")
    print("1. Upper Body")
    print("2. Lower Body")
    print("3. Full Body")
    print("4. Completely random!")

    while True:
        muscles = input("\nEnter a number option: ")
        if muscles == "1" or muscles == "2" or muscles == "3" or muscles == "4" or muscles == "5":
                return muscles
        else:
            if muscles == 'exit' or muscles == 'Exit':          # user wants to exit process
                return 1
            if muscles == 'back' or muscles == 'Back':          # user wants to go back a step
                return -1
            else:
                print("Oops! Looks like you have an invalid input. Please enter a number option 1-5 or "
                  "enter 'help' for a tutorial.")


def confirmation(user_parameters, muscle_num, muscles_directory, level_directory, workout_directory, time_directory):
    muscle_group_dir = {"1": "Upper Body", "2": "Lower Body", "3": "Full Body", "4": "Random"}
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Great! Now let's confirm that you entered the correct information.")
        print("1. Level             =   "f"{user_parameters["level"]}")
        print("2. Style             =   "f"{user_parameters["style"]}")
        print("3. Workout Length    =   "f"{user_parameters["time"]}")
        if muscle_num == "0":
            print("4. Muscle Groups     =   "f"{" , ".join(user_parameters["muscles"])}")
        else:
            print("4. Muscle Groups     =   "f"{muscle_group_dir[muscle_num]}")
        correct = input("Is this correct? (Y/N): ")
        if correct == "Y" or correct == "y":
            break
        if correct == "N" or correct == "n":
            change_group = input("Please enter the number of the parameter you would like to change (1-4): ")

            if change_group == "1":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("You selected to change your experience level.")
                print("It is currently at "f"{user_parameters["level"]}")
                print("Here are your options to change:\n")
                print("1. Beginner - I am new and excited!")
                print("2. Intermediate - I know my way around, but I am still unsure at times")
                print("3. Expert - I know that place like the back of my hand!")
                while True:
                    new_level = input("Please enter the number index of the level you would like to change to: ")
                    if level_directory[new_level] == user_parameters["level"]:
                        print("That was the same level you already had!")
                        same_as_before = input("If you would like to exit, enter 'done' if you would like to try again just press the enter key on your computer: ")
                        if same_as_before == 'done' or same_as_before == 'Done':
                            break
                    if new_level == "1" or new_level == "2" or new_level == "3":
                        user_parameters["level"] = level_directory[new_level]
                        print("Changing your level now...")
                        break
                    else:
                        print("Invalid input! Please enter a number index (1-3).")

            if change_group == "2":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("You selected to change your workout style.")
                print("You currently selected the "f"{user_parameters["style"]}.")
                print("Here are you options to change: \n")
                print("1. Bodybuilding")
                print("2. Powerlifting")
                print("3. Olympic Lifting")
                print("4. Strongman")
                print("5. Yoga/Stretching")
                print("6. Cardio")
                print("7. Totally random!")
                while True:
                    new_style = input("Please enter the number index of the level you would like to change to: ")
                    if workout_directory[new_style] == user_parameters["style"]:
                        print("That was the same level you already had!")
                        same_as_before = input("If you would like to exit, enter 'done' if you would like to try again just press the enter key on your computer: ")
                        if same_as_before == 'done' or same_as_before == 'Done':
                            break
                    if new_style == "1" or new_style == "2" or new_style == "3" or new_style == "4" or new_style == "5" or new_style == "6" or new_style == "7":
                        user_parameters["style"] = workout_directory[new_style]
                        print("Changing your level now...")
                        break
                    else:
                        print("Invalid input! Please enter a number index (1-7).")

            if change_group == "3":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("You selected to change your workout length.")
                print("You currently selected the "f"{user_parameters["time"]}.")
                print("Here are your options to change: \n")
                print("1. 30 - 45 minutes")
                print("2. 45 minutes - 1 hours")
                print("3. 1 hour - 1.5 hours")
                print("4. 1.5 hours - 2 hours")
                print("5. 2+ hours")
                while True:
                    new_wk_time = input("Please enter the number index of the level you would like to change to: ")
                    if time_directory[new_wk_time] == user_parameters["time"]:
                        print("That was the same level you already had!")
                        same_as_before = input("If you would like to exit, enter 'done' if you would like to try again just press the enter key on your computer: ")
                        if same_as_before == 'done' or same_as_before == 'Done':
                            break
                    if new_wk_time == "1" or new_wk_time == "2" or new_wk_time == "3" or new_wk_time == "4" or new_wk_time == "5":
                        user_parameters["time"] = time_directory[new_wk_time]
                        print("Changing your level now...")
                        break
                    else:
                        print("Invalid input! Please enter a number index (1-8).")

            if change_group == "4":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("You selected to change your muscle groups.")
                print("You currently selected "f"{muscle_group_dir[muscle_num]}")
                print("Here are your options to change: \n")
                print("1. Upper Body")
                print("2. Lower Body")
                print("3. Full Body")
                print("4. Completely random!")
                while True:
                    new_muscles = input("Please enter the number index of the level you would like to change to: ")
                    if new_muscles == muscle_num:
                        print("That was the same level you already had!")
                        same_as_before = input(
                            "If you would like to exit, enter 'done' if you would like to try again just press the enter key on your computer: ")
                        if same_as_before == 'done' or same_as_before == 'Done':
                            break
                    if new_muscles == "1" or new_muscles == "2" or new_muscles == "3" or new_muscles == "4":
                        user_parameters["muscles"] = muscles_directory[new_muscles]
                        muscle_num = new_muscles
                        print("Changing your level now...")
                        break
                    else:
                        print("Invalid input! Please enter a number index (1-4).")


def output():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Here is your workout!")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")



# make tutorial page
# scrape set up



user_parameters = {}
level_directory = {"1": "beginner", "2": "intermediate", "3": "expert"}
workout_directory = {"1": "strength", "2": "powerlifting,strength", "3": "olympic-weightlifting", "4": "strongman", "5": "stretching", "6": "cardio", "7": "random"}
time_directory = {"1": "30 - 45 minutes", "2": "45 minutes - 1 hour", "3": "1 hour - 1.5 hours", "4": "1.5 hours - 2 hours", "5": "2+ hours"}
muscles_directory = {"1": ["chest", "forearms", "triceps", "middle-back", "biceps", "shoulders", "traps", "abdominals", "lats"], "2": ["lower-back", "quadriceps", "hamstrings", "calves", "glutes", "adductors", "abductors"], "3": ["lats", "shoulders", "biceps", "abdominals", "hamstrings", "quadriceps", "triceps"], "4": "random"}
go_home = 0             # variable that allows me to break through multiple loops to get to the home one

while True:
    if go_home == 1:
        go_home = 0     # resets the go_home variable
        user_parameters = {}    # resets the user inputs after exiting the process
    get_started = intro()

    if get_started == "1":
        while True:
            if go_home == 1:
                break
            log_process = get_login()
            if log_process == 1:
                break                # return to home
            else:  #login was successful

                while True:
                    if go_home == 1:
                        break
                    level = experience_level()
                    if level == 1:          # user wanted to return to home
                        go_home = 1
                        break
                    if level == -1:         # user wanted to go back a step
                        break
                    else:
                        level_index = level_directory[level]
                        user_parameters["level"] = level_index

                        while True:
                            if go_home == 1:
                                break
                            style = workout_style()
                            if style == 1:
                                go_home = 1
                                break
                            if style == -1:
                                break
                            else:
                                style_index = workout_directory[style]
                                user_parameters["style"] = style_index

                                while True:
                                    if go_home == 1:
                                        break
                                    wk_time = time_set()
                                    if wk_time == 1:
                                        go_home = 1
                                        break
                                    if wk_time == -1:
                                        break
                                    else:
                                        time_index = time_directory[wk_time]
                                        user_parameters["time"] = time_index

                                        while True:
                                            if go_home == 1:
                                                break
                                            muscles = set_muscles()
                                            if muscles == 1:
                                                go_home = 111
                                                break
                                            if muscles == -1:
                                                break
                                            else:
                                                muscle_num = muscles
                                                muscle_index = muscles_directory[muscles]
                                                user_parameters["muscles"] = muscle_index       # if the user did basic input --> will be a list of the muscles included in the group for web scraping purposes

                                                confirmation(user_parameters, muscle_num, muscles_directory, level_directory, workout_directory, time_directory)   # the confirmation function ONLY exits once the user has confirmed everything


                                                scraper(user_parameters["level"], user_parameters["style"], user_parameters["time"], user_parameters["muscles"])
                                                output()
                                                quit()

















