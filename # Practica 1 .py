# Practica 1 - Medicion empirica de complejidad
# Analisis de Algoritmos
# Codigo base de ejemplo
# Lenguaje: Python 3
# Julian Lopez Ramirez

import time #Libreria para devolver el tiempo en segundo
import random #Libreia para generar numeros aleatorios

def recorrido_simple(lista):  #Se define la funcion
    total = 0             #Se asigna un valor inicial
    for x in lista:        # Se inicializa el ciclo for   
        total += x         # Suma los valores de los elementos de la lista   
    return total           # Retorna el valor del recorrido de la lista

def doble_ciclo(lista):  #Se define la funcion
    contador = 0      # Se inicializa la lista
    for i in range(len(lista)):      #Se obtiene el tamaño de la primer lista   
        for j in range(len(lista)):       #Se obtiene el tamaño de la segunda lista       
            contador += lista[i] * lista[j]   # Toma los valores de las dos listas y los multiplica
    return contador     # Retorna el valor de la multiplicacion anterior

def experimento():  # Se define la funcion
    tamanios = [100, 500, 1000, 2000] # Se definen los tamaños con cantidades de prueba
    print("Tamano | Recorrido simple (s) | Doble ciclo (s)")           # Se hace una tabla bien bonita
    print("----------------------------------------------")             # Se hace una tabla bien bonita

    for n in tamanios:   # Hace un bucle con los tamaños
        datos = [random.randint(1, 100) for _ in range(n)]      # Hace una lista con elementos aleatorios

        inicio = time.time()                 # Inicia el momento del recorrido simple                               
        recorrido_simple(datos)              # Mide el tiempo del recorrido simple 
        t1 = time.time() - inicio            # Da el tiempo total que tardo el recorrido                       

        inicio = time.time()              # Inicia el tiempo del recorrido doble ciclo
        doble_ciclo(datos)                # Mide el tiempo del doble ciclo
        t2 = time.time() - inicio         # Obtiene el tiempo del doble ciclo

        print(f"{n:6d} | {t1:20.6f} | {t2:15.6f}")   # Se imprimen los resultados del tiempo de cada recorrido

if __name__ == "__main__":   #Inicializa 
    experimento()