import csv
from Ejercicio3.modulos.grafo import Grafo, Vertice
from Ejercicio3.modulos.cola_prioridad import ColaPrioridadMax, ColaPrioridadMin
from Ejercicio3.modulos.algoritmos_dijkstra import dijkstra_capacidad_de_carga, dijkstra_precio

def abrir_archivo(nombre: str = 'rutas.txt'):
    '''
    Abre un archivo, lee sus datos, los almacena en una lista,
    y la retorna.

    Parameters
    ----------
    nombre : str, optional
        Nombre del archivo a leer. Por defecto es 'rutas.txt'.

    Returns
    -------
    datos : list
        Lista de datos que contiene el archivo leído.

    '''
    datos = []
    with open(nombre, 'r') as archivo:
        lector = csv.reader(archivo, delimiter=",")
        for linea in lector:
            datos.append((linea[0], linea[1], int(linea[2]), int(linea[3])))
        
    return datos

def completar_grafo(lista: list):
    grafo = Grafo()     # Inicializo un Grafo
    
    '''
    Lleno el Grafo con los Vértices y las aristas que los conectan a sus vecinos.
    Como ponderación, cargo la capacidad de carga. 
    Luego, en base al grafo procesado de las capacidades de carga, creo un grafo con los precios.
    '''
    for linea in lista:
        grafo.agregarArista(linea[0], linea[1], int(linea[2]))
    
    return grafo

def obtener_mayor_capacidad_carga(grafo, de: str, a: str):
    '''
    Aplico el algoritmo de dijkstra modificado sobre el Grafo, 
    dándole una ciudad inicial. Luego del procesamiento, 
    retorno el mayor cuello de botella para llegar a la ciudad destino.

    Parameters
    ----------
    grafo : Grafo
        Grafo de las rutas.
    de : str
        Ciudad inicial.
    a : str
        Ciudad destino.

    Returns
    -------
    int
        Ponderación del Vértice destino.
        (Mayor cuello de botella para llegar a la ciudad destino).

    '''
    
    '''
    Aplico dijkstra modificado en el Grafo para buscar 
    el mayor cuello de botella para llegar a cada ciudad.
    '''
    dijkstra_capacidad_de_carga(grafo, grafo.obtenerVertice(de))
    
    '''
    Luego del procesamiento, el Vértice destino guarda en su atributo de distancia,
    la Ponderación con el mayor cuello de botella para llegar hasta él desde la ciudad inicial.
    '''
    return grafo[a].obtenerDistancia()

def obtener_menor_precio(grafo, de: str, a: str):
    '''
    Aplico el algoritmo de dijkstra sobre el Grafo, 
    dándole una ciudad inicial. Luego del procesamiento, 
    retorno el precio tota para llegar a la ciudad destino.

    Parameters
    ----------
    grafo : Grafo
        Grafo de las rutas.
    de : str
        Ciudad inicial.
    a : str
        Ciudad destino.

    Returns
    -------
    int
        Ponderación del Vértice destino.
        (Menor precio para llegar a la ciudad destino).

    '''
    
    '''
    Aplico dijkstra en el Grafo para buscar el menor precio
    para llegar a ca dada ciudad.
    '''
    dijkstra_precio(grafo, grafo.obtenerVertice(de))
    
    '''
    Luego del procesamiento, el Vértice destino guarda en su atributo de distancia,
    la Ponderación con el precio total para llegar hasta él desde la ciudad inicial.
    '''
    return grafo[a].obtenerDistancia()

def obtener_ruta(grafo, de: str, a: str):
    '''
    Obtengo la ruta del Grafo ya procesado. 

    Parameters
    ----------
    grafo : Grafo
        Grafo ya procesado con la ruta con Mayor capacidad de carga y menor precio.
    de : str
        Ciudad inicial.
    a : str
        Ciudad destino.

    Returns
    -------
    ruta : list
        Ruta de ciudades.

    '''
    
    # Creo lista para guardar las ciudades de la ruta
    ruta = []
    
    # Arranco a recorrer los Vértices de la ruta desde la ciudad destino hacia la ciudad inicial.
    verticeActual = grafo.obtenerVertice(a)
    ruta.append(verticeActual.obtenerClave())
    
    while verticeActual.obtenerPredecesor():
        '''
        Recorro el predecesor de cada Vértice, agregando su ciudad a la ruta,
        y actualizando el Vértice actual.
        '''
        ruta.append(verticeActual.obtenerPredecesor().obtenerClave())
        verticeActual = verticeActual.obtenerPredecesor()
    
    # Invierto la lista, ya que comienzo a armarla desde la ciudad destino hacia la ciudad inicial
    ruta.reverse()
    
    return ruta        

def evaluar_opciones_de_transporte(de: str, a: str, archivo: str = 'rutas.txt'):
    '''
    Recibe una ciudad inicial, una ciudad destino, y un archivo de rutas (opcional),
    Crea 2 grafos (Uno para la capacidad de carga y otro para el precio), aplica el
    algoritmo de dijkstra, y retorna cual es la ruta a seguir con su mayor cuello de
    botella y precio total.

    Parameters
    ----------
    de : str
        Ciudad inicial.
    a : str
        Ciudad destino.
    archivo : str, optional
        Archivo de rutas a leer. Por defecto es 'rutas.txt'.

    Returns
    -------
    mayor_cuello_de_botella : int
        Mayor cuello de botella de capacidad de carga para la ruta óptima.
    precio_total : int
        Menor precio de costo para la ruta óptima.
    ruta : list
        Lista de las ciudades de la ruta óptima.

    '''
    
    # Guardo los datos del archivo en una lista para llenar el Grafo
    datos = abrir_archivo(archivo)
    
    
    '''
    ==========================
    Grafo Capacidades de Carga
    ==========================
    '''
    # Creo un Grafo y lo lleno con los datos del archivo (Ponderación: Capacidades de Carga)
    grafo_capacidades_de_carga_maxima = completar_grafo(datos)
    
    # Aplico dijkstra y guardo el mayor cuello de botella
    mayor_cuello_de_botella = obtener_mayor_capacidad_carga(grafo_capacidades_de_carga_maxima, de, a)
    
    
    '''
    =============
    Grafo Precios
    =============
    '''
    # Inicializo un Grafo para los precios mínimos
    grafo_precios_minimos = Grafo()
    
    for linea in datos:
        de_ciudad = linea[0]
        a_ciudad = linea[1]
        peso = linea[2]
        precio = linea[3]
        
        if peso >= mayor_cuello_de_botella:
            '''
            Si la capacidad de carga de la Arista es mayor o igual al cuello de botella,
            se agregan al Grafo ambos Vértices con su Arista.
            '''
            '''
            Lleno el grafo solo con los vértices y aristas que tengan un cuello de botella 
            mayor o igual al obtenido en el procesamiento anterior de dijkstra.
            '''
            grafo_precios_minimos.agregarArista(de_ciudad, a_ciudad, precio)
    
    # Aplico dijkstra y guardo el menor precio
    precio_total = obtener_menor_precio(grafo_precios_minimos, de, a)
    
    # Obtengo la ruta a seguir
    ruta = obtener_ruta(grafo_precios_minimos, de, a)
    
    '''Una vez procesado todo, retorno el mayor cuello de botella (int), el menor precio (int), y la ruta a seguir.'''
    return mayor_cuello_de_botella, precio_total, ruta