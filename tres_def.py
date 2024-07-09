#importar
import csv
import time
#declaracion de variables 
opcion=0
#declaracion de DEF
def menu():
    print("--Menu--")
    print("1.-Ingresar un miembro\n2.-Ver miembros\n3.-Modificar un meinbro\n4.-Salir del programa.")
def animacion():
    print("Saliendo del programa", end='')
    for h in range(3):
        print(".",flush=True,end='')
        time.sleep(0.5)