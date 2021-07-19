import numpy as np


class NeuralNetwork():

    def __init__(self, layer_sizes):

        # layer_sizes example: [4, 10, 2]
        self.biases = [np.random.randn(y, 1) for y in layer_sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(layer_sizes[:-1], layer_sizes[1:])]


    def activation(self, x, name):
        if name == "sigmoid":
            return (1/(1 + np.exp(-x)))
        elif name == "tanh":
            return np.tanh(x)
        
        

    def forward(self, x, mode):
        # print("forward")
        # TODO
        # x example: np.array([[0.1], [0.2], [0.3]])
        # A1 = self.activation(self.w1 @ x + self.b1, "sigmoid")
        # A2 = self.activation(self.w2 @ A1 + self.b2, "sigmoid")

        output = x
        for b, w in zip(self.biases, self.weights):
            if mode == 'helicopter' or 'gravity':
                output = self.activation((w @ output + b), "sigmoid")
            elif mode == 'thrust':
                output = self.activation((w @ output + b), "sigmoid")
                
            
        return output



