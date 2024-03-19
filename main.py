from gen_and_out import *
from main_functions import *
from scraper import *
from tutorial import *


def main():
    """Main UI function that calls all the others"""
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

                                                    scraper(user_parameters["style"], user_parameters["muscles"], muscle_num)

                                                    output_f = Output(user_parameters["time"])
                                                    output_f.output()
                                                    quit()


        if get_started == "2":
            tutorial_greeting()


if __name__ == "__main__":
    main()













