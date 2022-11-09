'''
Aplicación para evaluar opciones de transporte
'''

from procesamiento import evaluar_opciones_de_transporte

ciudadInicial = input("\nIngrese la ciudad inicial: ")
ciudadDestino = input("Ingrese la ciudad destino: ")

mayor_cuello_de_botella, precio_total, ruta = evaluar_opciones_de_transporte(ciudadInicial, ciudadDestino)


print(f"\nPara ir de {ciudadInicial} a {ciudadDestino}, seguir esta ruta:")

cantidad_ciudades = len(ruta)
ciudades_recorridas = 0 # Contador utilizado para el formato de mostrar las ciudades

# Recorro la lista de ciudades de la ruta, para mostrar el recorrido
for ciudad in ruta:
    if ciudades_recorridas < cantidad_ciudades-1:
        print(f"{ciudad} -> ", end="")
        ciudades_recorridas += 1
    else:   # Si es la última ciudad, no se escribe la flecha
        print(f"{ciudad}")


print(f"\nMayor capacidad de carga: {mayor_cuello_de_botella}")
print(f"Precio total: ${precio_total*1000}")