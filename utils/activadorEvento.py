import pygame
from utils.obtenerFuente import get_font
from utils.contarMejoras import contarMejoras
from utils.actualizar_variables_globales import actualizar_bardos,actualizar_druidas
from utils.actualizarProducciones import actualizar_producciones


def activador_evento(evento_guerra, evento_despertar_ruinas, partida,trad,GUERRA_TICK,DESPERTAR_TICK,screen,fondo_actual,aldeano,lenyador,bardo,mago,clerigo,druida,event):
    if not evento_despertar_ruinas.activo and event.type == GUERRA_TICK and evento_guerra.sucedeEvento():
        mensaje = get_font(20).render(f'{trad.t("the_event")} {trad.t("war_event")} {trad.t("has_begun")}\n{trad.t("war_event_desc")}', True, (0, 255, 0))
        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
        pygame.display.update()
        pygame.time.delay(1500)  
        if (round(contarMejoras.contarSoldados(partida) < 5 * evento_guerra.multiplicador)):
            evento_guerra.efectoEvento(partida,True)
            screen.fill((0, 0, 0))
            screen.blit(fondo_actual)
            mensaje = get_font(20).render(f'{trad.t("lost_war")}', True, (255, 0, 0))
            screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
            pygame.display.update()
            pygame.time.delay(1500)  
            partida.eventos.append(evento_guerra.nuevaInstancia())
            actualizar_producciones(partida)
            actualizar_bardos(partida,aldeano,lenyador,bardo)
            actualizar_druidas(partida,mago,clerigo,druida)
            
            return True
        
        
        evento_guerra.efectoEvento(partida,False)
        screen.fill((0, 0, 0))
        screen.blit(fondo_actual)
        mensaje = get_font(20).render(trad.t("won_war"), True, (0, 255, 0))
        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
        pygame.display.update()
        pygame.time.delay(1500)

        return False

    elif not evento_guerra.activo and event.type == DESPERTAR_TICK and evento_despertar_ruinas.sucedeEvento(): 
        evento_despertar_ruinas.efectoEvento(partida,True)
        
        mensaje = get_font(20).render(f'{trad.t("the_event")} {trad.t("ruins_event")} {trad.t("has_begun")}\n{trad.t("ruins_event_desc")}', True, (0, 255, 0))
        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
        pygame.display.update()
        pygame.time.delay(1500)  
        partida.eventos.append(evento_despertar_ruinas.nuevaInstancia())
        return True
    
    
    return False