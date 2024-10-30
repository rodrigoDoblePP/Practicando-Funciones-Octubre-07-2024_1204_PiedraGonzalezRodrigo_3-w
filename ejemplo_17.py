#17-Sin el *, se le permite utilizar argumentos posicionales 
#incluso si la función espera argumentos de palabras clave:

def my_function(x):
  print("El valor de x es:" ,x)

my_function(3)


#18-Pero al agregar *, / obtendrás un error si intentas enviar un argumento posicional:
def my_function(*, x):
  print(x)
  pass
  my_function(3)


