#15-Pero al agregar , / obtendrá un error si intenta enviar un argumento de palabra clave:
def arguemnto(x, /):
  print(x)

argumento(x = 3)