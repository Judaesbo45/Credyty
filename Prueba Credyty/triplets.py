from math import sqrt

# Esta funcion retorna la multiplicacion de la suma de una tripleta pitagoriga
# Recibe como parametro el resultado deseado de la suma
def pysum_triplet(sum_value):
    #se crea una lista que va hasta la mitad de la suma de las tripletas
    list = [x for x in range(1, int(sum_value/2))]
    #se definen dos indices para recorrer la lista de los extremos hacia adentro
    i = 1
    j = len(list) - 1

    #Se crea un ciclo para recorrer la totalidad de la lista
    while True:
        # Se definen todas las variables en funcion de a,b o la lista
        a = list[i]
        b = list[j]
        c = sqrt(a**2 + b**2)

        # si la suma de la tripleta es menor al numero deseado, se aumenta "a"
        if (a + b + c) < sum_value:
            i += 1

        # si la suma de la trimpleta es mayor al numero deseado, se disminuye "b"
        elif (a + b + c) > sum_value:
            j -= 1

        # una vez encontrados los valores, se sale de ciclo
        elif (a + b + c) == sum_value:
            print('Found it !')
            break
    # se calcula la multiplicacion deseada
    result = a*b*c
    print(i)
    return result

times_triplet = pysum_triplet(1000)
print(times_triplet)
