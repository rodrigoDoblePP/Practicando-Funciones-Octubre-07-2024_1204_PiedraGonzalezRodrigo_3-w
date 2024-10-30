#6- Si no sabe cuántos argumentos se pasarán a su función, agregue un * 
#antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:
#Si se desconoce el número de argumentos, agregue un * antes del nombre del parámetro:

print(" ")
def my_function(*kids):
    print ("El niño mas joves es: " +kids[2])
my_function("Rodrigo", "Ivan", "Alan")