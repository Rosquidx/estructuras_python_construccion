from dataclasses import dataclass
import random

@dataclass(order=True) #Compara string con stri,g int con int
# Pueden no tener guardada la información.
# frozen=True, INMUTABLE, no se puede cambiar
class JugadorDataClass:
    competicion:str = ''
    goles:int = 0 
    partidos:int = 0
    promedio:int = 0
    nombre:str = ''

    def obtener_goles(self):
        return self.promedio*self.partidos

    def mostrar(self):
        return f"{self.nombre} juega en {self.competicion}"


@dataclass(frozen=True, order=True)
class empleadoNutresa:
    nombre:str = ''
    compania:str = ''
    edad:int = 0
    cargo:str = ''
    precio:int = 0

    def numeroFavorito(self) -> float:
        return random.randint(1, 100)

    def mensajeEnviar(self) -> str:
        return f"La empleada {self.nombre} de la compañia {self.compania} su edad es {self.edad}, su cargo: {self.cargo} y al mes gana: {self.precio}"