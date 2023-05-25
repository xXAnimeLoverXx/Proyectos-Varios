from random import *
# pajitas
pajitas = ['Mas chica','Mediana','Grande','Gigante']

# Mezclar pajitas
def batir(lista):
    shuffle(pajitas)
    return lista

#prueba suerte
def lucky_shot():
    attempt = ''
    while attempt not in ['1','2','3','4']:
        attempt = input("dime un numero del 1 al 4: ")
    return int(attempt)

#comprobacion
def comprobar_intento(lista,attempt):
    if lista[attempt -1] == 'Mas chica':
        print('Hoy te toca perder')
    else:
        print("Te has librado!!")
    print(f"has sacado la pajita {lista[attempt -1]}")

pajitas_batidas = batir(pajitas)
golpe_suerte = lucky_shot()
comprobar_intento(pajitas_batidas,golpe_suerte)





