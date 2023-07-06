import numpy as np
import time 
import os
import msvcrt
lista_ruts = []
lista_asistentes = []
lista_asientos = []
lista_cedula = []
ganancia_total = 0
escenario = np.zeros((10,10),int)
def mostrar_menu ():
    while True:
        try:
            opc = int(input("""Bienvenido a creativos.cl:
            1. Comprar entradas.
            2. Mostrar ubicaciones disponibles.
            3. Ver listado de asistentes.
            4. Mostrar ganancias totales.
            5. Salir.
            Ingrese una opcion: """))
            if opc == 1:
                validar_compra_entrada()
                return mostrar_menu
            elif opc == 2:
                ver_escenario()
                time.sleep(5)
            elif opc == 3:
                lista_personas()
            elif opc == 4:
                ganancias_totales()
            else:
                print("Gracias por entrar hasta pronto!!:D")
                return        
                
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO!!")    

    
def validar_compra_entrada ():
     while True:
          try:
            cant_entrada = int(input("\t\t\tIndique cuantas entradas desea comprar entre 1 y 3: "))
            if cant_entrada >= 1 and cant_entrada <= 3:
                print("\t\t\tGracias por su compra a continuacion indique el asiento: ")
                while True:
                        try:
                            modelo = int(input("""Precio asientos:
                            1. Del asiento 1 a 20 su precio es $120.000 (PLATINUM)
                            2. Del asiento 21 a 50 su precio es $80.000 (GOLD)
                            3. Del asiento 51 a 100 su precio es 50.000 (SILVER)
                            Indique el asiento que desea reservar: """))
                            if modelo == 1:
                                validar_rut()
                                ver_escenario()
                                while True:
                                    try:
                                        asiento = int(input("Indique el asiento: "))
                                        if asiento >= 1 and asiento <= 20:
                                            print("Asiento",asiento,"reservado!!")
                                            time.sleep(3)
                                            os.system("cls")
                                            ganancia_total == 120000*cant_entrada
                                            lista_asistentes.append(asiento)
                                            return mostrar_menu()
                                        elif modelo == 2:
                                            print("Asiento",asiento,"reservado!!")
                                            time.sleep(3)
                                            os.system ("cls")
                                            ganancia_total == 80000*cant_entrada
                                            lista_asistentes.append(asiento)
                                            return mostrar_menu()
                                        elif modelo == 3:
                                            print("Asiento",asiento,"reservado!!")
                                            time.sleep(3)
                                            os.system("cls")
                                            ganancia_total == 50000*cant_entrada
                                            lista_asistentes.append(asiento)
                                            return mostrar_menu()
                                        else:
                                            print("ERROR debe ingresar almenos una opcion!!")
                                    except:
                                        print("ERROR DEBE INGRESAR UN NUMERO ENTERO")        
                            else:
                                print("ERROR!! DEBE INDICAR LAS OPCIONES DE 1 A 3!!") 
                        except:
                            print("ERROR DEBE INGRESAR UN NUMERO ENTERO!")                        
            else:
                print("Debe escoger entre 1 a 3 entradas para poder ingresar.!!")
          except:
              print("ERROR DEBE INGRESAR UN NUMERO ENTERO!!!")      


def ganancias_totales():
    ganancia_total*lista_asientos
    print("Total ganancias:$",ganancia_total)
    time.sleep (5)
    return mostrar_menu()
     
def validar_rut():
    while True:
        try:
            rut=int(input("Indique  su rut sin puntos: "))
            if rut >= 11111111 and rut >= 99999999:
                print("Rut valido!")
                return validar_rut
            else:
                print("RUT NO VALIDO!!")
                lista_ruts.append(rut) 
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO!!")        
    

def ver_escenario():
    for x in range (10):
        print(f" ",str(x+1), end=" ")
        for y in range(10):
            print(" ",escenario[x][y], end=" ")
        print()  
   

def lista_personas ():
    print("Asistentes:")
    print(lista_asistentes)
    time.sleep(3)
    return mostrar_menu()


