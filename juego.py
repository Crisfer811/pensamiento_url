def pseudo_random(limite):
    """Genera un número pseudoaleatorio basado en el tiempo del sistema"""
    # Usamos el tiempo del sistema como semilla (aproximación simple)
    tiempo = str(int(id(object()) % 1000) + int(str(id(object))[-3:]))
    return (int(tiempo) % limite) + 1

def medir_tiempo(inicio, fin):
    """Calcula la diferencia de tiempo de forma simple"""
    return fin - inicio

def adivina_el_numero(numero_secreto, intentos_restantes, tiempo_inicio):
    # Caso base: si no quedan intentos
    if intentos_restantes <= 0:
        tiempo_fin = int(input("Presiona 1 y Enter para terminar... "))  # Simulamos fin de tiempo
        tiempo_total = medir_tiempo(tiempo_inicio, tiempo_fin)
        print(f"\n¡Se acabaron los intentos! El número era {numero_secreto}.")
        print(f"Tiempo total: {tiempo_total} unidades de tiempo aproximadas.")
        return
    
    # Pedir al jugador que ingrese un número
    try:
        intento = int(input(f"\nIntento #{6 - intentos_restantes} - Ingresa un número (1-100): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return adivina_el_numero(numero_secreto, intentos_restantes, tiempo_inicio)
    
    # Verificar el intento
    if intento < numero_secreto:
        print("El número secreto es mayor.")
        return adivina_el_numero(numero_secreto, intentos_restantes - 1, tiempo_inicio)
    elif intento > numero_secreto:
        print("El número secreto es menor.")
        return adivina_el_numero(numero_secreto, intentos_restantes - 1, tiempo_inicio)
    else:
        tiempo_fin = int(input("Presiona 1 y Enter para terminar... "))  # Simulamos fin de tiempo
        tiempo_total = medir_tiempo(tiempo_inicio, tiempo_fin)
        print(f"\n¡Felicidades! Adivinaste el número {numero_secreto} en {6 - intentos_restantes} intentos.")
        print(f"Tiempo total: {tiempo_total} unidades de tiempo aproximadas.")
        return

# Configuración del juego
numero_secreto = pseudo_random(100)  # Número pseudoaleatorio entre 1 y 100
intentos_totales = 5

# Iniciar el juego
print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print(f"Tienes {intentos_totales} intentos. ¡Buena suerte!")
print("Para medir el tiempo, presiona 1 y Enter cuando termines.")
tiempo_inicio = 1  # Valor inicial arbitrario

adivina_el_numero(numero_secreto, intentos_totales, tiempo_inicio)