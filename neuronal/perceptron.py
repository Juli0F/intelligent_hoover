import random

class Perceptron:

    def __init__(self,entradas,salidas):
        self.w1 = random.random()
        self.w2 = random.random()
        self.U = random.random()
        self.lambda_ = 0.1
        self.iteraciones = 1000
        self.umbral_error = 1
        self.entradas = entradas
        self.salidas_deseadas = salidas


    def funcion_activacion(self, z):
        return 1 if z >= 0 else 0

    def algorithm(self):
        for i in range(self.iteraciones):
            errores_totales = 0
            for entrada, self.salida_deseada in zip(self.entradas, self.salidas_deseadas):
                z = self.w1 * entrada[0] + self.w2 * entrada[1] + self.U
                Y = self.funcion_activacion(z)

                e = self.salida_deseada - Y
                errores_totales += abs(e)

                if self.salida_deseada != 0:
                    self.e_porcentual = e / self.salida_deseada * 100
                else:
                    self.e_porcentual = e

                diffU = self.lambda_ * e
                diffW1 = self.lambda_ * e * entrada[0]
                diffW2 = self.lambda_ * e * entrada[1]

                self.w1 += diffW1
                self.w2 += diffW2
                self.U += diffU

            if (errores_totales / len(self.entradas)) * 100 < self.umbral_error:
                print(
                    f'Entrenamiento completo en la iteración {i + 1} con un error porcentual promedio de {(errores_totales / len(self.entradas)) * 100:.2f}%')
                break
    def test(self):
        self.algorithm()
        print("\nPruebas:")
        for entrada in self.entradas:
            z = self.w1 * entrada[0] + self.w2 * entrada[1] + self.U
            Y = self.funcion_activacion(z)
            print(f'Entrada: {entrada}, Salida Predicha: {Y}')