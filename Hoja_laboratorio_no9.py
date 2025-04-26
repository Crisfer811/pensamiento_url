# Ejercicio 1
def es_par_o_impar(n):
    if n % 2 == 0:
        print(f"El número {n} es par")
    else:
        print(f"El número {n} es impar")


# Ejercicio 2
def suma_lista(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

# Ejercicio 3
def cuenta_regresiva(n):
    if n >= 0:
        print(n)
        cuenta_regresiva(n - 1)


# Ejercicio 4
def cuenta_ascendente(n, actual=1):
    if actual <= n:
        print(actual)
        cuenta_ascendente(n, actual + 1)


# Ejercicio 5
def suma_hasta(n):
    if n == 1:
        return 1
    else:
        return n + suma_hasta(n - 1)


# Ejercicio 6
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Ejercicio 7
def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        primero = lista[0]
        menor_del_resto = minimo(lista[1:])
        return primero if primero < menor_del_resto else menor_del_resto


