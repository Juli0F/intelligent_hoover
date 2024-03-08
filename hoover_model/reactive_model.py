estados = ['buscando', 'limpiando-c1', 'limpiando-c2']
percepciones = ['limpio', 'sucio']

reglas = {
    'buscando': 'revisar',
    'limpiando-c1': 'limpiar',
    'limpiando-c2': 'limpiar',
}

acciones = {
    'revisar': "Revisar si el cuadrante está sucio",
    'limpiar': "Limpiar el cuadrante",
    'mover-a-c1': "Moverse al cuadrante 1",
    'mover-a-c2': "Moverse al cuadrante 2",
}

modelo = {
    ('buscando', 'revisar', 'sucio', 0): 'limpiando-c1',
    ('buscando', 'revisar', 'sucio', 1): 'limpiando-c2',
    ('limpiando-c1', 'limpiar', 'limpio', 0): 'buscando',
    ('limpiando-c2', 'limpiar', 'limpio', 1): 'buscando',
}


def actualizar_estado(estado, accion, percepcion, posicion):
    clave = (estado, accion, percepcion, posicion)
    return modelo.get(clave, estado)

