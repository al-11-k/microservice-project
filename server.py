from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)


def function_gen():
    encoding_list = ["%5E", "%2F", "%2B", "%2D", "%2A"]
    iterations = random.randint(1, 10)
    function_list = []
    for i in range(0, iterations):
        x_bool = random.randint(0, 1)

        if x_bool == 1:
            function_list.append(str(random.randint(1, 1000)))
            function_list.append("x")
            function_list.append(random.choice(encoding_list))

        else:
            function_list.append(str(random.randint(1, 1000)))
            function_list.append(random.choice(encoding_list))

    del function_list[-1]
    return "".join(function_list)


@app.route('/', methods=['GET', 'POST'])

def rendering():
    # this was for the test request :)
    if request.method == 'POST':
        input_1 = function_gen()
        input_2 = function_gen()
        return render_template('/answer.html', function1=input_1, function2=input_2)

    if request.method == 'GET':
        return render_template('/test_call.html')


#def home():
    #print("")
    #print("********************************************")
    #print("Listening... for randomize click")
    #print("")
    #print("Received message and generating 2 random functions for you!")
    #print("Calculating...")
    #print("")
    #input_1 = function_gen()
    #input_2 = function_gen()
    #print("Sending...")
    #print("Sending input 1: " + str(input_1))
    #print("Sending input 2: " + str(input_2))

    #print("********************************************")
    #return render_template('test_call.html', )
    #return jsonify({"input_1": input_1, "input_2": input_2})


if __name__ == '__main__':
    app.run(debug=True)