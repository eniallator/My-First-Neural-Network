from src.Neuron import Neuron

class NeuralNetwork():
    
    def __init__(self, network_architecture):
        self._architecture = []

        for index, layer_size in enumerate(network_architecture):
            input_size = -1 if not index else network_architecture[index - 1]
            current_layer = [Neuron(input_size) for i in range(layer_size)]
            self._architecture.append(current_layer)
