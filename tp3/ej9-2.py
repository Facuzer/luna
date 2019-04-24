import ej9
# Importo la función que cree anteriormente en otro archivo.
# Le pregunto al profesor cuantos ejercicios tiene en total su evaluación.
cantidadTotal = int(input(
    "Indique la cantidad de ejercicios totales del examen que \
    desea corregir: "))
# Le pregunto al profesor cuanto porcentaje es necesario tener para aprobar
# la evaluación.
porcentajeAprobacion = int(input(
    "Indique el porcentaje de ejercicios correctos necesarios para aprobar: "))
# Llamo a la función que cree en el otro archivo. Le paso los parámetros
# que anteriormente le pedí al profesor.
ej9.evaluarExamenes(cantidadTotal, porcentajeAprobacion)
