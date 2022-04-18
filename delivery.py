""""
Una persona trabaja como delivery en una pizzería de viernes a domingo. Percibe $ 300 por entrega los viernes y sábados, y $ 200 los domingos.
 Si suma al menos 20 entregas en la semana, obtiene un incentivo extra de $ 1000. Desea disponer de un resumen rápido por día y semana.

Etapas a realizar:

Solicitar por consola el ingreso del número de entregas realizadas día x día.
Mostrar un resumen de esas entregas y un subtotal de lo cobrado día x día.
Mostrar el total de entregas y lo ganado en toda la semana (sumando el premio si corresponde).
Consignas a respetar:

Utilizar al menos una lista, una tupla y una función.
Utilizar el control if (__name__ == "__main__") para iniciar el flujo principal de código.
Recordar:

Las tuplas son inmutables, no se puede modificar su contenido, por ende se aplican a elementos que no necesitan ser
 cambiados durante 
la ejecución de código (constantes para cálculos, nombres de días, meses, etc).
Se puede generar una lista vacía y luego ir agregando elementos a ella mediante el método append. """


#Viernes y sabado 300$ x entrega 
#Domingos 200$ x entrega
#Si entregas >= 20 +1000$ 

dias = ("Viernes", "sabado", "Domingo")
entre = []
total = []
a = -1
tot = 0
tota = 0
totales = 0
def entregas():
    global tot
    global tota
    gana = 0
    dia = int(input("Entregas realizadas el dia de hoy: "))
    gana = dia * 300
    tota = tota + dia
    tot = tot + gana
    entre.append(dia)
    total.append(gana)
if (__name__ == "__main__"):    
    for i in dias:
        entregas()

    for i in dias: 
        a = a + 1 
        print("El dia ",i, "se hicieron",entre[a],"entregas.", "Y las ganancias totales fueron de: ",total[a], "$" )
        print()
    totales = tota
    if tota >=20:
        tot = tot + 1000
        print("Has hecho mas de 20 entregas, cobraras un bonus de 1000 $")
        print()
    print("Has hecho",tota, "entregas esta semana. " "Y en total has ganado ",tot, "$")    



