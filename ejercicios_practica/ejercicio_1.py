# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

x = 0
# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea menor a 6>
# Además, complete la línea de código necesaria para que
# el valor de "x" incremente "1" en cada iteración
condicion = False
while x < 6:
    condicion = True
    x = x+1
    print ("El valor de X es", x)
# reemplace "condicion" por lo que crea necesario
x = 0
while True: 
    x = x+1   
    print("Valor de x =", x)
    if x > 6:
        break
    # Coloque la línea de código para que "x" incremente "1"

x = 5
# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea mayor o igual a 0>
# Además, complete la línea de código necesaria para que
# el valor de "x" decremente "1" en cada iteración

while True:    # reemplace "condicion" por lo que crea necesario
    if x < 0:
        break
    print("Valor de x =", x)
    x -= 1
    # Coloque la línea de código para que "x" decremente "1"

print("terminamos!")
