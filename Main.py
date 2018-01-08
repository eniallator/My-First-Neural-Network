import math
from src.NeuralNetwork import NeuralNetwork


def main(inputs):
    normalize = lambda num: 1 / (1 + math.e ** -num)
    architecture = [784, 16, 16, 10]
    neural_network_instance = NeuralNetwork(architecture, normalize)
    print(neural_network_instance.feed_forward(inputs))


if __name__ == '__main__':
    main()
