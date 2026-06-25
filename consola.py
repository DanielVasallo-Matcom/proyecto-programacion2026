from datetime import datetime, timedelta
from models import ASIGNATURAS, crear_evento
from validaciones import hora_valida, hay_conflicto, obtener_huecos


def mostrar_asignaturas_disponibles():
    print("\nAsignaturas disponibles:")
    for nombre, datos in ASIGNATURAS.items():
        print(f"\n- {nombre}")
        print(f"Aula: {datos['aula']}")
        print(f"Profesores: {', '.join(datos['profesores'])}")
        print(f"Requisito: {datos['requisito']}")


def listar_eventos(eventos):
    if not eventos:
        print("No hay asignaturas planificadas.")
        return

    for i, e in enumerate(eventos, 1):
        print(f"{i}. {e['asignatura']} | {e['inicio']} - {e['fin']}")


def agregar_evento(eventos):
    mostrar_asignaturas_disponibles()

    nombre = input("\nAsignatura: ")

    if nombre not in ASIGNATURAS:
        print("Asignatura invalida")
        return

    profesores = ASIGNATURAS[nombre]["profesores"]

    print("\nProfesores disponibles:")
    for i, p in enumerate(profesores, 1):
        print(f"{i}. {p}")

    try:
        opcion_prof = int(input("Seleccione profesor: ")) - 1
        profesor = profesores[opcion_prof]
    except Exception:
        print("Seleccion invalida")
        return

    requisito = ASIGNATURAS[nombre]["requisito"]
    respuesta = input(f"Tienes el requisito ({requisito})? (si/no): ")

    if respuesta.lower() != "si":
        print("No puedes entrar al aula sin el requisito.")
        return

    huecos = obtener_huecos(eventos)

    print("\nHuecos disponibles:")
    for h in huecos:
        print("-", h)

    try:
        hora = int(input("Hora de inicio (8,10,12,14,16): "))
    except Exception:
        print("Hora invalida")
        return

    if not hora_valida(hora):
        print("Horario invalido")
        return

    inicio = datetime.strptime(f"{hora}:00", "%H:%M")
    fin = inicio + timedelta(hours=2)

    aula = ASIGNATURAS[nombre]["aula"]

    if hay_conflicto(eventos, inicio, fin, aula, profesor):
        print("Conflicto de aula o profesor")
        return

    evento = crear_evento(
        nombre,
        inicio.strftime("%H:%M"),
        fin.strftime("%H:%M"),
        profesor
    )

    eventos.append(evento)
    print("Clase agregada correctamente.")


def eliminar_evento(eventos):
    listar_eventos(eventos)

    try:
        indice = int(input("Numero de asignatura a eliminar: ")) - 1
        eliminado = eventos.pop(indice)
        print(f"{eliminado['asignatura']} eliminada.")
    except Exception:
        print("Seleccion invalida")


def ver_detalles(eventos):
    listar_eventos(eventos)

    try:
        indice = int(input("Numero de asignatura: ")) - 1
        e = eventos[indice]

        print("\nDetalles:")
        for k, v in e.items():
            print(f"{k}: {v}")
    except Exception:
        print("Seleccion invalida")