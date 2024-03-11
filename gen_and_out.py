import zmq
from main_functions import *


def client(exercises_count):
    context = zmq.Context()

    # socket to connect to server
    client_socket = context.socket(zmq.REQ)
    client_socket.connect("tcp://127.0.0.1:5555")

    try:
        # sends a request to the server
        client_socket.send_string(str(exercises_count))

        # receive the response
        generated_index = int(client_socket.recv_string())

    finally:
        client_socket.close()
        context.term()

    return generated_index


def read_from_txt(line_number):
    try:
        with open("exercises.txt", 'r') as file:
            for i, line in enumerate(file, start=1):
                if i == line_number:
                    return line.strip()  # Strip any leading/trailing whitespace
        return None  # Return None if the specified line number is out of range
    except FileNotFoundError:
        print(f"Error: File not found.")
        return None


def generate(exercises_count, time):
    workout_length = 0  # the amount of exercises the user should have based on their time constraints
    previously_generated = []  # the indexes in the exercises.txt file that have already been generated
    exercises_generated = 0  # the count of exercises that have been generated
    exercise_list = []

    if time == "30 - 45 minutes":
        workout_length = 5

    if time == "45 minutes - 1 hour":
        workout_length = 6

    if time == "1 hour - 1.5 hours":
        workout_length = 7

    if time == "1.5 hours - 2 hours":
        workout_length = 8

    if time == "2+ hours":
        workout_length = 10

    while exercises_generated <= workout_length:
        index = client(exercises_count)
        if index not in previously_generated:
            previously_generated.append(index)
            exercise = read_from_txt(index)
            exercise_list.append(exercise)
            exercises_generated += 1

    return exercise_list



def output(exercises_count, time):
    output_list = generate(exercises_count, time)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Here is your workout!\n")
    for i in range(0, len(output_list)):
        print(f"{i}: {output_list[i]}")
