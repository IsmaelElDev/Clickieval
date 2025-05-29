from entidades.evento import Evento
def contarEventos(partida):
    numevent = sum (1 for evento in partida.eventos if isinstance(evento, Evento))
    print(numevent)