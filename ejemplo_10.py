#Pasar una lista como argumento
#Puede enviar cualquier tipo de argumento de datos a una funcion (Cadena,Numero,Lista,Diccionario Etc)
#Y sera tratado como el mismo tipo de datos dentro de la funcion
#Ej. Si se envia una lista como argumento, seguira siendo una lista cuando llegue a la funcion 

def comida (food):
    for x in food:
        print(x)

frutas = ["Arandanos","Naranja","Uvas"]
comida (frutas)