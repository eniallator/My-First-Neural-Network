from random import random

class Neuron():
    
    def __init__(self, input_size, normalize):
        self._weights = [1] if input_size == -1 else [random() for i in range(input_size)]
        self._normalize = normalize
        self._bias = input_size if input_size == -1 else random() * input_size

    def back_prop(self, cost, inp):
        deriv_cost_activation = lambda y, a: 2 * (a - y)
        deriv_activation = lambda a: self._normalize(a) * (1 - self._normalize(a))
        

    def activate(self, inputs):
        output = sum([inp * weight for inp, weight in zip(inputs, self._weights)]) - self._bias
        self._last_output = output
        return self._normalize(output)
