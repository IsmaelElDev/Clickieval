import pygame
from utils.obtenerFuente import get_font

def verificarDurEventos(screen,evento_despertar_ruinas,evento_guerra,partida,trad,current_time):
    if evento_despertar_ruinas.verificarDuracion(partida,current_time) == True:
        mensaje = get_font(20).render(f'{trad.t("the_event")} {trad.t("ruins_event")} {trad.t("has_ended")} ', True, (0, 255, 0))
        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
        pygame.display.update()
        pygame.time.delay(1500)  
    elif evento_guerra.verificarDuracion(partida,current_time) ==True:
        mensaje = get_font(20).render(f'{trad.t("the_event")} {trad.t("war_event")} {trad.t("has_ended")} ', True, (0, 255, 0))
        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
        pygame.display.update()
        pygame.time.delay(1500)  