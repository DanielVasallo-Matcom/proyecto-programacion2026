from persistencia import cargar_datos, guardar_datos
from consola import (
    listar_eventos,
    agregar_evento,
    eliminar_evento,
    ver_detalles,
    mostrar_asignaturas_disponibles
)

def main():
    eventos = cargar_datos()

    while True:
        print("\nPLANIFICADOR DOCENTE")
        print("1. Listar asignaturas")
        print("2. Agregar asignatura")
        print("3. Eliminar asignatura")
        print("4. Ver detalles")
        print("5. Asignaturas disponibles")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            listar_eventos(eventos)
        elif opcion == "2":
            agregar_evento(eventos)
        elif opcion == "3":
            eliminar_evento(eventos)
        elif opcion == "4":
            ver_detalles(eventos)
        elif opcion == "5":
            mostrar_asignaturas_disponibles()
        elif opcion == "6":
            guardar_datos(eventos)
            print("Datos guardados. Programa finalizado.")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()