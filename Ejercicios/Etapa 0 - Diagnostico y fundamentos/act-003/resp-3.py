numeros = [10, 25, 7, 40, 15]

print(len(numeros))
print(numeros[0])
print(numeros[-1])
numeros.append(50)
numeros.insert(0, 5)
numeros.remove(25)
ultimo_numero = numeros.pop()
numeros.sort()
numeros2 = numeros.copy()
numeros.remove(40) # numeros2 va a seguir con 40
print(numeros)
print(numeros2)
