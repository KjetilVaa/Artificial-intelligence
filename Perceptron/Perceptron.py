import random
from numpy import array, dot


class Perceptron(object):


    def __init__(self, data, lrate=0.2, theta=0, amountWeights=2):
        self.theta = theta
        self.lrate = lrate
        self.weights = array([self.getRandomInterval() for x in range(amountWeights)])
        self.train(data)

    def predict(self, inputs, weights):
        a = dot(inputs, weights)
        if a >= self.theta:
            return 1
        else:
            return -1

    def train(self, data):
        iteration = 0
        while True:
            iteration+= 1
            mistakes = 0
            for inputs, truth  in data:
                prediction = self.predict(inputs, self.weights)
                diff = truth - prediction
                if diff != 0:
                    mistakes+= 1
                    ##Formula for reweighting
                    self.weights = array([self.weights[i] + self.lrate * diff * value for i, value in enumerate(inputs)])
                    print("Vector change: %s" % repr(self.weights))
            if not mistakes:
                break
        print("Training finished: %d iterations" % iteration)


    def getRandomInterval(self):
        return random.uniform(-0.5, 0.5)