estados = ['sin-moneda', 'recibi-moneda', 'servido-c1', 'servido-c2', 'servido-c3']
percepciones = ['moneda', 'c1', 'c2', 'c3']

reglas = {
    "sin-moneda": "pedir-moneda",
    "recibi-moneda": "pedir-codigo",
    "servido-c1": "esperar",
    "servido-c2": "esperar",
    "servido-c3": "esperar"
}

acciones = {
    "pedir-moneda": "Mostrar en pantalla: 'Por favor, inserte una moneda'",
    "pedir-codigo": "Mostrar en pantalla: 'Seleccione su refresco (c1, c2, c3)'",
    "esperar": "Mostrar en pantalla: 'Gracias por su compra, por favor, tome su bebida'"
}

modelo = {
    ('sin-moneda', 'pedir-moneda', 'moneda'): "recibi-moneda",
    ('recibi-moneda', 'pedir-codigo', 'c1'): "servido-c1",
    ('recibi-moneda', 'pedir-codigo', 'c2'): "servido-c2",
    ('recibi-moneda', 'pedir-codigo', 'c3'): "servido-c3",
    ('servido-c1', 'esperar', 'moneda'): "recibi-moneda",
    ('servido-c2', 'esperar', 'moneda'): "recibi-moneda",
    ('servido-c3', 'esperar', 'moneda'): "recibi-moneda"
}


def actualizar_estado(estado, accion, percepcion):
    clave = (estado, accion, percepcion)
    return modelo.get(clave, "sin-moneda")


estado = 'sin-moneda'

while True:
    print(acciones[reglas[estado]])
    percepcion = input("Ingresar percepción: ").strip()

    accion = reglas[estado]
    estado = actualizar_estado(estado, accion, percepcion)

