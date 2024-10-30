#Argumentos arbitrarios de palabras clave, **kwargs
#Si no sabe cuántos argumentos de palabras clave se pasarán a su función, 
#agregue dos asteriscos: ** antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá un diccionario de argumentos y 
#podrá acceder a los elementos en consecuencia:
#Si se desconoce el número de argumentos de palabras clave, agregue un doble ** antes del nombre del parámetro:
print (" ")

#Icono validado por la comunidad
def my_function(**kid):
    print("Su ultimo Apellido es:" + kid["Iname"])

my_function(fname="Rodrigo",Iname=" Piedra")
print (" ")