from random import random

class Neuron():

    def __init__(self, input_size, normalize):
        self.weights = [1] if input_size == -1 else [random() for i in range(input_size)]
        self._normalize = normalize
        self.bias = input_size if input_size == -1 else random() * input_size


    def activate(self, inputs):
        output = sum([inp * weight for inp, weight in zip(inputs, self.weights)]) - self.bias
        self.last_output = output
        self.last_normalized_output = self._normalize(output)
        return self.last_normalized_output
