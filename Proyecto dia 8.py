from Gen_Dec import *


def elegir_area():
    tp = ticket_perfumeria()
    tf = ticket_farmacia()
    tc = ticket_cosmetica()
    opcion = 0
    while opcion != "":
        print('Seleccione un area: ')
        print('perfumeria (P)\ncosmetica (C)\nfarmacia(F)\n')
        opcion = input().upper()
        if opcion == 'P':
            decorador()
            print("Ha escogido la sección Perfumeria")
            print(next(tp))
        elif opcion == 'F':
            decorador()
            print("Ha escogido la sección Farmacia")
            print(next(tf))
        elif opcion == 'C':
            decorador()
            print("Ha escogido la sección Cosmetica")
            print(next(tc))
        elif opcion == 'S'.upper():
            print('Adios, vuelva pronto')
            exit()


elegir_area()
