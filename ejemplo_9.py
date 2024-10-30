#Valor de parámetro predeterminado
#El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.
#Si llamamos a la función sin argumento, usa el valor predeterminado:

def my_function(Pais="España"):
    print("Soy de " + Pais)

my_function("México")
my_function("Alemania")
my_function()
my_function("Canadá")
print(" ")