
def Suma(num1, num2):
    return num1 + num2

def Resta(num1,num2):
    return num1 - num2

def Multiplicar(num1, num2):
    return num1 * num2

def Division(num1, num2):
    if num1 != 0:
        return num1 / num2
    else:
        print('Error,division por 0')
def Potencia(num1,num2):
    return num1 ** num2

def Operador_modulo(num1,num2):
    return num1 % num2

def Division_al_piso(num1,num2):
    return num1 // num2


while True:
    print('1.Suma')
    print('2.Resta')
    print('3.Multiplicacion')
    print('4.Division')
    print('5.Elevar potecia')
    print('6.Operador modulo')
    print('7.Division al piso')
    print('8.Salir programa')

    opcion = int(input('Elige la operacion a realizar: '))

    if opcion == 8:
        print('Fin del programa')
        break

    num1 = float(input('Introduce el primer valor: '))
    num2 = float(input('Introduce el segundo valor: '))

    if opcion == 1:
        resultado = Suma(num1,num2)
    elif opcion == 2:
        resultado = Resta(num1,num2)
    elif opcion == 3:
        resultado = Multiplicar(num1,num2)
    elif opcion == 4:
        resultado = Division(num1,num2)
    elif opcion == 5:
        resultado = Potencia(num1, num2)
    elif opcion == 6:
        resultado = Operador_modulo(num1,num2)
    elif opcion == 7:
        resultado = Division_al_piso(num1,num2)
        print(f'El numero {num2} cabe {resultado} veces')
    else:
        print('Operacion erronea')

    print(f'El resultado es: {resultado}')


