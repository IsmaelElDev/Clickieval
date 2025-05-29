import pygame
from utils.formatearNumero import formatear_numero
from utils.obtenerFuente import get_font

# Función tooltip_mejoras simplificada:
def tooltip_mejoras(trad,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey,aldeano_rect,lenyador_rect,arquero_rect,picaro_rect,mago_rect,bardo_rect,soldado_rect,clerigo_rect,druida_rect,bruja_rect,noble_rect,princesa_rect,reina_rect,rey_rect,upgrade_list_rect,screen,scroll_y):
    mouse_pos = pygame.mouse.get_pos()
    
    # Solo mostrar tooltips cuando el ratón está en el área de mejoras
    if not upgrade_list_rect.collidepoint(mouse_pos):
        return
        
    # Calcular posición relativa del ratón
    rel_x = mouse_pos[0] - upgrade_list_rect.x
    rel_y = mouse_pos[1] - upgrade_list_rect.y + scroll_y
    
    # Comprobar cada área de mejora
    
    # Aldeano
    if aldeano_rect.collidepoint(rel_x, rel_y) and aldeano.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(aldeano.produccion))} {trad.t("gold_per_second")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Leñador
    if lenyador_rect.collidepoint(rel_x, rel_y) and lenyador.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(lenyador.produccion))} {trad.t("wood_per_second")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Arquero
    if arquero_rect.collidepoint(rel_x, rel_y) and arquero.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(arquero.produccion))} {trad.t("gold_per_second")} \n{trad.t("and")} {trad.t("per_click")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Pícaro
    if picaro_rect.collidepoint(rel_x, rel_y) and picaro.locked == False:
        texto = f'{trad.t("produces_between")} \n{formatear_numero(round(picaro.min_produccion))} {trad.t("and")} {formatear_numero(round(picaro.max_produccion))} {trad.t("gold_per_min")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Mago
    if mago_rect.collidepoint(rel_x, rel_y) and mago.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(mago.produccion))} {trad.t("magic_per_second")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Bardo
    if bardo_rect.collidepoint(rel_x, rel_y) and bardo.locked == False:
        texto = f'{trad.t("prod_bard")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Soldado
    if soldado_rect.collidepoint(rel_x, rel_y) and soldado.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(soldado.produccion))} {trad.t("gold_per_click")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Clerigo
    if clerigo_rect.collidepoint(rel_x, rel_y) and clerigo.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(clerigo.produccion))} {trad.t("magic_per_second")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return

    # Druida
    if druida_rect.collidepoint(rel_x, rel_y) and druida.locked == False:
        texto = f'{trad.t("prod_cleric")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Bruja
    if bruja_rect.collidepoint(rel_x, rel_y) and bruja.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(bruja.produccion))} {trad.t("gold_per_second")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Noble
    if noble_rect.collidepoint(rel_x, rel_y) and noble.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(noble.produccion))} {trad.t("gold_per_second")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Princesa
    if princesa_rect.collidepoint(rel_x, rel_y) and princesa.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(princesa.produccion))} {trad.t("gold_per_click")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Reina
    if reina_rect.collidepoint(rel_x, rel_y) and reina.locked == False:
        texto = f'{trad.t("produces")} {formatear_numero(round(reina.produccion))} {trad.t("gold_per_second")}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Rey
    if rey_rect.collidepoint(rel_x, rel_y) and rey.locked == False:
        texto = f'{trad.t("prod_king")} {round(rey.produccion)}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return