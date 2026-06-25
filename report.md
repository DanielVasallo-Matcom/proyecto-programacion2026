Tema del proyecto: Planificador Inteligente de Eventos

El Planificador Inteligente de Eventos es una aplicacion desarrollada en Python cuyo objetivo principal es la asignación eficiente de recursos limitados a eventos que ocurren en intervalos de tiempo específicos.Aquí cada evento representa una actividad la cual requiere recursos limitados para poder ejecutarse correctamente.Este proyecto simula un sistema real de gestión de horarios y recursos, aplicando conceptos de programación abordados a lo largo de todo el curso.

DOMINIO ELEGIDO

El dominio elegido para el proyecto es el de un sistema de planificación académica.En este contexto, el sistema se encarga de organizar clases dentro de una institución educativa gestionando la disponibilidad de aulas, profesores y recursos materiales.Este dominio refleja problemas reales en la planificación que ocurren constantemente tanto en universidades como en centros educativos.En este sistema, los eventos representan clases o sesiones académicas, y los recursos incluyen:
-Aulas disponibles
-Profesores
-Material educativo

Este entorno permite simular situaciones como:
-Un profesor no puede impartir dos clases al mismo tiempo
-Un aula que no puede ser utilizada por dos grupos simultaneamente
-Un estudiante que necesite materiales específicos para asistir a la clase

COMPONENTES DEL SISTEMA
Este sistema se compone de eventos, recursos y restricciones:

EVENTOS
Los eventos son la unidad principla de este sistema.Cada evento contiene la siguiente información:

-Nombre de la asignatura
-Hora de inicio
-Hora de finalización
-Profesor asignado
-Aula donde se realiza

Ejemplos de eventos:
-Programación
-Física
-Química

RECURSOS
Los recursos son todos los elementos necesarios para que un evento pueda realizarse correctamente.En este sistema académico los recursos incluyen:

-Aulas(Aula1,Laboratorio,Centro Deportivo,etc)
-Profesores(Juan,Pedro,Laura,etc)
-Materiales educativos(libros,calculadoras,bata de laboratorio,etc)

Estos recursos son finitos por lo que no pueden ser usados simultáneamente por múltiples eventos

RESTRICCIONES DEL SISTEMA
Las restricciones son el núcleo lógico del sistema, definen las reglas que determinan si un evento puede o no ser programado.Este proyecto implementa dos tipos de restricciones:

RESTRICCIONES DE CO-REQUISITO(INCLUSION)
Esta restricción establece que ciertos eventos requieran obligatoriamente la presencia de recursos específicos para poder realizarse. Si estos recursos no están disponibles o no son proporcionados, el evento no puede ser planificado

Ejemplos:
-La asignatura Programación requiere una computadora
-La asignatura Educación Física requiere ropa deportiva adecuada

Estas restricciones aseguran que los eventos solo se realicen cuando se cumplen las condiciones necesarias para su ejecución

RESTRICCIONES DE EXCLUSION MUTUA
Esta restricción establece que ciertos recursos no pueden ser utilizados simultáneamente en el mismo evento o en eventos que se solapan en el tiempo

Ejemplos:
-Un profesor no puede impartir dos clases al mismo tiempo
-Un recurso no puede ser compartido entre eventos incompatibles

FUNCIONALIDADES DEL SISTEMA
Este sistema cuenta con funcionalidades que permiten se uso completo

PLANIFICADOR DE EVENTOS
Esta función permite crear nuevos eventos siempre que se cumplan todas las condiciones

-Disponibilidad del aula
-Disponibilidad del profesor
-Cumplimiento de los requisitos del evento
-Ausencia de conflictos de horario

El sistema realiza validaciones automáticas antes de aceptar un evento

LISTAR EVENTOS
Esta función muestra todos los eventos actualmente programados en el sistema, indicando su asignatura, horario y recursos asignados.Permite al usuario tener una visión general del calendario completo

ELIMINAR EVENTOS
Permite eliminar un evento previamente creado. Al eliminarlo, los recursos asociados quedan automáticamente disponibles para otros eventos.Garantizando una correcta gestión del sistema

VER DETALLES DE EVENTOS
Permite consultar información detallada de un evento específico,incluyendo todos sus atributos:

-Asignatura
-Profesor
-Aula
-Horario
-Recursos utilizados

BUSQUEDA DE HUECOS
El sistema es capaz de analizar el calendario completo y sugerir los intervalos de tiempo disponibles donde se puede programar un nuevo evento sin conflictos.Esta funcionalidad mejora la eficiencia del sistema y ayuda a optimizar la planificación

INTERFAZ DE USUARIO
El sistema funciona mediante un interfaz de consola(CLI). El usuario puede interactuar con el sistema mediante un menú de opciones numeradas, lo que permite realizar acciones como:

-Agregar eventos
-Eliminar eventos
-Consultar eventos
-Ver asiganturas disponibles
-Guardar y salir del sistema

PERSISTENCIA DE DATOS
El sistema utiliza un archivo JSON llamado datos.json para almacenar toda la información relacionada con los eventos.Este archivo permite:

-Guardar el estado del sistema
-Recuperar eventos perviamente creados
-Mantener la información entre ejecuciones del programa

TECNOLOGIAS UTILIZADAS
El proyecto esta desarrollado utilizando las siguientes tecnologías:
-Python 3 como lenguaje principal
-Módulo datetime para el manejo de fechas y horas
-Módulo json para la persistencia de datos
-Programación mediante archivos separados

ESTRUCTURA DEL PROYECTO
El proyecto está organizado en diferentes módulos:

-main.py(punto de entrada de este sistema)
-consola.py(interfaz de usuario y lógica de interacción)
-models.py(define asiganturas y crea eventos)
-validaciones.py(reglas de conflictos y validacion de horarios)
-persistencia.py(manejo de almacenamiento en JSON)
-datos.json(archivo de almacenamiento de eventos)

COMO EJECUTAR EL PROYECTO
-en Visual Studio Code o cualquier otro lector de código ejcutar el archivo main.py

Este Planificador Inteligente de Eventos es un proyecto que permite aplicar los conceptos fundamentales de programación y la lógica computacional.Este sistema resuelve un problema real relacionado con la planificacion de recursos en entornos limitados, usando validaciones automáticas y estructuras de datos bien definidas.Sentando bases para sistemas más avanzados utilizados en el mundo real, como sistemas hospitalarios, universitarios o empresariales



