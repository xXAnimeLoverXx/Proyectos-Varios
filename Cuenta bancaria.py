class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def __str__(self):
        return f"Señor/a: {self.nombre} {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\n" \
               f"Balance: {self.balance}"
    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print('Deposito aceptado')
    def retirar(self,monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print('Retiro realizado')
        else:
            print('Fondos insuficientes')
def crear_cliente():
    nombre = input('ingrese su nombre: ')
    apellido = input('ingrese su apellido: ')
    num_cuenta = input('ingrese su numero de cuenta: ')
    cliente1 = Cliente(nombre,apellido,num_cuenta)
    return cliente1
def inicio():
    nuevoCL = crear_cliente()
    print(nuevoCL)
    opcion = 0
    while opcion != 'S':
        print('Elija funcion: Depositar (D), Retirar(R), Salir (S)')
        opcion = input().upper()
        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            nuevoCL.depositar(monto_dep)
        elif opcion ==  'R':
            monto_ret = int(input('Cuanto desea retirar?: '))
            nuevoCL.retirar(monto_ret)
        print(nuevoCL)
    print('Gracias por confiar')
inicio()
