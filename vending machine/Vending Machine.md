# AGENTES REACTIVOS BASADOS EN MODELOS

## Pseudo Code

```python
Estados: 'sin-moneda', 'recibi-moneda', 'servido-c1', 'servido-c2', 'servido-c3'

Percepcion: 'moneda', 'c1', 'c2', 'c3', 'servido'

Reglas: {"sin-moneda": "pedir-moneda",
	"recibi-moneda": "pedir-codigo",
	"servido-c1": "servir-c1-esperar",
	"servido-c2": "servir-c2-esperar",
	"servido-c3": "servir-c3-esperar"}
	
acciones: {"pedir-moneda": "mostrar en pantalla 'Pedir moneda'",
	"pedir-codigo": "mostrar en pantalla 'Pedir codigo'",
	"servir-c1-esperar": "Mostrar en pantalla 'Sirviendo refresco 1 y esperar'",
	"servir-c2-esperar": "Mostrar en pantalla 'Sirviendo refresco 2 y esperar'",
	"servir-c3-esperar": "Mostrar en pantalla 'Sirviendo refresco 3 y esperar'"
}

estado = 'sin-moneda'
accion = 'pedir-moneda'

agente:
mientras(verdadero)
	Escribir "ingresar percepcion"
	leer(percepcion)
	
	estado = actualizar-estado(estado, accion, percepcion)
	regla = reglas[estado]
	accion = regla
	textoAccion = acciones[accion]
	Escribir textoAccion
fimientras

Modelo: 'sin-moneda', 'pedir-moneda', 'moneda': "recibi-moneda",
	'recibi-moneda', 'pedir-codigo', 'c1': "servido-c1",
	'recibi-moneda', 'pedir-codigo', 'c2': "servido-c2",
	'recibi-moneda', 'pedir-codigo', 'c3': "servido-c3",
	'servido-c1', 'servir-c1-esperar', 'servido': "sin-moneda",
	'servido-c2', 'servir-c2-esperar', 'servido': "sin-moneda",
	'servido-c3', 'servir-c3-esperar', 'servido': "sin-moneda",
	'recibi-moneda', 'pedir-codigo', 'moneda': "recibi-moneda"
	
actualizar-estado(estado, accion, percepcion)
	si(exiteEnModelo(estado, accion, percepcion)) entonces
		retornar Modelo[estado, accion, percepcion]
	sino
		retornar "sin-moneda"





```