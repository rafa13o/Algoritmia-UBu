'''
    Nombre: SubsecuenciaComunMasLarga.py
    Descripción: Programa que realiza el algoritmo que localiza la subsecuencia común más larga entre dos cadenas (LCS).
        Realizado para la asignatura de Algoritmia. Universidad de Burgos.
    Autor: TRECEÑO RODRÍGUEZ, RAFAEL - rafa13o - https://linktr.ee/rafa13o
    Fecha: 1 de junio de 2023
    Versión: 1.0
'''

def LCS(cadena1, cadena2):
    # paso 1: crear la matriz
    # va en la parte izquierda de la tabla (indica filas - vertical)
    tamanioCadena1 = len(cadena1)
    # va en la parte derecha de la tabla (indica columnas - horizontal)
    tamanioCadena2 = len(cadena2)

    matriz = []  # se convertirá en una matriz

    # una fila para cada caracter + fila de ceros
    for filaActual in range(tamanioCadena1+1):
        fila = []  # creamos la fila
        # una columna para cada uno de los caracteres + columna de ceros
        for columnaActual in range(tamanioCadena2+1):
            fila.append(0)
        matriz.append(fila)

    # Calculamos matriz
    contadorCadena1 = 0  # contamos el índice de la cadena en el que estamos
    for filaActual in range(1, len(matriz)):  # recorremos filas
        contadorCadena2 = 0  # contamos el índice de la cadena en el que estamos
        for columnaActual in range(1, len(matriz[0])):  # recorremos columnas

            # guardamos los valores más importantes
            valorDiagonal = matriz[filaActual-1][columnaActual-1]
            valorIzquierda = matriz[filaActual][columnaActual-1]
            valorArriba = matriz[filaActual-1][columnaActual]
            valorAGuardar = None

            # el caracter de la fila coincide con el de la columna (se toma la diagonal y se suma 1)
            if(cadena1[contadorCadena1] == cadena2[contadorCadena2]):
                valorAGuardar = (valorDiagonal+1)
            # los valores no coincide, se copia el máximo (de entre el de la izquierda y el de arriba)
            else:
                if valorIzquierda > valorArriba:  # el valor de la izquierda es mayor que el de arriba
                    valorAGuardar = valorIzquierda
                else:
                    valorAGuardar = valorArriba

            # guardamos el valor calculado (o copiado)
            matriz[filaActual][columnaActual] = valorAGuardar
            # aumentamos el índice de la cadena2 (columnas)
            contadorCadena2 += 1

        contadorCadena1 += 1

    # seleccionamos valores
    subcadena = ""  # Resultado de ejecutar LCS

    fila = len(matriz)-1
    columna = len(matriz[0])-1

    # Contamos el índice de la cadena que estamos analizando
    contadorCadena1 = len(cadena1) - 1
    # Contamos el índice de la cadena que estamos analizando
    contadorCadena2 = len(cadena2) - 1
    valor = None

    while(valor != 0):  # recorremos la matriz hasta encontrar un 0 (llegamos a la columna de más a la izquierda)
        # Comprobamos el valor en esa celda (numérico)
        valor = matriz[fila][columna]

        # si el caracter de la fila es igual que el de la columna nos moveremos en diagonal y ese caracter será parte de la LCS
        if cadena1[contadorCadena1] == cadena2[contadorCadena2]:
            subcadena = cadena1[contadorCadena1] + subcadena
            fila -= 1
            columna -= 1

            contadorCadena1 -= 1
            contadorCadena2 -= 1
        # si los caracteres no son iguales, nos movemos a la izquierda (una columna menos)
        else:
            columna -= 1
            contadorCadena2 -= 1

    return matriz, subcadena  # devolvemos matriz y subcadena (para debug)


        
def imprimirMatriz(matriz):
    """Método que imprime una matriz junto con los índices de las filas y las columnas.

    Args:
        matriz (list[]): Matriz que se desea imprimir por pantalla
    """
    
    cabecera = "\t\t|\t\t"
    for indice in range(len(matriz[0])): # Agregamos los índices de las columnas
        cabecera += str(indice) + "\t\t "
    
    cabecera += "\n"
    
    # Imprimimos una línea de separación entre los índices y los valores de la matriz
    for i in range(len(cabecera)):
        cabecera += "--"
    
    print(cabecera) # Imprimimos la cabecera
    
    # Imprimimos los valores
    contadorFila = 0 # Índice de las filas
    for fila in matriz: # Recorremos las filas
        print(contadorFila, "\t|\t\t", end= "") # Imprimimos el indice de la fila
        for valor in fila: # Recorremos las columnas
            print(valor, "\t", end="\t")
        contadorFila += 1 # Incrementamos el indice
        print() # Salto de línea (nueva fila)


if __name__ == "__main__":
    # *** PRUEBA 1 ***
    cadena1 = "ABCBDAB"
    cadena2 = "BDCABA"

    # *** PRUEBA 2 ***
    #cadena1 = "TTAACGAGGTA"
    #cadena2 = "TGCAGAATAGG"

    matriz, subcadena = LCS(cadena1, cadena2)
    imprimirMatriz(matriz)
    print("La subcadena común más larga encontrada entre la cadena '",
          cadena1, "' y la cadena '", cadena2, "' es '", subcadena, "'")
