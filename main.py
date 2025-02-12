num= int(input("ingrese un numero entre el 1 al 9: "))
if(num <= 3):
    resultado = num * "I"
    numero =num
    print("El valor romano del numero",numero, resultado )
elif(num == 4):
    print("El numero 4 en romanos es: IV")
elif(num == 5):
    print("El numero 5 en romanos es: V")
elif(num == 6):
    print("El numero 6 en romanos es: VI")
elif(num == 7):
    print("El numero 7 en romanos es: VII")
elif(num == 8):
    print("El numero 8 en romanos es: VIII")
elif(num == 9):
    print("El numero 9 en romanos es: IX")
else:
    print("El numero elegido no esta dentro del rango")
