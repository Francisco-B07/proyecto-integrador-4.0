def cargarLista():
    lista=[]
    for i in range(5):
        numero = int(input("Introduce un número entero: "))
        lista.append(numero)
    return lista


# funcion suma
def suma(lista):
    suma = 0
    for i in range(5):
        suma += lista[i] 
    return suma

# funcion promedio
def promedio(lista):
    promedio = suma(lista)/len(lista)    
    return promedio

# funcion máximo
def maximo(lista):
    max = 0
    for i in range(5):
        if(lista[i]>max):
            max = lista[i] 
    return max


def main():
    lista = cargarLista()
    print("El resultado de la suma es: ", suma(lista))
    print("El resultado del promedio es: ", promedio(lista))
    print("El máximo es: ", maximo(lista))

main()
