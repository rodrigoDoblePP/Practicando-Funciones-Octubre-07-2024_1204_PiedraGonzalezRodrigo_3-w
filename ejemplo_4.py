#De forma predeterminada, se debe llamar a una función con la cantidad correcta de argumentos. 
#Lo que significa que si su función espera 2 argumentos, debe llamar a la función con 2 argumentos, ni más ni menos.

#Ejemplo

#Esta función espera 2 argumentos y obtiene 2 argumentos:

def  my_function(fname,inname):
    print (fname + " " + inname)
print (" ")
my_function("Hola", "Como Estas")
