#not a microservice
import hashlib
import re
import time
from tutorial import *


def signup():
    """Allows users to sign up """
    print("Welcome! We are so glad that you are signing up!")
    while True:
        username = input("Enter your username or email address: ")
        check = open('credential.txt', 'r')
        opened_check = check.read()
        match = re.search(username, opened_check)

        if match is not None:
            print("Your email or username is already registered with an account! Would you like to create a new account or login?")
            print("1. Create a new account with this email")
            print("2. Login to my account")
            option = input("Enter a number option: ")

            if option == "1":
                continue
            if option == "2":
                check.close()
                time.sleep(3)
                return(1)

        pwd = input("Enter your password: ")
        conf_pwd = input("Confirm your password: ")

        if conf_pwd != pwd:
            print("Oh-oh! Your password is not the same as above! Please try again!\n")
            continue

        else:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()

            database = open("credential.txt", "w")
            database.write(username + "\n")
            database.write(hash1)
            database.close()

            print("You have successfully registered!")
            return(0)


def login():
    """Prompts users to log in"""
    while True:
        email = input("Enter email: ")
        pwd = input("Enter your password: ")

        authenticate = pwd.encode()
        authenticated_hash = hashlib.md5(authenticate).hexdigest()
        database = open("credential.txt", "r")
        stored_email, stored_pwd = database.read().split("\n")
        database.close()

        if email == stored_email and authenticated_hash == stored_pwd:
            print("You have successfully logged in!")
            return(0)
        else:
            if email != stored_email and authenticated_hash == stored_pwd:
                print("Login failed. You entered an incorrect email. Please try again.")

            if email == stored_email and authenticated_hash != stored_pwd:
                print("Login failed. Password not valid. Please try again.")

            else:
                print("Login failed. Both email and password and incorrect. Are you sure you have an account with us? If not, create one with the sign in option.")
                return(1)


def login_process():
    """Displays the login home page"""
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n                             Welcome! Let's login or create a new account!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        print("4. Help")
        option = int(input("Please enter an option: "))
        if option == 1:
            ret = signup()
            if ret != 1:
                return 0

        if option == 2:
            ret = login()
            if ret != 1:
                return 0

        if option == 3:
            return 1

        if option == 4:
            tutorial_greeting()




