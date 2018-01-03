from random import random

class Neuron():
    
    def __init__(self, input_size):
        self._weights = [1] if input_size == -1 else [random() for i in range(input_size)]
        self._bias = 1 if input_size == -1 else random()
