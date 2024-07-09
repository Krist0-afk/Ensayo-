#importar 
import tres_def as funciones
import csv
import time
#definir variables
flag = True 
user_1 = 'Cristobal'
contra1 = '1234'
opcion = 0
#comienda el codigo
print("---Bienvenido a la empresa de registro---");
user=input("Ingrese el usuario:\n");
contra=input("Ingrese la contraseña de su usuario:\n");
while flag == True:
 if user != user_1 and contra != contra1:
    time.sleep(0.5)
    print("ERROR\nVuelva a intentarlo");
    user=input("Ingrese el usuario:\n");
    contra=input("Ingrese la contraseña de su usuario:\n");

 elif user == user_1 and contra == contra1:
    flag = False
    time.sleep(0.5)
    print("Ha Ingresado de forma Correcta!")
    while opcion != 4:
      funciones.menu()
      try:
        opcion=int(input("Ingrese una de las opciones mostrdas por pantalla:\n"))
      except:
          print("ERROR\nVuelva a intentarlo.")   
      if opcion == 1:
        print
      if opcion == 2:
        print()
      if opcion == 3:
        print()
      if opcion == 4:
        funciones.animacion()              
