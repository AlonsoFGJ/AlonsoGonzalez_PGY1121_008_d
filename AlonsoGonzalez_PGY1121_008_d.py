import numpy as np
import os
import funciones as fp
import os

lista_rut=[]


while True:
    opcion = fp.menu()
    if opcion == 1:
        fp.verificar_rut()
        fp.opcion1()
    elif opcion == 2:
        os.system("cls")
        fp.opcion2()
    elif opcion == 3:
        fp.opcion3()
    elif opcion == 4:
        os.system("cls")
        fp.opcion4()
    else:
        print("""Adios!! c:
        (Sistema creado por Alonso Fabian González Jara 11/07/2023)""")