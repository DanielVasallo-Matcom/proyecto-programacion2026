from datetime import datetime

def hora_valida(hora):
    return hora in [8, 10, 12, 14, 16]

def hay_conflicto(eventos, inicio, fin, aula, profesor):
    for e in eventos:
        ei = datetime.strptime(e["inicio"], "%H:%M")
        ef = datetime.strptime(e["fin"], "%H:%M")

        if inicio < ef and fin > ei:
            if e["aula"] == aula or e["profesor"] == profesor:
                return True
    return False

def obtener_huecos(eventos):
    ocupados = []

    for e in eventos:
        inicio = datetime.strptime(e["inicio"], "%H:%M").hour
        fin = datetime.strptime(e["fin"], "%H:%M").hour
        ocupados.append((inicio, fin))

    huecos = []
    hora = 8

    while hora < 18:
        libre = True

        for ini, fin in ocupados:
            if hora < fin and hora + 2 > ini:
                libre = False
                break

        if libre and hora + 2 <= 18:
            huecos.append(f"{hora}:00 - {hora+2}:00")

        hora += 2

    return huecos