from random import random

class Neuron():

    def __init__(self, input_size):
        self._weights = [random()] * input_size
        self._bias = random()
