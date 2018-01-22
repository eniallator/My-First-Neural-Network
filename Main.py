import math
from src.NeuralNetwork import NeuralNetwork


def init_network(architecture):
    normalize = lambda num: 1 / (1 + math.e ** -num)
    return NeuralNetwork(architecture, normalize)


def cost(label, outputs):
    return [((1 if i == label else 0) - output) ** 2 for i, output in enumerate(outputs)]


def main(inputs, labels, architecture):
    beautify = lambda in_list: ['%f' % item for item in in_list]
    network = init_network(architecture)
    outputs = network.feed_forward(inputs[0])
    print(beautify(outputs))
    print(beautify(cost(labels[0], outputs)))

# if __name__ == '__main__':
#     main()

# up to 5:33 in backpropagation 
