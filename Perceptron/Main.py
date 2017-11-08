from Perceptron import Perceptron
from feedForward import feedForward
from numpy import array, dot



def main(data, choice):

    if choice == "P":
        total_training_sess = int(input("How many total traning session do you want to train the network? "))
        t = 0
        and_errors = 0
        or_errors = 0
        while t < total_training_sess:
            t += 1
            ## Initializing and training AND perceptron
            print(str(t) + "-"*20+"TRAINING AND PERCEPTRON"+"-"*20)
            perceptron_and = Perceptron(data[0])

            ## Initializing and training OR perceptron
            print(str(t) + "-"*20+"TRAINING OR PERCEPTRON"+"-"*20)
            perceptron_or = Perceptron(data[1])

            print(str(t) + "-"*20+"TESTING AND PERCEPTRON"+"-"*20)
            if test(perceptron_and, AND):
                and_errors += 1
            print(str(t) + "-"*20+"TESTING OR PERCEPTRON"+"-"*20)
            if test(perceptron_or, OR):
                or_errors += 1

        print("-"*20 + "TRAINING AND TESTING COMPLETE"+"-"*20)
        print("AND_ERROS: %s, OR_ERRORS: %d, ITERATIONS: %f" % (and_errors, or_errors, total_training_sess))
    elif choice == "F":
        feedForwardNetwork = feedForward()
    else:
        print("Invalid input. Running percetron by default...")
        main(data, "P")





def test(p, info):
    isError = False
    for win, ed in info:
        res = dot(win, p.weights) > p.theta
        diff = ed - res
        if diff != 0:
            print("Error: input %s with output %d" % (repr(win), ed))
            isError = True
        else:
            print("Test passed! input %s with output %d" % (repr(win), ed))
    return isError



if __name__ == "__main__":

    AND = [
        (array([0, 0]), 0),
        (array([0, 1]), 0),
        (array([1, 0]), 0),
        (array([1, 1]), 1),
    ]
    
    OR = [
        (array([0, 0]), 0),
        (array([0, 1]), 1),
        (array([1, 0]), 1),
        (array([1, 1]), 1),
    ]

    data = array([AND, OR])

    print("TO RUN THE PERCEPTRON PRESS 'P'")
    print("TO RUN THE FEEDFORWARD ANN PRESS 'F'")
    choice = input("Answer: ")

    main(data, choice)

