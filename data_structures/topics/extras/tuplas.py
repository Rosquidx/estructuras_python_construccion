from typing import NamedTuple


def publicar(datos, nombre):
    competicion, goles, partidas, promedio = datos
    return f"{nombre} en {competicion} jugó {partidas} con un promedio {promedio} y metió {goles} goles"


def goles(datos, nombre):
    goles = datos[1]
    return (nombre, goles)


class Jugador(NamedTuple):
    competicion: str
    goles: int
    partidos: int
    promedio: float
    nombre: str


class InformacionEstudiante(NamedTuple):
    universidad: str
    promedio: float
    nombre: str
    apellido: str
    comidafavorita: str
    nota1: int
    nota2: int
    
    def promedioFun(self) -> float:
        return self.nota1/self.nota2

    def mensajeEnviar(self) -> str:
        return f"El estudiante {self.nombre} {self.apellido} tiene un promedio de {self.promedio}, es estudiante del {self.universidad} y su comida favorita es: {self.comidafavorita} tiene dos notas de: {self.nota1} {self.nota2}"
