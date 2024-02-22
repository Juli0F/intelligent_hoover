from quadrant import Quadrant
from hoover import Hoover
from trash import Trash
import threading
import time

quadrantA = Quadrant(5, 5)
hoover = Hoover(0, 0)
trash = None


def animation():
    quadrantA.show_square(hoover)
    hoover.search_and_move(quadrantA)



def move_hoover():
    while True:
        animation()
        print("Moviendo aspiradora...")
        time.sleep(6)

#3,2
def user_input(quadrant):

    while True:
        try:
            # coords = input("Ingresa las coordenadas para la basura (x,y): ")
            # x, y = map(int, coords.split(','))
            print("Ingrese coordenada en X")
            x = int(input())
            print("Ingrese coordenada en Y")
            y = int(input())
            print("")
            trash = Trash(x - 1, y - 1)
            quadrant.add_trash(trash)
        except ValueError:
            print("Por favor, ingrese un número válido.")


hoover_thread = threading.Thread(target=move_hoover)
input_thread = threading.Thread(target=user_input, args=(quadrantA,))

hoover_thread.start()
input_thread.start()

hoover_thread.join()
input_thread.join()