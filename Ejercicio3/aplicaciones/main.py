from procesamiento import evaluar_opciones_de_transporte

ciudadInicial = input("Ingrese la ciudad inicial: ")
ciudadDestino = input("Ingrese la ciudad destino: ")

mayor_cuello_de_botella, menor_precio, ruta = evaluar_opciones_de_transporte(ciudadInicial, ciudadDestino)

print(f"\nPara ir de {ciudadInicial} a {ciudadDestino}, seguir esta ruta:\n{ruta}")
print(f"Mayor cuello de botella: {mayor_cuello_de_botella}")
print(f"Menor precio: {menor_precio}")