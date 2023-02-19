

s='me ENCANTA el chocolate y las GALLETAS'

print(s)

# lower convierte en minusculas todas las letras de una cadena de texto
print(s.lower())

# upper convierte en mayusculas todas las letras de una cadena de texto
print(s.upper())

# count cuenta la frecuencia en que se repite el texto que se le pasa en la cadena
# la siguiente linea contara la cantidad de o's en el texto declarado
print(s.count('o'))

# El metodo capitalize convierte en mayusculas la primera letra de la frase
t='me encanta aprender en udemy'
print(t.capitalize())

# El metodo title convierte en mayusculas la primera letra de cada palabra
print(t.title())

# El metodo swapcase pasa minusculas a mayusculas y viceversa
print(t.swapcase())

# El metodo replace reemplaza el texto en una cadena de caracteres

w='me gusta ir a la playa'
print(w.replace('playa','montaña'))

# el metodo split separa la cadena de texto segun el separador que indiquemos en la funcion
# el resultado es un arreglo con todas las palabras o letras separadas 
a='programando en el lenguaje de programacion python'

print(a.split(' '))

# El metodo strip elimina los espacios al inicio y al final del string
# El metodo rstrip elimina los espacios al final del string
# El metodo lstrip elimina los espacios al inicio 
d='         El elefante tiene las orejas muy grande     '
print(d.strip())
print(d.rstrip())
print(d.lstrip())

# el metodo find busca una letra y devuelve la posicion del primer match
# diferente del count que este ultimo mustra la frecuencia con que se repite el caracter
# recibe dos parametros mas el inicio y fin find( n, start, end )
h='Esta es otra cadena de texto'
print(h.find('e'))

# el metodo index es util para encontrar el indicie del texto que se le da similar al find
# la diferencia de find e index es que index lanza un error al no encontrar el caracter y 
# find devuelve -1
print(h.index('e'))

# rindex devuelve el indice de la primera letra a encontrar de derecha a izquierda
# encontrar la ultima ocurrencia

print(h.rindex('e'))

