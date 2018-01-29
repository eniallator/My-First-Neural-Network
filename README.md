# My-First-Neural-Network
As the title implies, this will be my first neural network!

### Todos

For each training example:

1. Calculate the cost: Cost = sum of the squared differences for each output neuron.
    - `(desired_outputs, actual_outputs) => cost`
2. Calculate and store the cost of weights and biases for last layer.
    - for each neuron:
    - `(last_layer_activations, current_layer_weights, current_layer_biases) => cost_wb`
3. Calculate the cost of the previous layer activations - use these to propagate backwards (using step 2 for previous layers).
    - `() => cost_a`

### Afterwards

Average the costs for each weight and bias from all training examples.

### Lastly

Nudge weights and biases using the learning rate * the negative cost (probably)