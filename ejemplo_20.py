#20-Recursividad
#Python también acepta la recursividad de funciones, 
#lo que significa que una función definida puede llamarse a sí misma.

def suma_recursiva(n):
    if n > 0:
        result = n + suma_recursiva(n - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nEjemplo de Resultados de Recursión")
suma_recursiva(5)

