"""Tareas realizadas:
- Contar en ronda de 1 en 1.
- Controlar límite de personas en ronda.
- Detectar cuenta divisible por 8 y cambiar en ese momento sentido de giro ronda

Tareas pendientes:
- Detectar cuenta divisible por 11 y saltar 1 persona, siguiendo mismo sentido de giro
Ej, si está contando horario la persona 8, la siguiente en contar deberá ser la 10; si es antihorario, la 6

- Permitir ingresar ctd de personas en ronda y límite de cuenta por consola, en lugar de indicarlos de forma fija
Ej: int(input("Personas en la ronda: "))

- Si el límite de cuenta es menor a la cantidad de personas en la ronda, no efectuar la cuenta, solo mostrar
en su lugar un mensaje de error con print.

"""
#TAREA, CORREGIR EL RANDOM.RANDINT
import random

PERSONAS = int(input("ingrese la cantidad de personas que participaran en la ronda: "))  #segundo punto
LIMITE_CUENTA = int(input("ingrese hasta que numero quieren contar: "))
cuenta = 0
persona = random.randint(1,PERSONAS)
giro = "horario"
for ciclo in range(LIMITE_CUENTA):
    if (LIMITE_CUENTA < PERSONAS):
        print("Error: El numero de personas en la ronda excede al numero hasta el cual se quiere contar.")
        break    
    
    cuenta = cuenta + 1 # se aumenta en 1 contador general

    if (giro == "horario"):
        if (persona == PERSONAS):
            persona = 0
        if (persona >= PERSONAS):
            persona = 1
        persona = persona + 1 # se suma 1 a contador de persona
    else:
        if (persona == 1):
            persona = PERSONAS + 1
        if (persona == 0):
            persona = PERSONAS   # En esta parte personas esta en decremento, si llega a 0, tiene que volver a 10.
        persona = persona - 1 # se resta 1 a contador de persona
    
    print(persona, cuenta)

    if (cuenta % 11 == 0 and cuenta % 8 == 0):
        if (giro == "horario"): # salta a la siguiente persona. Si queremos que salte antes de decir el numero divisible, movemos
            giro = "antihorario"
            persona = persona - 1    #Aca lleva -1 ya que queremos que persona saltee 1 puesto hacia abajo, con este -1 y el - 1 que esta  
        else:                                # antes del print lo logra
            giro = "horario"
            persona = persona + 1   # Aca queremos que saltee 1 hacia arriba, con este +1 y el +1 antes del print lo logra 
        continue
    
    if (cuenta % 11 == 0):  # con esto cumplo lo de si una persona dice un numero divisible por 11,
        if (giro == "horario"): # salta a la siguiente persona. Si queremos que salte antes de decir el numero divisible, movemos
            persona = persona + 1  # este if arriba del print
        else: 
            persona = persona - 1
    
    if (cuenta % 8 == 0): # cuenta es perfectamente divisible por 8
        if (giro == "horario"):
            giro = "antihorario"
        else:
            giro = "horario"
    
  
   


