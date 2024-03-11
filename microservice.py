import zmq
import random


def start_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5555")

    while True:
        print("**************************************")
        print("Server Listening..")
        #  Wait for next request from client
        message = socket.recv()
        print("Microservice has been called upon!")

        # Generate Random number
        random_num = str(random.randint(1, int(message)))

        #  Send reply back to client
        socket.send(random_num.encode())
        print("Sending random number " + random_num)
        print("**************************************")
        print("")


def main():
    start_server()


if __name__ == "__main__":
    main()