import os 
import msvcrt
import time 
from funciones import *
lista_ruts = []
lista_asientos = []
lista_cedula = []
os.system("cls")
while True:
    menu = mostrar_menu()
    if menu == 1:
        mostrar_menu()
    elif menu == 2:
        ver_escenario()
    elif menu == 3:
        lista_personas()
    elif menu == 4:
        ganancias_totales()
    else:
        break
