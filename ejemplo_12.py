#12- La declaración del pass
#Las definiciones de función no pueden estar vacías, pero si por alguna razón tiene una definición de función sin contenido, ingrese la instrucción pass para evitar recibir un error.
# Mensaje explicativo
print("Pass funciona para ignorar si no hay línea de código y este se ejecute sin error.")

def myfunction():
    pass  

myfunction()

print("La función 'myfunction' se ejecutó, aunque no hace nada por ahora.")
