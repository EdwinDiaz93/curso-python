# funcion str()
# util para convertir numeros a string debido a que no se pueden concatenar numeros y strings

nombre='edwin'
edad=29

# print(nombre + ' esta programando a la edad de ' + edad) -> no se puede
print(nombre + ' esta programando a la edad de ' + str(edad)) 

# .format() permite inyectar valores dentro de una cadena de texto independiente si es numero o string

nombre='Chuck Norris'
numero_peliculas=20

print('El actor mas fuerte del cine es: {} y tuvo {} peliculas'.format(nombre,numero_peliculas))