from django.shortcuts import render
from .extras.tuplas import InformacionEstudiante, publicar, goles, Jugador

from .extras.dataclases import JugadorDataClass, empleadoNutresa
# Create your views here.


def cargar_index(request):
    return render(
        request,
        'topics/index.html',
        {}
    )


'''TUPLAS: Son objetos que puede generar objectos de otros objetos y es inmutable.
Abre el tema a la prograamcion funcional, (x, y): Es un ejemplo de tupla, es muy diferente
# tener una tupla (255,0,0) a (0,0,255) -> es un contenedor podemos crearla simplemente separando valroes por (,)'''

'''
Cuando se utiliza una tupla algunas veces el parentesis es obligatorio, para separar los datos.
'''


def cargar_tuplas(request):

    goles1 = "liga 1", 1, 8, 0.12
    goles2 = ("champions", 1, 8, 0.75)

    nombre = "Mbappé"

    d3 = (2000,)  # Tupla generada, es de un solo elemento.
    d4 = ()
    d5 = goles1, goles2

    info = InformacionEstudiante(
        'Politecnico Jaime Isaza Cadavid', 4, 'Roberto', 'Cristal', 'Mazamorra', 4, 4)

    # Debe tener el numero exactyo de valores para rcrear la tupla
    j1 = Jugador('Champions', 4, 8, 0.9, 'Mbappé')

    universidad, promedio, nombre, apellido, comida, nota1, nota2 = info

    universidaddd = info[0]
    return render(
        request,
        'topics/tuplas.html',
        {
            'd1': publicar(goles2, nombre),
            'd2': goles(goles2, nombre),
            'd3': d3,
            'd4': d4,
            'd5': d5,
            'd6': goles1[1:6],
            'd7': j1,
            'infoGrande': info.mensajeEnviar,
            'promedio': info.promedioFun,
            'nombre': nombre,
            'info': info,
            'u': universidaddd
        }
    )


def cargar_dataclases(request):

    jugador = JugadorDataClass('Champion',
                               9,
                               12,
                               0.25,
                               'Mbappé')

    jugador.nombre = "Elias"

    jugador.casado = True

    jugador2 = JugadorDataClass('Champion',
                                3,
                                12,
                                0.25,
                                'Mbappé')

    jugador2.nombre = "Elias"

    jugador2.casado = True

    jugador3 = JugadorDataClass(promedio=0.88)

    empleado = empleadoNutresa(
        'Clara Ines Restrepo', 'Compañia Nacional de Chocolates', 45, 'Analista de Soporte Tecnico', 3500000)
    # comparacion = jugador == jugador2

    # compania = empleado[1]
    comparacion = jugador < jugador2
    return render(
        request,
        'topics/dataclases.html',
        {
            'j': jugador,
            'j2': jugador2,
            'c': comparacion,
            'j3': jugador3,
            'empleado': empleado,
            'nfavorito': empleado.numeroFavorito,
        }
    )


def cargar_dictionaries(request):

    jugadores = {
        'jugador1': {'Champion', 9, 0.25, 'Mbappé'},
        'jugador2': {'Liga Inglesa', 5, 0.25, 'Riollano'},
        'jugador3': {'Liga Española', 3, 0.5, 'Fernando Espinoza'},
        'jugador4': {'Liga Francesa', 10, 0.83, 'Marcus'},
    }

    jugadores['jugador1'] = ("Liga Alemana", 5, 10, 3.5, "Ferraro")
    jugadores['jugador6'] = ("Liga Colombiana", 8, 10, 6.5, "James"),


    class cualquierObjeto:
        def __init__(self, valor):
            self.valor = valor

    objecto1 = cualquierObjeto('hola')


    cosas = {}
    cosas['prenda'] = 'Traje rojo'
    cosas[3] = 'Numero 3'
    cosas[10.5] = 'Numero flotante'
    cosas[('nombre',1200)] = 'tupla'
    cosas[objecto1] = 'Es un objecto'
    cosas[True] = 'Es un true'
    # cosas[[1,2,3]] = 'Es una lista'
    # No se puede utilizar listas porque son mutables y los otros no, las listas cambian y modifician.


    return render(
        request,
        'topics/dictionaries.html',
        {
            'j1': jugadores['jugador1'],
            'j2': jugadores['jugador2'],
            'j3': jugadores.get('jugador3', 'No hay jugador, lo siento.'),
            'j4': jugadores.get('jugador1', 'INVALIDO'),
            'j5': jugadores.get('jugador18', ('Sin definir', 0, 0, 0, 'Sin definir')),
            'jugadores': jugadores,
            'o': objecto1,
            'cosas': cosas
        }
    )


def cargar_lists(request):
    return render(
        request,
        'topics/lists.html',
        {}
    )


def cargar_sets(request):
    return render(
        request,
        'topics/sets.html',
        {}
    )


def cargar_queues(request):
    return render(
        request,
        'topics/queues.html',
        {}
    )
