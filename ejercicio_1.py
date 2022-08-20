# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def imprimir_mayor(lista_numeros):
    print("Funcion imprimir mayor")
    ordenar_mayor = sorted(lista_numeros, reverse = True)
    return ordenar_mayor
    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    # y luego imprimir dicho valor en pantalla


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Complete la función "imprimir_mayor"
    numeros = (2, 10)
    numeros_ordenados = imprimir_mayor (numeros)
    print ('Numeros ordenados:')
    print (numeros_ordenados)
    print("terminamos")

# Fin del ejercicio