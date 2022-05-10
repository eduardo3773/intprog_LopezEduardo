import json
ruta = 'sem11\FUno.json'
def mostrar(ruta):
	archivo = open(ruta, "r", encoding="UTF-8")  # ruta va sin "". Con esto asignamos a archivo lo que se lea en ruta
	archivos = json.load(archivo)              # Cargamos en archivos el contenido de archivo
	archivo.close
	return archivos
def total():
	a = 0
	ab = mostrar(ruta)
	print("Los tres primeros clasificados son: ")
	print("--------------------------")
	for i in range(3):
		a = a + 1
		print("Puesto numero ", a, ":" )
		print("Nombre: ", ab["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][i]["Driver"]["givenName"], "-","Apellido: ", ab["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][i]["Driver"]["familyName"]) # [clave], [numero si dentro de esa clave hay una lista].
		print("Posicion: ", ab["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][i]["position"], "Victorias: ", ab["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][i]["wins"])
		print("--------------------------------------------------------------")

if (__name__ == "__main__"):
	total()

	


