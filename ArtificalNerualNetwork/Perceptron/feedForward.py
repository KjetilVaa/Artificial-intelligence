from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer


class feedForward():

    def __init__(self):
        self.ds = self.buildDataSet()
        self.ds2 = self.buildDataSet2()
        self.net = self.buildNetwork()
        self.trainer = self.trainNetwork(self.net, self.ds)
        print(self.net.activateOnDataset(self.ds))
        print(self.net.activateOnDataset(self.ds2))
        print(self.net)
        print(self.net.params)
        print(sum(self.net.params))

    
    def buildDataSet(self):
        dataSet = SupervisedDataSet(1, 1)
        dataSet.addSample((1,),(1,))
        dataSet.addSample((2,),(2,))
        dataSet.addSample((3,),(3,))
        dataSet.addSample((4,),(4,))
        dataSet.addSample((5,),(5,))
        dataSet.addSample((6,),(6,))
        dataSet.addSample((7,),(7,))
        dataSet.addSample((8,),(8,))
        return dataSet

    def buildDataSet2(self):
        dataSet = SupervisedDataSet(1, 1)
        dataSet.addSample((-10,),(-10,))
        dataSet.addSample((0.0002,),(0.0002,))
        dataSet.addSample((30,),(30,))
        dataSet.addSample((415,),(415,))
        dataSet.addSample((0.05,),(0.05,))
        return dataSet


    def buildNetwork(self):
        net = buildNetwork(1, 20, 1, bias=True, hiddenclass=TanhLayer)
        net.sortModules()
        return net

    def trainNetwork(self, net, ds):
        trainer = BackpropTrainer(net, ds)
        trainer.trainUntilConvergence(verbose=False, validationProportion=0.15, maxEpochs=1000, continueEpochs=10)
        return trainer