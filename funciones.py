import numpy as np
import os
import time

asientos = np.zeros((10,10), int)

lista_rut=[]

cont_plat=0
cont_gold=0
cont_silv=0
cont_total=0

total_plat = cont_plat * 120000
total_gold = cont_gold * 80000
total_silv = cont_silv * 50000

total_total = total_plat + total_gold + total_silv
def menu():
        while True:
            try:
                print("""Ver menú
                1.- Comprar entradas
                2.- Mostrar ubicaciones disponibles
                3.- Ver listado de asistentes
                4.- Mostrar ganancias totales
                5.- Salir""")
                opcion = int(input("Ingrese una opcion: "))
                if opcion>=1 and opcion<=5:
                    return opcion
                else:
                    print("Error! Debe elegir una opcion")
            except:
                print("Error! Debe ser un numero de la lista")  

def verificar_rut():
    while True:
        try:
            rut = int(input("Ingrese su RUT (Sin guion, puntos ni dígito verificador): "))
            if rut >= 10000000 and rut <= 99999999:
                lista_rut.append(rut)
                return rut
            else:
                print("Ingrese un RUT valido")
        except:
            print("Error! Debe ingresar digitos")


def opcion1():
    while True:
        try:
            cant_ent = int(input("Ingrese la cantidad de entradas a comprar (1 o 3): "))
            os.system("cls")
            if cant_ent >=1 and cant_ent <=3:
                os.system("cls")
                for h in range(cant_ent):
                    for x in range(10):
                        print(f"Fila {x+1} ", end="")
                        for y in range(10):
                            print(asientos[x][y], end=" ")
                        print()
                    print("""                               _______
                                |PRECIOS|
                    Platinum, $120.000 - Asientos del 1 al 20
                    Gold, $80.000 - Asientos del 21 al 50
                    Silver, $50.000 - Asientos del 51 al 100""")
                    fila = int(input("Ingrese fila (1 al 10): "))
                    columna = int(input("Ingrese columna (1 al 10): "))
                    os.system("cls")
                    fila-=1                    
                    columna-=1                                                        
                    if asientos[fila][columna]==0:
                        asientos[fila][columna]=1 
                        return fila
                    else:
                        os.system("cls")
                        print("No está disponible!")
            else:   
                print("Error! Debe elegir entre 1 o 3 entradas")
        except:
            print("Error! La cantidad de entradas deben ser digitadas")

#                        if fila == 0 or fila == 1:
#                                cont_plat += 1
#                        elif fila == 2 or fila <= 4:
#                                cont_gold += 1
#                        else:
#                            if fila == 5 and fila <= 9:
#                                cont_silv += 1


def opcion2():
    for x in range(10):
        print (f"Fila {x+1} ", end="")
        for y in range(10):
            print(asientos[x][y], end=" ")
        print()
    time.sleep(3)

def opcion3():
    print("Lista de asistentes: ", lista_rut.sort)

def opcion4():
    os.system("cls")
    print(f"""             |-------------------------------------------------|
             | Tipo entrada    |     Cantidad    |    Total    |
             |Platinum $120.000|         {cont_plat}       |      {total_plat}      |
             |Gold     $80.000 |         {cont_gold}       |      {total_gold}      |
             |Silver   $50.000 |         {cont_silv}       |      {total_silv}      |
             |TOTAL            |         {cont_total}       |      {total_total}      |
             |-------------------------------------------------|""")
    time.sleep(3)