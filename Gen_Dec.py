
#herramienta tickets

def ticket_farmacia():
    numero = 0
    while True:
        numero += 1
        yield f"Su ticket es F-{numero}"

def ticket_cosmetica():
    numero1 = 0
    while True:
        numero1 += 1
        yield f"Su ticket es C-{numero1}"

def ticket_perfumeria():
    numero2 = 0
    while True:
        numero2 += 1
        yield f"Su ticket es P-{numero2}"
tf = ticket_farmacia()
tc = ticket_cosmetica()
tp = ticket_perfumeria()

#herramienta para decorar turnos

def decorador():
    def funcion_saludo():
        print('saludos!')
    return funcion_saludo()






