import pygame
from utils.obtenerFuente import get_font
from utils.contarMejoras import contarMejoras
from utils.formatearNumero import formatear_numero

def pintarMejoras(partida,trad,tarjetasMejora,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey,aldeano_surface,lenyador_surface,arquero_surface,picaro_surface,mago_surface,bardo_surface,soldado_surface,clerigo_surface,druida_surface,bruja_surface,noble_surface,princesa_surface,reina_surface,rey_surface,upgrade_list_surface,upgrade_list_rect,scroll_y):

    if partida.oro >= aldeano.coste:
        aldeano_nombre_text = get_font(20).render(f'{trad.t("villager")} {contarMejoras.contarAldeanos(partida)}', True, (255, 255, 0))
        aldeano_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(aldeano.coste)} {trad.t("of_gold")}',True,(255,255,0))
        aldeano_surface = pygame.image.load('graphics/icons/aldeano.png')
        aldeano.locked = False
  
    elif partida.oro < aldeano.coste and aldeano.locked == False:
        aldeano_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(aldeano.coste)} {trad.t("of_gold")}',True,( 101, 101, 101 )) 
        aldeano_nombre_text = get_font(20).render(f'{trad.t("villager")} {contarMejoras.contarAldeanos(partida)}', True, (101,101,101))
        aldeano_surface = pygame.image.load('graphics/icons/aldeano_baw.png')
  
    elif aldeano.locked == True:
        aldeano_coste_text = get_font(15).render(f'{trad.t("cost")} ?? {trad.t("of_gold")}',True,( 101, 101, 101 )) 
        aldeano_nombre_text = get_font(20).render(f'????????', True, (101,101,101))

    
    if partida.oro >= lenyador.coste:
        lenyador_nombre_text = get_font(20).render(f'{trad.t("woodcutter")} {contarMejoras.contarLenyadores(partida)}', True, (255, 255, 0))
        lenyador_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(lenyador.coste)} {trad.t("of_gold")}',True,(255,255,0))
        lenyador_surface = pygame.image.load('graphics/icons/lenyador.png')
        lenyador.locked = False

    elif partida.oro <= lenyador.coste and lenyador.locked == False:
        lenyador_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(lenyador.coste)} {trad.t("of_gold")}',True,( 101, 101, 101 )) 
        lenyador_nombre_text = get_font(20).render(f'{trad.t("woodcutter")} {contarMejoras.contarLenyadores(partida)}', True, (101,101,101))
        lenyador_surface = pygame.image.load('graphics/icons/lenyador_baw.png')
    
    elif lenyador.locked == True:
        lenyador_coste_text = get_font(15).render(f'{trad.t("cost")} ??? {trad.t("of_gold")}',True,( 101, 101, 101 )) 
        lenyador_nombre_text = get_font(20).render(f'????????', True, (101,101,101))



    if partida.oro >= arquero.coste and partida.madera >= arquero.coste:
        arquero_nombre_text = get_font(20).render(f'{trad.t("archer")} {contarMejoras.contarArqueros(partida)}', True, (255, 255, 0))
        arquero_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(arquero.coste)} {trad.t("of_wood")} {trad.t("and")} \n {trad.t("gold")}',True,(255,255,0))
        arquero_surface = pygame.image.load('graphics/icons/arquero.png')
        arquero.locked = False

    elif (partida.oro < arquero.coste or partida.madera < arquero.coste) and arquero.locked == False: 
        arquero_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(arquero.coste)} {trad.t("of_wood")} {trad.t("and")} \n {trad.t("gold")}',True,(101,101,101))
        arquero_nombre_text = get_font(20).render(f'{trad.t("archer")} {contarMejoras.contarArqueros(partida)}', True, (101,101,101))
        arquero_surface = pygame.image.load('graphics/icons/arquero_baw.png')

    elif arquero.locked == True:
        arquero_coste_text = get_font(15).render(f'{trad.t("cost")}??? {trad.t("of_wood")} {trad.t("and")} \n {trad.t("gold")}',True,( 101, 101, 101 )) 
        arquero_nombre_text = get_font(20).render(f'????????', True, (101,101,101))



    if partida.oro >= picaro.coste:
        picaro_nombre_text = get_font(20).render(f'{trad.t("rogue")} {contarMejoras.contarPicaros(partida)}', True, (255, 255, 0))
        picaro_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(picaro.coste)} {trad.t("of_gold")}',True,(255,255,0))
        picaro_surface = pygame.image.load('graphics/icons/picaro.png')
        picaro.locked = False

    elif partida.oro < picaro.coste and picaro.locked == False: 
        picaro_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(picaro.coste)} {trad.t("of_gold")}',True,(101,101,101))
        picaro_nombre_text = get_font(20).render(f'{trad.t("rogue")} {contarMejoras.contarPicaros(partida)}', True, (101,101,101))
        picaro_surface = pygame.image.load('graphics/icons/picaro_baw.png')

    elif picaro.locked == True: 
        picaro_coste_text = get_font(15).render(f'{trad.t("cost")} ???? {trad.t("of_gold")}',True,(101,101,101))
        picaro_nombre_text = get_font(20).render(f'???????: ', True, (101,101,101))


    if partida.oro >= mago.coste:
        mago_nombre_text = get_font(20).render(f'{trad.t("wizard")} {contarMejoras.contarMagos(partida)}', True, (255, 255, 0))
        mago_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(mago.coste)} {trad.t("of_gold")}',True,(255,255,0))
        mago_surface = pygame.image.load('graphics/icons/mago.png')
        mago.locked = False

    elif partida.oro < mago.coste and mago.locked == False: 
        mago_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(mago.coste)} {trad.t("of_gold")}',True,(101,101,101))
        mago_nombre_text = get_font(20).render(f'{trad.t("wizard")} {contarMejoras.contarMagos(partida)}', True, (101,101,101))
        mago_surface = pygame.image.load('graphics/icons/mago_baw.png')

    elif mago.locked == True:
        mago_coste_text = get_font(15).render(f'{trad.t("cost")} ???? {trad.t("of_gold")}',True,(101,101,101))
        mago_nombre_text = get_font(20).render(f'?????', True, (101,101,101))


    if partida.oro >= bardo.coste and partida.magia >= bardo.coste:
        bardo_nombre_text = get_font(20).render(f'{trad.t("bard")} {contarMejoras.contarBardos(partida)}', True, (255, 255, 0))
        bardo_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(bardo.coste)} {trad.t("of_gold")} {trad.t("and")} \n {trad.t("magic")}',True,(255,255,0))
        bardo_surface = pygame.image.load('graphics/icons/bardo.png')
        bardo.locked = False

    elif (partida.oro < bardo.coste or partida.magia < bardo.coste) and bardo.locked == False:
        bardo_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(bardo.coste)} {trad.t("of_gold")} {trad.t("and")} \n {trad.t("magic")}',True,(101,101,101))
        bardo_nombre_text = get_font(20).render(f'{trad.t("bard")} {contarMejoras.contarBardos(partida)}', True, (101,101,101))
        bardo_surface = pygame.image.load('graphics/icons/bardo_baw.png')

    elif bardo.locked == True:
        bardo_coste_text = get_font(15).render(f'{trad.t("cost")} ??? {trad.t("of_gold")} {trad.t("and")} \n {trad.t("magic")}',True,(101,101,101))
        bardo_nombre_text = get_font(20).render(f'???????', True, (101,101,101))


    if partida.oro >= soldado.coste:
        soldado_nombre_text = get_font(20).render(f'{trad.t("soldier")} {contarMejoras.contarSoldados(partida)}', True, (255, 255, 0))
        soldado_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(soldado.coste)} {trad.t("of_gold")}',True,(255,255,0))
        soldado_surface = pygame.image.load('graphics/icons/soldado.png')
        soldado.locked = False

    elif partida.oro < soldado.coste and soldado.locked == False: 
        soldado_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(soldado.coste)} {trad.t("of_gold")}',True,(101,101,101))
        soldado_nombre_text = get_font(20).render(f'{trad.t("soldier")} {contarMejoras.contarSoldados(partida)}', True, (101,101,101))
        soldado_surface = pygame.image.load('graphics/icons/soldado_baw.png')

    elif soldado.locked == True: 
        soldado_coste_text = get_font(15).render(f'{trad.t("cost")} ???? {trad.t("of_gold")}',True,(101,101,101))
        soldado_nombre_text = get_font(20).render(f'????????', True, (101,101,101))


    if partida.magia >= clerigo.coste:
        clerigo_nombre_text = get_font(20).render(f'{trad.t("cleric")} {contarMejoras.contarClerigos(partida)}', True, (255, 255, 0))
        clerigo_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(clerigo.coste)} {trad.t("of_magic")}',True,(255,255,0))
        clerigo_surface = pygame.image.load('graphics/icons/clerigo.png')
        clerigo.locked = False

    elif partida.magia < clerigo.coste and clerigo.locked == False: 
        clerigo_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(clerigo.coste)} {trad.t("of_magic")}',True,(101,101,101))
        clerigo_nombre_text = get_font(20).render(f'{trad.t("cleric")}{contarMejoras.contarClerigos(partida)}', True, (101,101,101))
        clerigo_surface = pygame.image.load('graphics/icons/clerigo_baw.png')

    elif clerigo.locked == True:
        clerigo_coste_text = get_font(15).render(f'{trad.t("cost")} ???? {trad.t("of_magic")}',True,(101,101,101))
        clerigo_nombre_text = get_font(20).render(f'????????', True, (101,101,101))


    if partida.magia >= druida.coste and partida.madera >= druida.coste:
        druida_nombre_text = get_font(20).render(f'{trad.t("druid")} {contarMejoras.contarDruidas(partida)}', True, (255, 255, 0))
        druida_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(druida.coste)} {trad.t("of_wood")} \n{trad.t("and")}  {trad.t("magic")}',True,(255,255,0))
        druida_surface = pygame.image.load('graphics/icons/druida.png')
        druida.locked = False

    elif (partida.magia < druida.coste or partida.madera < druida.coste) and druida.locked == False: 
        druida_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(druida.coste)} {trad.t("of_wood")} \n{trad.t("and")}  {trad.t("magic")}',True,(101,101,101))
        druida_nombre_text = get_font(20).render(f'{trad.t("druid")} {contarMejoras.contarDruidas(partida)}', True, (101,101,101))
        druida_surface = pygame.image.load('graphics/icons/druida_baw.png')

    elif druida.locked == True: 
        druida_coste_text = get_font(15).render(f'{trad.t("cost")} ???? {trad.t("of_wood")} \n{trad.t("and")}  {trad.t("magic")}',True,(101,101,101))
        druida_nombre_text = get_font(20).render(f'???????', True, (101,101,101))


    if partida.magia >= bruja.coste:
        bruja_nombre_text = get_font(20).render(f'{trad.t("witch")} {contarMejoras.contarBrujas(partida)}', True, (255, 255, 0))
        bruja_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(bruja.coste)} {trad.t("of_magic")}',True,(255,255,0))
        bruja_surface = pygame.image.load('graphics/icons/bruja.png')
        bruja.locked = False

    elif partida.magia < bruja.coste and bruja.locked == False: 
        bruja_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(bruja.coste)} {trad.t("of_magic")}',True,(101,101,101))
        bruja_nombre_text = get_font(20).render(f'{trad.t("witch")} {contarMejoras.contarBrujas(partida)}', True, (101,101,101))
        bruja_surface = pygame.image.load('graphics/icons/bruja_baw.png')

    elif bruja.locked == True:
        bruja_coste_text = get_font(15).render(f'{trad.t("cost")} ???? {trad.t("of_magic")}',True,(101,101,101))
        bruja_nombre_text = get_font(20).render(f'??????', True, (101,101,101))


    if partida.oro >= noble.coste:
        noble_nombre_text = get_font(20).render(f'{trad.t("noble")} {contarMejoras.contarNobles(partida)}', True, (255, 255, 0))
        noble_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(noble.coste)} {trad.t("of_gold")}',True,(255,255,0))
        noble_surface =pygame.image.load('graphics/icons/noble.png')
        noble.locked = False

    elif partida.oro < noble.coste and noble.locked == False: 
        noble_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(noble.coste)} {trad.t("of_gold")}',True,(101,101,101))
        noble_nombre_text = get_font(20).render(f'{trad.t("noble")} {contarMejoras.contarNobles(partida)}', True, (101,101,101))
        noble_surface =pygame.image.load('graphics/icons/noble_baw.png')

    elif noble.locked == True:
        noble_coste_text = get_font(15).render(f'{trad.t("cost")} ????? {trad.t("of_gold")}',True,(101,101,101))
        noble_nombre_text = get_font(20).render(f'??????', True, (101,101,101))


    if partida.oro >= princesa.coste:
        princesa_nombre_text = get_font(20).render(f'{trad.t("princess")} {contarMejoras.contarPrincesas(partida)}', True, (255, 255, 0))
        princesa_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(princesa.coste)} {trad.t("of_gold")}',True,(255,255,0))
        princesa_surface =pygame.image.load('graphics/icons/princesa.png')
        princesa.locked = False

    elif partida.oro < princesa.coste and princesa.locked == False: 
        princesa_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(princesa.coste)} {trad.t("of_gold")}',True,(101,101,101))
        princesa_nombre_text = get_font(20).render(f'{trad.t("princess")} {contarMejoras.contarPrincesas(partida)}', True, (101,101,101))
        princesa_surface =pygame.image.load('graphics/icons/princesa_baw.png')

    elif princesa.locked == True:
        princesa_coste_text = get_font(15).render(f'{trad.t("cost")} ?????? {trad.t("of_gold")}',True,(101,101,101))
        princesa_nombre_text = get_font(20).render(f'??????', True, (101,101,101))


    if partida.oro >= reina.coste:
        reina_nombre_text = get_font(20).render(f'{trad.t("queen")} {contarMejoras.contarReinas(partida)}', True, (255, 255, 0))
        reina_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(reina.coste)} {trad.t("of_gold")}',True,(255,255,0))
        reina_surface =pygame.image.load('graphics/icons/reina.png')
        reina.locked = False

    elif partida.oro < reina.coste and reina.locked == False: 
        reina_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(reina.coste)} {trad.t("of_gold")}',True,(101,101,101))
        reina_nombre_text = get_font(20).render(f'{trad.t("queen")} {contarMejoras.contarReinas(partida)}', True, (101,101,101))
        reina_surface =pygame.image.load('graphics/icons/reina_baw.png')

    elif reina.locked == True:
        reina_coste_text = get_font(15).render(f'{trad.t("cost")} ?????? {trad.t("of_gold")}',True,(101,101,101))
        reina_nombre_text = get_font(20).render(f'??????', True, (101,101,101))
        reina.locked = True


    if partida.oro >= rey.coste:
        rey_nombre_text = get_font(20).render(f'{trad.t("king")} {contarMejoras.contarReyes(partida)}', True, (255, 255, 0))
        rey_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(rey.coste)} {trad.t("of_gold")}',True,(255,255,0))
        rey_surface =pygame.image.load('graphics/icons/rey.png')
        rey.locked = False

    elif partida.oro < rey.coste and rey.locked == False: 
        rey_coste_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(rey.coste)} {trad.t("of_gold")}',True,(101,101,101))
        rey_nombre_text = get_font(20).render(f'{trad.t("king")} {contarMejoras.contarReyes(partida)}', True, (101,101,101))
        rey_surface =pygame.image.load('graphics/icons/rey_baw.png')

    elif rey.locked == True:
        rey_coste_text = get_font(15).render(f'{trad.t("cost")} ?????? {trad.t("of_gold")}',True,(101,101,101))
        rey_nombre_text = get_font(20).render(f'??????', True, (101,101,101))


    # Dibujar cada mejora con datos actualizados
    datos_mejoras = [
        (tarjetasMejora[0],contarMejoras.contarAldeanos(partida),aldeano_surface,aldeano_nombre_text,aldeano_coste_text),
        (tarjetasMejora[1],contarMejoras.contarLenyadores(partida),lenyador_surface,lenyador_nombre_text,lenyador_coste_text),
        (tarjetasMejora[2],contarMejoras.contarArqueros(partida),arquero_surface,arquero_nombre_text,arquero_coste_text),
        (tarjetasMejora[3],contarMejoras.contarPicaros(partida),picaro_surface,picaro_nombre_text,picaro_coste_text),
        (tarjetasMejora[4],contarMejoras.contarMagos(partida),mago_surface,mago_nombre_text,mago_coste_text),
        (tarjetasMejora[5],contarMejoras.contarBardos(partida),bardo_surface,bardo_nombre_text,bardo_coste_text),
        (tarjetasMejora[6],contarMejoras.contarSoldados(partida),soldado_surface,soldado_nombre_text,soldado_coste_text),
        (tarjetasMejora[7],contarMejoras.contarClerigos(partida),clerigo_surface,clerigo_nombre_text,clerigo_coste_text),
        (tarjetasMejora[8],contarMejoras.contarDruidas(partida),druida_surface,druida_nombre_text,druida_coste_text),
        (tarjetasMejora[9],contarMejoras.contarBrujas(partida),bruja_surface,bruja_nombre_text,bruja_coste_text),
        (tarjetasMejora[10],contarMejoras.contarNobles(partida),noble_surface,noble_nombre_text,noble_coste_text),
        (tarjetasMejora[11],contarMejoras.contarPrincesas(partida),princesa_surface,princesa_nombre_text,princesa_coste_text),
        (tarjetasMejora[12],contarMejoras.contarReinas(partida),reina_surface,reina_nombre_text,reina_coste_text),
        (tarjetasMejora[13],contarMejoras.contarReyes(partida),rey_surface,rey_nombre_text,rey_coste_text)
    ]
    
    mouse_pos = pygame.mouse.get_pos()
        
    # Convertir las coordenadas del mouse a coordenadas relativas a upgrade_list_surface
    # Tomamos en cuenta la posición de upgrade_list_rect en la pantalla
    mouse_rel_x = mouse_pos[0] - upgrade_list_rect.x
    mouse_rel_y = mouse_pos[1] - upgrade_list_rect.y + scroll_y
    
    # Verificar si el mouse está dentro de upgrade_list_rect antes de procesar hover
    if upgrade_list_rect.collidepoint(mouse_pos):
        rel_mouse_pos = (mouse_rel_x, mouse_rel_y)
    else:
        # Si el mouse está fuera, configuramos una posición que no activará ningún hover
        rel_mouse_pos = (-100, -100)

    for tarjeta, cantidad, imagen, texto_nombre, texto_coste in datos_mejoras:
        # Usar rel_mouse_pos en lugar de mouse_pos para el hover
        if tarjeta.collidepoint(rel_mouse_pos, scroll_y):  # Nota: ya ajustamos por scroll_y en rel_mouse_pos
            tarjeta.current_color = tarjeta.hover_color
        else:
            tarjeta.current_color = tarjeta.normal_color

        tarjeta.draw(upgrade_list_surface, cantidad, imagen, texto_nombre, texto_coste, scroll_y)


    #tooltip_mejoras(aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey)

    # ...etc