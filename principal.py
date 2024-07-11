import funciones as fn
import statistics

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez",
                "Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]


sueldos= {trabajador:0 for trabajador in trabajadores }

while True:
    try:
        print("---   Menu analisis sueldos  ---\n")

        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5.- Salir del programa ")

        opcionMenu=int(input("Ingrese una opción : "))
       
        if opcionMenu==1:
           sueldos = fn.asignar_sueldos_aleatorios(trabajadores)
           print(" Sueldos aleatorios asignados")

        elif opcionMenu==2:
            print("")
            fn.clasificar_sueldos(sueldos)
            

        elif opcionMenu==3:
            fn.ver_estadísticas(sueldos)
            print()

        elif opcionMenu==4:
            fn.reportes_sueldos(sueldos)
            print()

        elif opcionMenu==5:
            print("Finalizando programa...")
            print(" Desarrollado por Paulina Zúñiga ")
            print(" Rut: 16.777.587-K")
            break
        else:
            print(" Ingrese una opción valida.")
    except ValueError:
        print(" Ingrese solo numeros")
    except Exception as e:
        print(e)
    except:
        print(" Ocurrio un error")

    