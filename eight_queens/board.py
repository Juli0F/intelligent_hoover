import random
import matplotlib.pyplot as plt

def generar_cromosoma():
    cromosoma = list(range(8))
    random.shuffle(cromosoma)
    return cromosoma

def funcion_de_aptitud(cromosoma):
    colisiones = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(cromosoma[i] - cromosoma[j]) == abs(i - j):
                colisiones += 1
    return 28 - colisiones

def seleccion(poblacion):
    seleccionados = []
    aptitudes = [funcion_de_aptitud(cromosoma) for cromosoma in poblacion]
    aptitud_total = sum(aptitudes)
    probabilidades = [aptitud / aptitud_total for aptitud in aptitudes]
    for _ in range(len(poblacion)):
        seleccionados.append(random.choices(poblacion, weights=probabilidades)[0])
    return seleccionados

def cruzamiento(padre1, padre2):
    hijo1, hijo2 = padre1[:], padre2[:]
    punto_cruce = random.randint(1, 6)
    segmento_hijo1 = padre2[punto_cruce:punto_cruce+2]
    segmento_hijo2 = padre1[punto_cruce:punto_cruce+2]


    hijo1 = [x for x in hijo1 if x not in segmento_hijo1]
    hijo2 = [x for x in hijo2 if x not in segmento_hijo2]

    hijo1[punto_cruce:punto_cruce] = segmento_hijo1
    hijo2[punto_cruce:punto_cruce] = segmento_hijo2


    return [hijo1, hijo2]

def reemplazo(poblacion, nueva_poblacion):
    poblacion.sort(key=funcion_de_aptitud, reverse=True)
    nueva_poblacion.sort(key=funcion_de_aptitud, reverse=True)
    return nueva_poblacion[:len(poblacion)]

def algoritmo_genetico(tamanio_poblacion, generaciones):
    poblacion = [generar_cromosoma() for _ in range(tamanio_poblacion)]
    print("Poblacion: ", poblacion)
    mejor_solucion = []
    for generacion in range(generaciones):
        seleccionados = seleccion(poblacion)
        nueva_poblacion = []
        for i in range(0, len(seleccionados), 2):
            padre1, padre2 = seleccionados[i], seleccionados[i + 1]
            nueva_poblacion.extend(cruzamiento(padre1, padre2))
        poblacion = reemplazo(poblacion, nueva_poblacion)
        mejor_solucion = max(poblacion, key=funcion_de_aptitud)
        if funcion_de_aptitud(mejor_solucion) == 28:
            break
    return mejor_solucion
def graficar_solucion(solucion):
    tablero = [[(i+j)%2 for j in range(8)] for i in range(8)]
    fig, ax = plt.subplots()
    colores_tablero = ['white', 'gray']

    for i in range(8):
        for j in range(8):
            ax.fill_between([j, j+1], i, i+1, color=colores_tablero[tablero[i][j]])

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_xticks(range(8))
    ax.set_yticks(range(8))
    ax.set_xticklabels(range(1,9))
    ax.set_yticklabels(range(1,9))

    for i, col in enumerate(solucion):
        ax.text(col + 0.5, i + 0.5, '♛', fontsize=36, ha='center', va='center', color='black' if (i+col)%2 == 0 else 'white')

    ax.grid(color='black', linestyle='-', linewidth=2)
    ax.set_title("Solucion")
    plt.gca().invert_yaxis()
    plt.savefig('./solucion.png')
    plt.show()


solucion = algoritmo_genetico(100, 1000)
print("Solución encontrada:", solucion)
print("Aptitud de la solución:", funcion_de_aptitud(solucion))
graficar_solucion(solucion)
