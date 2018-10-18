from Perceptron import Perceptron
#from feedForward import feedForward
from numpy import array, dot
import random


def main(data, choice):

    if choice == "P":
        total_training_sess = int(input("How many total traning session do you want to train the network? "))
        t = 0
        errors = 0

        while t < total_training_sess:
            t += 1
            ## Initializing and train perceptron
            print(str(t) + "-"*20+"TRAINING PERCEPTRON"+"-"*20)
            perceptron = Perceptron(data)

            print(str(t) + "-"*20+"TESTING PERCEPTRON"+"-"*20)
            if test(perceptron, testData):
                errors += 1

        print("-"*20 + "TRAINING AND TESTING COMPLETE"+"-"*20)
        print("ERRORS: %d, ITERATIONS: %f" % (errors, total_training_sess))
    elif choice == "F":
        print("Pyprain not currently availiable")
        #feedForwardNetwork = feedForward()
    else:
        print("Invalid input. Running percetron by default...")
        main(data, "P")


def testPrediction(inputs, weights, thres):
    a = dot(inputs, weights)
    if a >= thres:
        return 1
    else:
        return -1

def test(p, info):
    isError = False
    for inputs, truth in info:
        prediction = testPrediction(inputs, p.weights, p.theta)
        diff = truth - prediction
        if diff != 0:
            print("Error: input %s with output %d" % (repr(inputs), truth))
            isError = True
        else:
            print("Test passed! input %s with output %d" % (repr(inputs), truth))
    return isError


def getRandomNumber():
    return int(round(random.uniform(-10, 10)))

def calculateLabel(x, y):
    #Label function: f(x) = 2x
    #Above line is 1, and below is -1 ---> check prediction helper function
    func = 2*x
    if func > y:
        return (array([x, y]), -1)
    elif func < y:
        return (array([x, y]), 1)
    else:
        #discard
        return calculateLabel(getRandomNumber(), getRandomNumber())

def generateData(numPoints, outputMsg):
    print("Generating data")
    data = []
    i = 1
    while i <= numPoints:
        i+= 1
        x = getRandomNumber()
        y = getRandomNumber()
        point = calculateLabel(x, y)
        if outputMsg:
            print("Point %s with label %s added." % (point[0], point[1]))
        data.append(point)
    return data


if __name__ == "__main__":

    numPoints = int(input("How many data points do you want? "))
    
    #Generate data
    data = generateData(numPoints, True)
    testData = generateData(numPoints, False)
    
    """
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
    """

    print("TO RUN THE PERCEPTRON PRESS 'P'")
    print("TO RUN THE FEEDFORWARD ANN PRESS 'F'")
    choice = input("Answer: ")

    main(data, choice)

