from src.Neuron import Neuron

class NeuralNetwork():
    
    def __init__(self, network_architecture, normalize):
        self._architecture = []
        self._normalize = normalize

        for index, layer_size in enumerate(network_architecture):
            input_size = -1 if not index else network_architecture[index - 1]
            current_layer = [Neuron(input_size, normalize) for i in range(layer_size)]
            self._architecture.append(current_layer)

    def feed_forward(self, inputs):
        self._last_inputs = inputs
        last_outputs = inputs
        for layer in self._architecture:
            last_outputs = [neuron.activate(last_outputs) for neuron in layer]
        return last_outputs

    def back_prop(self, expected_outputs):
        deriv_cost_activation = lambda y, a: 2 * (a - y)
        deriv_activation = lambda a: self._normalize(a) * (1 - self._normalize(a))

        layer = self._architecture[-1]
        for i, neuron in enumerate(layer):
            # assumes same number of inputs as neurons
            print(neuron.back_prop(expected_outputs[i], self._last_inputs[i]))

"""
FUNCTION calculate_cost(neurons, desired_output)
    sum = 0
    FOR i=0 UP TO neurons.length() DO
        sum = sum + (neurons[i].activation - desired_output) ^ 2
    END FOR
    RETURN sum
END FUNCTION
"""
