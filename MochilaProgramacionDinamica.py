'''
    Nombre: MochilaProgramacionDinamica.py
    Descripción: Programa que realiza el algoritmo de la mochila con programación dinámica.
        Realizado para la asignatura de Algoritmia. Universidad de Burgos.
    Autor: TRECEÑO RODRÍGUEZ, RAFAEL - rafa13o - http://rafaeltreceno.es
    Fecha: 1 de junio de 2023
    Versión: 1.0
'''


class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

    def __repr__(self) -> str:
        return "Objeto{ Peso="+str(self.peso)+", Valor="+str(self.valor)+" }"


def Mochila(listadoObjetos, tamanioMochila):
    """
        Método que realiza el algoritmo de la mochila mediante programación dinámica.

        Recibe unos objetos (que tienen un valor y un peso) y, mediante una matriz, selecciona los objetos que más valor aporten a la mochila.

    Args:
        listadoObjetos (list): Listado de Objetos que se desean guardar en la mochila
        tamanioMochila (int): Capacidad de la mochila

    Returns:
        list: Matriz con los cálculos del algoritmo (valores)
        list: Lista de tuplas que almacena los objetos seleccionado de la siguiente forma --> (número de objeto, Objeto)
    """

    # ---- PASO 1 ---- Creamos la matriz
    matriz = []  # será una matriz más adelante
    cantidadObjetos = len(listadoObjetos)

    for contadorFila in range(0, cantidadObjetos+1):  # Creamos las filas
        fila = []
        for contadorColumna in range(0, tamanioMochila + 1):  # Creamos las columnas
            fila.append(0)  # Agregamos 0s para rellenar todas las columnas

        matriz.append(fila)  # Agregamos la nueva fila a la matriz



    # ---- PASO 2 ---- Calculamos la matriz
    for contadorFila in range(1, len(matriz)): # Recorremos las filas
        # Seleccionamos el primer objeto de la lista. Como la fila empieza en 1, tenemos que tomar uno menos (para no ignorar el 0 y no pasarnos de tamaño)
        objeto = listadoObjetos[contadorFila-1]
        
        for contadorColumna in range(1, len(matriz[0])): # Recorremos las columnas
            # Recogemos datos importantes
            valorArriba = matriz[contadorFila-1][contadorColumna]
            valorIzquierda = matriz[contadorFila][contadorColumna-1]

            # Si ya hemos encontrado una capacidad en la que poder meter el objeto actual
            if contadorColumna >= objeto.peso: 
                valorMatriz = matriz[contadorFila - 1][contadorColumna - objeto.peso]
                resultadoValor = objeto.valor + valorMatriz

                if resultadoValor > valorArriba: # Si el objeto actual proporciona más valor que otro que teníamos
                    valorAGuardar = resultadoValor
                else:
                    valorAGuardar = valorArriba
            else: # Si todavía no hemos encontrado una capacidad en la que poder meter el objeto actual
                if valorArriba > valorIzquierda:
                    valorAGuardar = valorArriba
                else:
                    valorAGuardar = valorIzquierda

            # Guardamos el valor en la posición correspondiente de la matriz
            matriz[contadorFila][contadorColumna] = valorAGuardar



    # ---- PASO 3 ---- Recogemos los objetos seleccionados
    contadorFila = len(matriz) - 1 # Empezamos desde la última fila
    contadorColumna = len(matriz[0]) - 1 # Empezamos desde la última columna
    valor = None

    listaObjetosSeleccionados = []  # Lista de tuplas

    while(valor != 0): # Mientras no hayamos llegado a la primera columna
        if contadorFila <= 0 or contadorColumna <= 0:  # la 0 no la cuento porque es una fila/columna "artificial"
            break # Para evitar salirnos de la matriz
        
        
        valor = matriz[contadorFila][contadorColumna] # recogemos el valor actual
        valorArriba = matriz[contadorFila-1][contadorColumna] # Recogemos el valor de arriba del actual

        # Si ambos valores son iguales, significa que ese objeto no lo cogemos, por lo que subimos una fila
        if valor == valorArriba:
            contadorFila -= 1

        # Ese objeto lo cogemos
        else:
            # Cogemos el objeto de la posición de la lista (como estamos trabajando con una posición más al tener una fila de 0s, tenemos que restar 1 al contador)
            objetoSeleccionado = listadoObjetos[contadorFila-1] 
            tupla = (contadorFila, objetoSeleccionado) # Creamos una tupla y almacenamos 
            listaObjetosSeleccionados.append(tupla) # Agregamos la tupla a la lista de tuplas
            contadorColumna -= objetoSeleccionado.peso # Nos movemos hacia la izquierda (restando) tantas posiciones como el peso de ese objeto
            contadorFila -= 1 # Nos movemos a la fila de arriba

    listaObjetosSeleccionados.reverse() # Damos la vuelta a la lista (para que salgan objetos 1,2,3 y no 3,2,1; no por otra cosa)

    return matriz, listaObjetosSeleccionados # Devolvemos la matriz calculada y la lista de objetos seleccionados


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
    listadoObjetos = []
    listadoObjetos.append(Objeto(1, 1))
    listadoObjetos.append(Objeto(2, 6))
    listadoObjetos.append(Objeto(5, 18))
    listadoObjetos.append(Objeto(6, 22))
    listadoObjetos.append(Objeto(7, 28))

    tamanioMochila = 11

    matriz, tupla = Mochila(listadoObjetos, tamanioMochila)
    imprimirMatriz(matriz)
    print("Objetos seleccionados: ",tupla)

    print("\n\n")

    # *** PRUEBA 2 ***
    listadoObjetos2 = []
    listadoObjetos2.append(Objeto(1, 20))
    listadoObjetos2.append(Objeto(1, 5))
    listadoObjetos2.append(Objeto(1, 7))
    listadoObjetos2.append(Objeto(6, 2))
    listadoObjetos2.append(Objeto(6, 3))
    listadoObjetos2.append(Objeto(3, 14))
    listadoObjetos2.append(Objeto(1, 11))

    tamanioMochila2 = 14

    matriz2, tupla2 = Mochila(listadoObjetos2, tamanioMochila2)
    imprimirMatriz(matriz2)
    print("Objetos seleccionados: ",tupla2)
