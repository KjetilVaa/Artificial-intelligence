import random
from numpy import array, dot


class Perceptron(object):


    def __init__(self, data, lrate=0.2, theta=5, amountWeights=2):
        self.theta = theta
        self.lrate = lrate
        self.weights = array([self.getRandomInterval() for x in range(amountWeights)])
        self.train(data)

    def train(self, data):
        iteration = 0
        while True:
            iteration+= 1
            mistakes = 0
            for win, ed in data:
                res = dot(win, self.weights) > self.theta
                diff = ed - res
                if diff != 0:
                    mistakes+= 1
                    ##Formula for reweighting
                    self.weights = array([self.weights[i] + self.lrate * diff * value for i, value in enumerate(win)])
                    print("Vector change: %s" % repr(self.weights))
            if not mistakes:
                break
        print("Training finished: %d iterations" % iteration)


    def getRandomInterval(self):
        return random.uniform(-0.5, 0.5)