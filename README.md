# My-First-Neural-Network
As the title implies, this will be my first neural network!

### Todos

For each training example:

1. Calculate the cost: Cost = sum of the squared differences for each output neuron.
    - `(desired_outputs, actual_outputs) => cost`
2. Calculate and store the cost of weights and biases for last layer.
    - for each neuron:
    - `(last_layer_activations, desired_output) => <store cost for each weight/bias in neuron>`
3. Calculate and cache the cost of the previous layer's activation functions.
    - for each neuron:
    - `(desired_output) => cost_a`
    - return and cache the cost
4. Iterate over each neuron in the previous layer and sum the costs.
5. For each neuron in the previous layer propagate backwards from the cost.

### Afterwards

Average the costs for each weight and bias from all training examples.

### Lastly

Nudge weights and biases using the learning rate * the negative cost (probably)