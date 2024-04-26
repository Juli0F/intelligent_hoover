from neuronal.perceptron import Perceptron


entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
salida_esperada = [0, 1, 1, 1]

print("Or")
perceptron_or = Perceptron(entradas, salida_esperada)
perceptron_or.test()

print("And")
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
salida_esperada = [0, 0, 0, 1]

perceptron_and = Perceptron(entradas, salida_esperada)
perceptron_and.test()