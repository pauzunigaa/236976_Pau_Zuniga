import random
import csv



def asignar_sueldos_aleatorios(trabajadores):
    sueldos_trabajadores={}

    for trabajador in trabajadores:
        sueldo=random.randint(300000,2500000)
        sueldos_trabajadores[trabajador] = sueldo
    return sueldos_trabajadores

def clasificar_sueldos(sueldos):
    menores_800={}
    entre_800_2={}
    superior_2={}

    acumulador_sueldo=0

    for trabajador,sueldo in sueldos.items():
        acumulador_sueldo=acumulador_sueldo+sueldo
        if sueldo <800:
            menores_800[trabajador]=sueldo
        elif sueldo<2000000:
            entre_800_2[trabajador]=sueldo
        else:
            superior_2[trabajador]=sueldo

    print("--- Lista de empleados --- \n")

    # menores a $800.000
    print(f"Nombre empleado","Sueldo")
    for trabajador,sueldo in menores_800.items():
        print(trabajador,sueldo)

    print(" Sueldos menores a  $800.000 :",len(menores_800))

    #entre $800.000 y $2.000.000
    print(f"Nombre empleado","Sueldo")
    for trabajador,sueldo in entre_800_2.items():
        print(trabajador,sueldo)

    print(" Sueldos entre $800.000 y $2.000.000 :",len(menores_800))
    
    # superior a $2.000.000
    print(f"Nombre empleado","Sueldo")
    for trabajador,sueldo in superior_2.items():
        print(trabajador,sueldo)

    print(" Sueldos superiores a $2.000.000 :",len(menores_800))


#def ver_estadísticas(sueldos):
    


def reportes_sueldos(sueldos):
    
    reportes_sueldos=[]
    for trabajador, sueldo in sueldos.items():
        descu_afp = sueldo*0.07
        descu_salud = sueldo*0.12
        sueldo_liquido=sueldo-descu_afp-descu_salud

        trabajador ={
            "Nombre empleado":trabajador,
            "Sueldo base":sueldo,
            "Descuento Salud":descu_salud,
            "Descuento AFP":descu_afp,
            "Sueldo Liquido":sueldo_liquido
        }

        reportes_sueldos.append(trabajador)
        print(reportes_sueldos)

    try:
        with open('archivo.csv','w',newline="") as archivo:
            escritor=csv.writer(archivo)
            escritor.writerow(["Nombre empleado","Sueldo base","Descuento Salud","Descuento AFP","Sueldo Liquido"])

            for trabajador in reportes_sueldos:
                escritor.writerow([trabajador["Nombre empleado"],trabajador["Sueldo base"],trabajador["Descuento Salud"],trabajador["Descuento AFP"],trabajador["Sueldo Liquido"]])
        print(" tu archivo 'reporte_sueldos se ha guardado con exito ") 
    except:
        print(" Tu archivo no se pudo guardar,intenta nuevamente")

