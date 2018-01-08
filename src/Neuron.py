from random import random

class Neuron():
    
    def __init__(self, input_size, normalize):
        self._weights = [1] if input_size == -1 else [random() for i in range(input_size)]
        self._normalize = normalize
        self._bias = 1 if input_size == -1 else random()

    def activate(self, inputs):
        output = sum([inp * weight for inp, weight in zip(inputs, self._weights)]) + self._bias
        return self._normalize(output)
