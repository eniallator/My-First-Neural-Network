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


"""
// This is for the last layer only
// For previous layers, instead of calculating the product of the deriv_cost_activation and deriv_activation, 
// we just need to pass that in as a value which we then multiply with whatever is necessary

FUNCTION calculate_weights_jiggle(self, desired_output, prev_layer_activations)
    FOR i=0 UP TO self.weights.length() DO
        deriv_cost_activation = 2 * (self.activation - desired_output)
        deriv_activation = self.normalize(self.activation) * (1 - self.normalize(self.activation))
        self.weight_matrix[i][training_id] = prev_layer_activations[i] * deriv_activation * deriv_cost_activation
    END FOR
END FUNCTION

FUNCTION calculate_bias_jiggle(self, desired_output)
    deriv_cost_activation = 2 * (self.activation - desired_output)
    deriv_activation = self.normalize(self.activation) * (1 - self.normalize(self.activation))
    self.bias[training_id] = deriv_activation * deriv_cost_activation
END FUNCTION

// ADDITIONAL NOTE: In reality, each jiggle needs to be be the sum of the calculation for _each neuron in the next layer_.
FUNCTION calculate_prev_activation_jiggle(self, prev_activations, desired_output)
    prev_activations_jiggles = []
    FOR i=0 UP TO prev_activations.length() DO
        SUM for j=0 UP TO self.neurons DO // ALI LOOK AT THIS!!
            deriv_cost_activation = 2 * (self.activation - desired_output)
            deriv_activation = self.normalize(self.activation) * (1 - self.normalize(self.activation))
            RETURN self.weights[i] * deriv_activation * deriv_cost_activation
        END SUM
        prev_activations_jiggles.append(sum)
    END FOR
    RETURN prev_activations_jiggles
END FUNCTION
"""
