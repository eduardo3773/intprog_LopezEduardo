import random
promedio = 0
lista = []
numero = 1
a = random.randint(300,320)
for i in range(50):
    a = random.randint(300,320)
    lista.append(a)
    promedio = promedio + a

promedioT = promedio / 50
   
print("La lista de temperaturas es: ",lista)
print("El promedio de temperaturas es ", promedioT)


while True:
    numero = int(input("Ingrese la temperatura actual del horno: "))
    if numero == 0:
        print ("Has ingresado 0, se cierra el programa.")
        break
    if numero in range (299, 321):
        print("La temperatura es normal.")
    else:    
        if numero < promedioT:
            if numero + 100 < promedioT:
                print("Se encienden dos hornallas")
                
            elif numero + 100 > promedioT:
                print("Se enciende 1 hornallas")
                
        else:
            print("Se apagan las 2 hornallas")
            


