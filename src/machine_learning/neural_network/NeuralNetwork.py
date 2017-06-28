import numpy as np


class BackPropagationNetwork:
    """ A back-propagation network """
    #
    # class members
    #

    layerCount: int = 0
    shape: tuple = None
    weights: list = []

    #
    # class methods
    #
    def __init__(self, layerSize: tuple):
        """ initialize the network """

        # layer info
        self.layerCount = len(layerSize) - 1
        self.shape = layerSize

        # input/output data from the last run
        self._layerInput: list = []
        self._layoutOutput: list = []

        # create the weight arrays
        for (layer1, layer2) in zip(layerSize[:-1], layerSize[1:]):
            self.weights.append(np.random.normal(scale=0.1, size=(layer2, layer1 + 1)))

    # Transfer functions
    def sgm(self, x, derivative: bool = False) -> float:
        if not derivative:
            return 1 / (1 + np.exp(-x))
        out: float = self.sgm(x)
        return out * (1 - out)

    #
    # Run method
    #
    def run(self, input: np.ndarray):
        """ Run the network based on the input data"""
        lnCases = input.shape[0]
        # clear out the previous intermediate value lists
        self._layerInput = []
        self._layoutOutput = []

        # Run it
        for index in range(self.layerCount):
            if index == 0:
                layerInput = self.weights[0].dot(np.vstack([input.T, np.ones([1, lnCases])]))


#
# If runs as a script, create a test object
#
if __name__ == "__main__":
    bpn = BackPropagationNetwork((2, 2, 1))
    print(bpn.shape)
    print(bpn.weights)
