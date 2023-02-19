s='tengo hambre'

# len devuelve la cantidad de caracteres y cuenta la cantidad de espacios
print(len(s))

# obtener la entrada de datos por consola con input

nombre=input('Introduce tu nombre:\t')

# se puede utilizar el casteo junto a al input

edad=int(input('Introduce tu edad:\t'))


altura=float(input('Introduce tu altura:\t'))


print(f'Tu nombre es {nombre}, y tu edad es {edad}, tienes una altura de {altura}m')

print('Tu nombre es {}, y tu edad es {}, tienes una altura de {}m'.format(nombre,edad,altura))
