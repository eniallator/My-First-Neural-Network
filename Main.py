from src.NeuralNetwork import NeuralNetwork


def main():
    architecture = [784, 16, 16, 10]
    neural_network_instance = NeuralNetwork(architecture)


if __name__ == '__main__':
    main()
