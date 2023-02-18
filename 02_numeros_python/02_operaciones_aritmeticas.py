from math import pow

# toda operacion que involucre un float dara como resultado un float
# solo la division de dos enteros da como resultado un decimal
# en versiones anteriores la division entera daba entero

print( 2 + 2 )

print( 4 + 2 )

print( 4 * 4 )

# multiplicar denomidador por 1.0 para compatibilidad con versiones antiguas
print( 4 / 4 )

# division que da como resultado la parte entera
print( 10 // 3 )

# division que da como resultado el resto
print( 10 % 3 )

# de igual forma la potencia da como resultado un float si almenos uno de los operando es float caso contratio sera int

# utilizando **
print( 5 ** 3 )

print( 5. ** 3 )

print( 5. ** 3. )

# utilizando pow
pow( 5 , 3 )

pow ( 5. , 3 )

pow ( 5. , 3. )

# Jerarquia de operadores

# Los parentesis con mayor jerarquia

# potencias y operaciones especiales

# multiplicaciones y divisiones de izquierda a dercha si hay muchas

# finalmente sumas y restas

