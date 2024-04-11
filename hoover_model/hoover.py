import threading
import time

from reactive_model import estados, percepciones, reglas, acciones, actualizar_estado

class Aspiradora:
    def __init__(self):
        self.mundo = [['limpio', 'limpio']]
        self.posicion = 0
        self.estado = 'buscando'
        self.garbage_collected = 0
        self.lock = threading.Lock()

    def ensuciar_cuadrante(self, cuadrante):
        with self.lock:
            if cuadrante in [1, 2]:
                self.mundo[0][cuadrante - 1] = 'sucio'
                print(f"Cuadrante {cuadrante} Sucio.")

    def revisar_cuadrante(self):
        with self.lock:
            return self.mundo[0][self.posicion]

    def limpiar_cuadrante(self):
        with self.lock:
            self.mundo[0][self.posicion] = 'limpio'
            print("Cuadrante limpiado.")

    def mover(self):
        with self.lock:
            self.posicion = 1 if self.posicion == 0 else 0

    def mostrar_mundo(self):
        with self.lock:
            estado_mundo = ' | '.join(self.mundo[0])
        print(estado_mundo)


    def exec(self):
        while True:
            time.sleep(2)
            self.mostrar_mundo()
            percepcion = self.revisar_cuadrante()
            accion = reglas[self.estado]
            if accion == 'revisar':
                if percepcion == 'sucio':
                    print(acciones['limpiar'])
                    self.limpiar_cuadrante()
                    self.garbage_collected += 1
                else:
                    print(acciones[f'mover-a-c{self.posicion + 1}'])
                    self.mover()
            elif accion == 'limpiar':
                self.limpiar_cuadrante()
            elif accion == 'esperar':
                print(acciones['esperar'])
                time.sleep(5)
            elif accion == 'Otro Cuadrante':
                print(acciones['Otro Cuadrante'])
                self.mover()
            self.estado = actualizar_estado(self.estado, accion, percepcion, self.posicion)

def manejar_entrada_usuario(aspiradora):
    while True:
        entrada = input("Ingrese '1' o '2' para ensuciar").strip()
        if entrada in ['1', '2']:
            aspiradora.ensuciar_cuadrante(int(entrada))
        else:
            print("Entrada no válida.")

aspiradora = Aspiradora()

hilo_aspiradora = threading.Thread(target=aspiradora.exec)
hilo_usuario = threading.Thread(target=manejar_entrada_usuario, args=(aspiradora,))


hilo_aspiradora.start()
hilo_usuario.start()

