estados = ['buscando', 'limpiando-c1', 'limpiando-c2','moviendo']

percepciones = ['limpio', 'sucio']

reglas = {
    'buscando': 'revisar',
    'limpiando-c1': 'limpiar',
    'limpiando-c2': 'limpiar',
    'moviendo': 'mover'
}

acciones = {
    'revisar': "Revisar si el cuadrante está sucio",
    'limpiar': "Limpiar el cuadrante",
    'mover-a-c1': "Moverse al cuadrante 1",
    'mover-a-c2': "Moverse al cuadrante 2",
    'mover': "Otro Cuadrante"
}

modelo = { # donde estoy, esta limpio , mover
    ('buscando', 'revisar', 'sucio', 0): 'limpiando-c1',
    ('buscando', 'revisar', 'sucio', 1): 'limpiando-c2',
    ('limpiando-c1', 'limpiar', 'limpio', 0): 'buscando',
    ('limpiando-c2', 'limpiar', 'limpio', 1): 'buscando',
    ('moviendo', 'mover', 'limpio', 0): 'buscando',
    ('moviendo', 'mover', 'sucio', 0): 'limpiando-c1',
    ('moviendo', 'mover', 'limpio', 1): 'buscando',
    ('moviendo', 'mover', 'sucio', 1): 'limpiando-c2',
}


def actualizar_estado(estado, accion, percepcion, posicion):
    clave = (estado, accion, percepcion, posicion)
    return modelo.get(clave, estado)

