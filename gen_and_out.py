import zmq
from main_functions import *
import random


class Output:
    """Class that keeps all the output information and functions"""
    def __init__(self, time):
        self.previously_generated = []
        self. exercise_list = []
        self.time = time

    def get_exercise_count(self):
        """Returns the number of exercises in the exercises file"""
        try:
            with open("exercises.txt", 'r') as file:
                exercise_count = len(file.readlines())
            return exercise_count
        except FileNotFoundError:
            print(f"Error: File not found.")
            return None

    def client(self):
        """Communicates with microservice"""
        context = zmq.Context()

        # socket to connect to server
        client_socket = context.socket(zmq.REQ)
        client_socket.connect("tcp://127.0.0.1:5555")

        try:
            # sends a request to the server
            client_socket.send_string(str(self.get_exercise_count()))

            # receive the response
            generated_index = int(client_socket.recv_string())
            # print(generated_index)

        finally:
            client_socket.close()
            context.term()

        return generated_index

    def read_from_txt(self, line_number):
        """Reads an inputted line from the exercises.txt file"""
        try:
            with open("exercises.txt", 'r') as file:
                for i, line in enumerate(file, start=1):
                    if i == line_number:
                        return line.strip()  # Strip any leading/trailing whitespace
            return None  # Return None if the specified line number is out of range
        except FileNotFoundError:
            print(f"Error: File not found.")
            return None

    def calculate_time(self):
        """Returns the number of workouts to generate based on the user's time input"""
        workout_length = 0

        if self.time == "30 - 45 minutes":
            workout_length = 5

        if self.time == "45 minutes - 1 hour":
            workout_length = 6

        if self.time == "1 hour - 1.5 hours":
            workout_length = 7

        if self.time == "1.5 hours - 2 hours":
            workout_length = 8

        if self.time == "2+ hours":
            workout_length = 10

        return workout_length

    def generate(self):
        """Generates the movements"""
        workout_length = self.calculate_time()    # the amount of exercises the user should have based on their time constraints
        exercises_generated = 0  # the count of exercises that have been generated

        while exercises_generated < workout_length:
            index = self.client()
            if index not in self.previously_generated:
                self.previously_generated.append(index)
                exercise = self.read_from_txt(index)
                self.exercise_list.append(exercise)
                exercises_generated += 1

    def regenerate(self):
        """Regenerates an index"""
        regen_index = int(input("Please enter the number of the exercise you would like to swap out: "))
        new_gen = 0
        while new_gen < 1:
            new_index = self.client()

            if new_index not in self.previously_generated:
                self.previously_generated.append(new_index)
                exercise = self.read_from_txt(new_index)
                self.exercise_list[regen_index - 1] = exercise
                new_gen += 1

        self.regen_output()

    def regen_output(self):
        """Outputs the regenerated workout"""
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Here is your workout!\n")
            for i in range(0, len(self.exercise_list)):
                info_tuple = self.gen_rep_and_set()
                sets = info_tuple[0]
                reps = info_tuple[1]
                print(f"{i + 1}: {self.exercise_list[i]} -> {sets} x {reps}")
            regen = input("Would you like to regenerate any of your exercises? (Y/N) (you can enter T to see the tutori"
                          "al): ")
            if regen.upper() == "Y":
                self.regenerate()
            if regen.upper() == "N":
                print("Thanks for playing along! Happy lifting!")
                exit(0)
            if regen.upper() == "T":
                tutorial_greeting()

    def gen_rep_and_set(self):
        """Randomly generates the sets and reps"""
        reps = random.randint(6, 15)
        sets = random.randint(2, 5)
        return sets, reps

    def output(self):
        """Outputs the generated workout"""
        self.generate()

        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Here is your workout!\n")
            for i in range(0, len(self.exercise_list)):
                info_tuple = self.gen_rep_and_set()
                sets = info_tuple[0]
                reps = info_tuple[1]

                print(f"{i + 1}: {self.exercise_list[i]} -> {sets} x {reps}")
            regen = input("Would you like to regenerate any of your exercises? (Y/N) (you can enter T to see the tutorial): ")
            if regen.upper() == "Y":
                self.regenerate()
            if regen.upper() == "N":
                print("Thanks for playing along! Happy lifting!")
                exit(0)
            if regen.upper() == "T":
                tutorial_greeting()

