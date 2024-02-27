import random

encoding_list = ["%5E", "%2F", "%2B", "%2D", "%2A"]



def function_gen():
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

print(function_gen())




