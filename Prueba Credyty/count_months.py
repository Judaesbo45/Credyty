# se uso la libreria calendar para el analisis de los meses
import calendar

# Esta funcion devuelve una lista de tuplas que contiene el mes de un año que inicia en domingo
def list_months():
    # Se inicia una lista vacia
    year_month = []

    # Se itera sobre el rango definido
    for year in range(1901, 2001):

        # Se itera sobre los meses del año
        for month in range(1,13):

            # Se instancia un objeto tipo calendar  con mes y año
            # Ademas se toma el primer elemento de la lista generada como primer dia
            month_firstday = calendar.monthcalendar(year, month)[0]

            # Se pregunta si el dia inicial es domingo
            if (month_firstday[calendar.SUNDAY] == 1):

                # Se añade la tupla a la lista
                year_month.append((year, month))
                
    # Se realiza el conteo total de los meses y se devuelve la lista de los mismos para mas utilidad
    count = len(year_month)
    return year_month, count

[all_months, amount] = list_months()
print(amount)
