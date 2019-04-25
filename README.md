# Prueba Credyty

## En el presente repositorio se agregaron dos archivos escritos en Python 3. 
## Estos archivos contienen la solucion al problema de las tripletas de pitagoras, retornando el producto de los tres valores encontrados y la solucion  al problema del conteo de numero de los meses que inician con domingo a lo largo del siglo 20.

# - Solucion al problema de las tripletas:
## Para solucionar este problema, se itera una lista ordenada de 1 hasta la mitad del resultado de la suma de la tripleta deseados, desde sus extremos opuestos. Lo anterior con el fin de hallar la pareja que produce el resultado deseado.

# - Solucion al problema del conteo de meses:
## Para resolver este problema, se utilizo la libreria nativa de python "Calendar" que permite generar calendarios ingresando el año y numero de mes. Usando los resultados de iterar al lo largo del rango de años establecido, mientas a su vez se itera sobre los 12 meses, se pregunta usando las funciones del calendario si el mes de ese año inicia en domnigo, en caso de ser positiva la respuesta, se almacena la misma en una lista de tuplas. Cuando es terminada la evaluacion de todos los meses, se verifica la longitud de la lista y asi se obtiene el numero total de meses.
