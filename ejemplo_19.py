#19-Combine solo posicional y solo palabras clave
#Puede combinar los dos tipos de argumentos en la misma función.

#Cualquier argumento antes de / es solo posicional y cualquier argumento después de * es solo de palabra clave.

def calcular_total(precio, cantidad, /, *, impuesto, descuento):
    total = (precio * cantidad) + impuesto - descuento
    print("El total es:", total)

# Llamamos a la función pasando los argumentos correctamente
calcular_total(100, 3, impuesto=15, descuento=5)  # Esto imprimirá "El total es: 310"

