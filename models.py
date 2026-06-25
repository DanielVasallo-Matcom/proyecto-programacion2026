ASIGNATURAS = {
    "Analisis Matematico": {
        "aula": "Aula 1",
        "profesores": ["Juan", "Pedro"],
        "requisito": "Libro de analisis"
    },
    "Logica": {
        "aula": "Aula 2",
        "profesores": ["Maria"],
        "requisito": "Cuaderno"
    },
    "Algebra": {
        "aula": "Aula 3",
        "profesores": ["Pablo"],
        "requisito": "Libro de algebra"
    },
    "Filosofia": {
        "aula": "Aula 4",
        "profesores": ["Ana"],
        "requisito": "Libro de filosofia"
    },
    "Educacion Fisica": {
        "aula": "Centro Deportivo",
        "profesores": ["Carlos"],
        "requisito": "Ropa deportiva"
    },
    "Programacion": {
        "aula": "Laboratorio",
        "profesores": ["Laura", "Sofia"],
        "requisito": "Computadora"
    },
    "Historia de Cuba": {
        "aula": "Aula 5",
        "profesores": ["Roberto"],
        "requisito": "Libro de historia"
    },
    "Economia Politica": {
        "aula": "Aula 6",
        "profesores": ["Elena"],
        "requisito": "Libro de economia"
    },
    "Fisica": {
        "aula": "Aula 7",
        "profesores": ["Miguel"],
        "requisito": "Calculadora"
    },
    "Quimica": {
        "aula": "Aula 8",
        "profesores": ["Daniel"],
        "requisito": "Bata de laboratorio"
    }
}

def crear_evento(nombre, inicio, fin, profesor):
    return {
        "asignatura": nombre,
        "inicio": inicio,
        "fin": fin,
        "profesor": profesor,
        "aula": ASIGNATURAS[nombre]["aula"]
    }