texto = input('Ingrese su texto: ').upper()
print('Ahora ingresa 3 letras')
letra1 = input('Primera letra: ').upper()
letra2 = input('Segunda letra: ').upper()
letra3 = input('Tercera letra: ').upper()
conjunto = letra1 + letra2 + letra3
conjunto_list = list(conjunto)
print('Las letras se repiten este numero de veces: ')
uno = (texto.count(letra1))
dos = (texto.count(letra2))
tres = (texto.count(letra3))
print(f'La {letra1} se repite {uno} veces')
print(f'La {letra2} se repite {dos} veces')
print(f'La {letra3} se repite {tres} veces')
prim = texto[0]
ult = texto[-1]
print(f'La primera letra del texto es {prim} y la ultima es {ult}')
texto_lista = texto.split()
inv = texto_lista[::-1]
print(inv)
largo = len(texto)
print(f'Tu texto posee {largo} palabras')
var = "python" in texto
print(f'La palabra "Python" se haya en su texto?')
print(var)
