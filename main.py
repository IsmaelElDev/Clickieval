import pygame,random, traceback
from sys import exit
from servicios.database import create_tables
from entidades.partida import Partida
from entidades.aldeano import Aldeano
from entidades.leñador import Lenyador
from entidades.arquero import Arquero
from entidades.picaro import Picaro
from entidades.bardo import Bardo
from entidades.mago import Mago
from entidades.soldado import Soldado
from entidades.clerigo import Clerigo
from entidades.druida import Druida
from entidades.bruja import Bruja
from entidades.noble import Noble
from entidades.princesa import Princesa
from entidades.reina import Reina
from entidades.rey import Rey
from entidades.evento import Evento
from fx.particula import Particula
from ui.boton import Boton
from servicios.database_operations import guardar_partida,buscar_partidas,cargar_partida,conectar_db
from servicios.traductor import TranslationManager
from ui.mejoratarjeta import MejoraTarjeta
from ui.caja import Caja
from utils.contarMejoras import contarMejoras
from utils.recuperarCostes import recuperarCostes
from utils.resetearMejoras import resetear_mejoras
from utils.comprarMejoras import comprarMejoras
from utils.formatearNumero import formatear_numero
from utils.pintarMejoras import pintarMejoras
from utils.tooltip import tooltip_mejoras
from utils.obtenerFuente import get_font
from utils.contarEventos import contarEventos
from utils.activadorEvento import activador_evento
from utils.verificarDurEventos import verificarDurEventos



# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Configurar pantalla
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Clickieval')

# Icono del juego
icon_surface = pygame.image.load('graphics/icons/espada.png')
pygame.display.set_icon(icon_surface)

# Configurar reloj
fps = pygame.time.Clock()

# Crear imagen del cofre

recurso_surface = pygame.Surface((240, 250),pygame.SRCALPHA)
recurso_rect = recurso_surface.get_rect(topleft=(380,275))
recurso_surface.fill((0,0,0,0))

# Crear fondo
mazmorra_surface = pygame.image.load('graphics/background/mazmorra.png')

# Crear variable que manejara los fondos
fondo_actual = mazmorra_surface

# Crear arbol
arbol_surface = pygame.image.load('graphics/background/bosque.png')
arbol_rect = arbol_surface.get_rect(topleft=(400,200))

# Crear icono refrescar 
refrescar_surface = pygame.image.load('graphics/icons/refresh-icon.png')
refrescar_rect = refrescar_surface.get_rect(topleft=(80,625))

# Crear icono de tienda
tienda_surface = pygame.image.load('graphics/icons/tienda.png')
tienda_rect = tienda_surface.get_rect(topleft=(40,625))

# Crear icono de estadisticas
stats_surface = pygame.image.load('graphics/icons/stats.png')
stats_rect = stats_surface.get_rect(topleft=(120,625))

# Fuente para mostrar el oro
font = get_font(26)

# Objeto partida que contiene las variables del juego
partida = Partida()

# Sonido de monedas
gold_sound = pygame.mixer.Sound('fx/monedas.mp3')
sound_delay = 900  # 900 milisegundos de espera
last_sound_time = -sound_delay  # Última vez que se reprodujo el sonido

# Creacion eventos

evento_guerra = Evento(1,0.40,1,60000)
evento_despertar_ruinas = Evento(2,0.20,20,80000)

# Definir upgrades
aldeano = Aldeano('Aldeano', 50, 1,1, 1.24)
lenyador = Lenyador('Lenyador',150,5,5,1.32)
arquero = Arquero('Arquero',100,5,5,1.30)
picaro = Picaro('Picaro',3000,3000,35000,0,0,1.40)
mago = Mago('Mago',2000,100,100,1.25)
bardo = Bardo('Bardo',500,2,2,1.60)
soldado = Soldado('Soldado',5000,100,100,1.26)
clerigo = Clerigo('Clerigo',2000,250,250,1.29)
druida = Druida('Druida',5000,1.3,1.3,1.58)
bruja = Bruja('Bruja',10000,800,800,1.16)
noble = Noble('Noble',50000,6000,6000,1.35)
princesa = Princesa('Princesa',160000,9300,9300,1.45)
reina = Reina('Princesa',520000,11000,11000,1.57)
rey = Rey('Rey',1500000,1.1,1.1,1.80)

scroll_y = 0
scroll_speed = 20
surface_height = 810  # Altura total del contenido 
upgrade_list_surface = pygame.Surface((300, surface_height))
upgrade_list_rect = pygame.Rect(720, 50, 300, 500)  # Área visible

aldeano_surface = pygame.image.load('graphics/icons/aldeano_locked.png')
aldeano_rect = pygame.Rect(0, 0, 81, 95)

lenyador_surface = pygame.image.load('graphics/icons/lenyador_locked.png')
lenyador_rect = pygame.Rect(0, 80, 81, 95)

arquero_surface = pygame.image.load('graphics/icons/arquero_locked.png')
arquero_rect = pygame.Rect(0, 160, 81, 95)

picaro_surface = pygame.image.load('graphics/icons/picaro_locked.png')
picaro_rect = pygame.Rect(0, 240, 81, 95)

mago_surface = pygame.image.load('graphics/icons/mago_locked.png')
mago_rect = pygame.Rect(0, 320, 81, 95)

bardo_surface = pygame.image.load('graphics/icons/bardo_locked.png')
bardo_rect = pygame.Rect(0, 400, 81, 95)

soldado_surface = pygame.image.load('graphics/icons/soldado_locked.png')
soldado_rect = pygame.Rect(0, 480, 81, 95)

clerigo_surface = pygame.image.load('graphics/icons/clerigo_locked.png')
clerigo_rect = pygame.Rect(0, 560, 81, 95)

druida_surface = pygame.image.load('graphics/icons/druida_locked.png')
druida_rect = pygame.Rect(0, 640, 81, 95)

bruja_surface = pygame.image.load('graphics/icons/bruja_locked.png')
bruja_rect = pygame.Rect(0, 720, 81, 95)

noble_surface =pygame.image.load('graphics/icons/noble_locked.png')
noble_rect = pygame.Rect(0, 800, 81, 95)

princesa_surface =pygame.image.load('graphics/icons/princesa_locked.png')
princesa_rect = pygame.Rect(0, 880, 81, 95)

reina_surface =pygame.image.load('graphics/icons/reina_locked.png')
reina_rect = pygame.Rect(0, 960, 81, 95)

rey_surface =pygame.image.load('graphics/icons/rey_locked.png')
rey_rect = pygame.Rect(0, 1040, 81, 95)

# Evento para sumar oro automáticamente cada segundo
RECURSOS_TICK = pygame.USEREVENT + 1
PICARO_TICK = pygame.USEREVENT + 2
GUERRA_TICK = pygame.USEREVENT + 3
DESPERTAR_TICK = pygame.USEREVENT + 4  
pygame.time.set_timer(RECURSOS_TICK, 1000)
pygame.time.set_timer(PICARO_TICK, 60000)
pygame.time.set_timer(GUERRA_TICK, evento_guerra.enfriamiento)
pygame.time.set_timer(DESPERTAR_TICK, evento_despertar_ruinas.enfriamiento)
# Crear tarjetas 
tarjetasMejoras = [
    MejoraTarjeta("Aldeanos", (0, 0), get_font(20), get_font(15)),
    MejoraTarjeta("Leñadores", (0, 80), get_font(20), get_font(15)),
    MejoraTarjeta("Arqueros", (0, 160), get_font(20), get_font(15)),
    MejoraTarjeta("Pícaros", (0, 240), get_font(20), get_font(15)),
    MejoraTarjeta("Magos", (0, 320), get_font(20), get_font(15)),
    MejoraTarjeta("Bardos", (0, 400), get_font(20), get_font(15)),    
    MejoraTarjeta("Soldados", (0, 480), get_font(20), get_font(15)),
    MejoraTarjeta("Clerigos", (0, 560), get_font(20), get_font(15)),
    MejoraTarjeta("Druidas", (0, 640), get_font(20), get_font(15)),
    MejoraTarjeta("Brujas", (0, 720), get_font(20), get_font(15)),
    MejoraTarjeta("Nobles", (0, 800), get_font(20), get_font(15)),
    MejoraTarjeta("Princesas", (0, 880), get_font(20), get_font(15)),
    MejoraTarjeta("Reinas", (0, 960), get_font(20), get_font(15)),
    MejoraTarjeta("Reyes", (0, 1040), get_font(20), get_font(15))
]

moneda_img = pygame.image.load('fx/moneda.png').convert_alpha()
moneda_img = pygame.transform.scale(moneda_img, (16, 16))  

particulas = []  # Lista para almacenar partículas activas


def recuperar_costes_mejoras(partida):
    global aldeano
    global lenyador
    global arquero
    global picaro
    global mago
    global bardo
    global soldado
    global clerigo
    global druida
    global bruja
    global noble
    global princesa
    global reina
    global rey

    recuperarCostes.recuperar_multiplicadores_bardos(aldeano,lenyador,bardo,partida)
    recuperarCostes.recuperar_multiplicadores_reyes(aldeano,lenyador,arquero,picaro,bardo,mago,soldado,clerigo,druida,bruja,noble,princesa,reina,rey,partida)
    recuperarCostes.recuperar_costes_aldeanos(aldeano,partida)
    recuperarCostes.recuperar_costes_lenyadores(lenyador,partida)
    recuperarCostes.recuperar_costes_arqueros(arquero,partida)
    recuperarCostes.recuperar_costes_picaros(picaro,partida)
    recuperarCostes.recuperar_costes_magos(mago,partida)
    recuperarCostes.recuperar_costes_soldados(soldado,partida)
    recuperarCostes.recuperar_costes_clerigos(clerigo,partida)
    recuperarCostes.recuperar_costes_druidas(druida,partida)
    recuperarCostes.recuperar_costes_brujas(bruja,partida)
    recuperarCostes.recuperar_costes_nobles(noble,partida)
    recuperarCostes.recuperar_costes_princesas(princesa,partida)
    recuperarCostes.recuperar_costes_reinas(reina,partida)
    recuperarCostes.recuperar_costes_reyes(rey,partida)
    recuperarCostes.recuperar_costes_bardos(bardo, partida)
    

def pantalla_cargar_partida(trad):
    """Muestra una pantalla para seleccionar partidas guardadas"""
    
    # Obtener todas las partidas guardadas
    partidas = buscar_partidas()
    
    # Si no hay partidas, mostrar mensaje
    if not partidas:
        return None
    
    # Variables para la pantalla
    seleccion = 0
    partidas_por_pagina = 5
    pagina_actual = 0
    total_paginas = (len(partidas) - 1) // partidas_por_pagina + 1
    
    while True:
        screen.fill((30, 30, 30))
        
        # Título
        titulo = get_font(50).render(trad.t("load_game"), True, "#ffffff")
        titulo_rect = titulo.get_rect(center=(500, 100))
        screen.blit(titulo, titulo_rect)
        
        # Mostrar partidas de la página actual
        inicio = pagina_actual * partidas_por_pagina
        fin = min(inicio + partidas_por_pagina, len(partidas))
        
        for i, partida in enumerate(partidas[inicio:fin]):
            y_pos = 200 + i * 60
            
            # Crear texto para cada partida
            texto = f'ID: {partida.id} - {trad.t("game_name")} {partida.nombre} - {trad.t("gold")} {formatear_numero(partida.oro)}'
            color = "#f0c67d" if i == seleccion else "#8f836e"
            
            partida_text = get_font(25).render(texto, True, color)
            partida_rect = partida_text.get_rect(center=(500, y_pos))
            screen.blit(partida_text, partida_rect)
        
        # Botones de navegación y selección
        volver = Boton(None, (250, 600), trad.t("return"), get_font(30), "#8f836e", "#f0c67d")
        siguiente = Boton(None, (750, 600), trad.t("next"), get_font(30), "#8f836e", "#f0c67d")
        anterior = Boton(None, (500, 600), trad.t("back"), get_font(30), "#8f836e", "#f0c67d")
        cargar = Boton(None, (500, 500), trad.t("load_selected"), get_font(30), "#8f836e", "#f0c67d")
        
        mouse_pos = pygame.mouse.get_pos()
        
        for boton in [volver, siguiente, anterior, cargar]:
            boton.changeColor(mouse_pos)
            boton.update(screen)
        
        # Indicador de página
        pagina_text = get_font(20).render(f'{trad.t("page")} {pagina_actual + 1}/{total_paginas}', True, "#ffffff")
        pagina_rect = pagina_text.get_rect(center=(500, 650))
        screen.blit(pagina_text, pagina_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and seleccion > 0:
                    seleccion -= 1
                elif event.key == pygame.K_DOWN and seleccion < min(partidas_por_pagina - 1, fin - inicio - 1):
                    seleccion += 1
                elif event.key == pygame.K_RETURN:
                    # Cargar la partida seleccionada
                    partida_id = partidas[inicio + seleccion].id
                    return cargar_partida(partida_id)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if volver.checkForInput(mouse_pos):
                    return None
                elif siguiente.checkForInput(mouse_pos) and pagina_actual < total_paginas - 1:
                    pagina_actual += 1
                    seleccion = 0
                elif anterior.checkForInput(mouse_pos) and pagina_actual > 0:
                    pagina_actual -= 1
                    seleccion = 0
                elif cargar.checkForInput(mouse_pos):
                    partida_id = partidas[inicio + seleccion].id
                    partidacargada = cargar_partida(partida_id)
                    recuperar_costes_mejoras(partidacargada)
                    jugar_partida(partidacargada,trad)

        pygame.display.update()
        fps.tick(60)


def menu_principal():
    create_tables()
    bandera_es = pygame.image.load('graphics/icons/bandera_es.png')
    bandera_en = pygame.image.load('graphics/icons/bandera_en.png')
    bandera_es = pygame.transform.scale(bandera_es, (180, 100))
    bandera_en = pygame.transform.scale(bandera_en, (180, 100))
    idioma_surface = bandera_es  # estado inicial de la bandera
    idioma_rect = pygame.Rect(820, 510, 81, 95)
    idioma = 'es'
    
    while True:
        fondo = pygame.image.load('graphics/background/pantalla_principal.png')
        fondo = pygame.transform.scale(fondo, (1000, 700))
        screen.blit(fondo,(0,0))
        mouse_pos = pygame.mouse.get_pos()
        
        trad = TranslationManager(idioma)


        nueva_partida = Boton(None,(500,510),trad.t("new_game"),get_font(30),"#8f836e","#f0c67d")
        cargar_partida = Boton(None,(500,560),trad.t("load_game"),get_font(30),"#8f836e","#f0c67d")
        cambiar_idioma = pygame.image.load('graphics/icons/flecha.png')
        cambiar_idioma_rect = cambiar_idioma.get_rect(topleft=(895,610))


        for button in [nueva_partida,cargar_partida]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nueva_partida.checkForInput(mouse_pos):
                    partidaNueva = Partida()
                    jugar_partida(partidaNueva,trad)
                elif cambiar_idioma_rect.collidepoint(mouse_pos):
                    if idioma_surface == bandera_es:
                        idioma_surface = bandera_en
                        idioma = 'en'
                    else: 
                        idioma_surface = bandera_es
                        idioma = 'es'
                elif cargar_partida.checkForInput(mouse_pos):
                    pantalla_cargar_partida(trad)

        
        screen.blit(idioma_surface,idioma_rect)
        screen.blit(cambiar_idioma,cambiar_idioma_rect)
        pygame.display.update()
        fps.tick(60)


def jugar_partida(partida,trad):
    while True:
        screen.blit(fondo_actual,(0,0))

        # Obtener tiempo actual
        current_time = pygame.time.get_ticks()

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                

            gestion_eventos(event,partida,trad,current_time,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble)
            activador_evento(evento_guerra,evento_despertar_ruinas,partida,trad,GUERRA_TICK,DESPERTAR_TICK,screen,fondo_actual,aldeano,lenyador,bardo,mago,clerigo,druida,event)
            verificarDurEventos(screen,evento_despertar_ruinas,evento_guerra,partida,trad,current_time)
        # Dibujar elementos en pantalla
        visible_area = pygame.Rect(0, scroll_y, upgrade_list_rect.width, upgrade_list_rect.height)
        screen.blit(upgrade_list_surface.subsurface(visible_area), upgrade_list_rect.topleft)
        
        # Dibuja los elementos en upgrade_list_surface (ajustando sus posiciones Y con scroll_y)
        
        aldeano_rect.y = 0 - scroll_y  # Posición relativa al scroll
        lenyador_rect.y = 80 - scroll_y
        arquero_rect.y = 160 - scroll_y
        picaro_rect.y = 240 - scroll_y
        mago_rect.y = 320 - scroll_y
        bardo_rect.y = 400 - scroll_y
        soldado_rect.y = 480 - scroll_y
        clerigo_rect.y = 560 -scroll_y
        druida_rect.y = 640 - scroll_y
        bruja_rect.y = 720 - scroll_y
        noble_rect.y = 800 - scroll_y
        princesa_rect.y = 880 - scroll_y
        reina_rect.y = 960 - scroll_y
        rey_rect.y = 1040 - scroll_y
    
        pintarMejoras(partida,trad,tarjetasMejoras,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey,aldeano_surface,lenyador_surface,arquero_surface,picaro_surface,mago_surface,bardo_surface,soldado_surface,clerigo_surface,druida_surface,bruja_surface,noble_surface,princesa_surface,reina_surface,rey_surface,upgrade_list_surface,upgrade_list_rect,scroll_y)
        tooltip_mejoras(trad,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey,aldeano_rect,lenyador_rect,arquero_rect,picaro_rect,mago_rect,bardo_rect,soldado_rect,clerigo_rect,druida_rect,bruja_rect,noble_rect,princesa_rect,reina_rect,rey_rect,upgrade_list_rect,screen,scroll_y)


        screen.blit(recurso_surface, recurso_rect.topleft)
        screen.blit(tienda_surface,tienda_rect.topleft)
        if(partida.pantalla_estadisticas == True):
            screen.blit(stats_surface,stats_rect)
        if(partida.pantalla_refrescar == True):
            screen.blit(refrescar_surface,refrescar_rect)


        # Mostrar estadisticas en pantalla
        gold_text = font.render(f'{trad.t("gold")} {formatear_numero(partida.oro)}', True, (255, 255, 0))
        madera_text = font.render(f'{trad.t("wood")} {formatear_numero(partida.madera)} ',True, (28,105,21))
        magia_text = font.render(f'{trad.t("magic")} {formatear_numero(partida.magia)} ',True, (223, 186, 245))


        screen.blit(gold_text, (30, 20))
        screen.blit(madera_text,(30,70))
        screen.blit(magia_text,(30,120))

        for p in particulas[:]:
            p.actualizar()
            p.dibujar(screen)
            if p.ha_muerto():
                particulas.remove(p)

        contarEventos(partida)
        # Actualizar pantalla
        pygame.display.update()
        fps.tick(60)

def gestion_eventos(event,partida,trad,current_time,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble):
    global last_sound_time  # Permite modificar la variable global
    global scroll_speed
    global scroll_y
    global fondo_actual

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
        if recurso_rect.collidepoint(event.pos) and fondo_actual == mazmorra_surface:  # Si clic en el cofre
            partida.oro += partida.oro_por_click
            partida.oro_total += partida.oro_por_click
            # Esto crea varias partículas (por ejemplo 10)
            for _ in range(10):
                pos = [event.pos[0], event.pos[1]]
                vel = [random.uniform(-2.4, 1.4), random.uniform(-2.5, -1)]
                particulas.append(Particula(pos, vel,pygame.image.load("fx/moneda.png").convert_alpha()))



            #  Reproducir sonido SOLO si han pasado 900 milisegundos desde el último
            if current_time - last_sound_time >= sound_delay:
                gold_sound.play()
                last_sound_time = current_time  # Actualizar tiempo del último sonido

        elif recurso_rect.collidepoint(event.pos) and fondo_actual == arbol_surface:
            partida.madera += partida.madera_por_click
            partida.madera_total += partida.madera_por_click
            for _ in range(10):
                pos = [event.pos[0], event.pos[1]]
                vel = [random.uniform(-2.4, 1.4), random.uniform(-2.5, -1)]
                particulas.append(Particula(pos, vel,pygame.image.load("fx/tronco.png").convert_alpha()))


        elif refrescar_rect.collidepoint(event.pos) and partida.pantalla_refrescar == True:
            if fondo_actual == mazmorra_surface:
                fondo_actual = arbol_surface
            else:
                fondo_actual = mazmorra_surface

        elif tienda_rect.collidepoint(event.pos):
            menu_tienda(partida,trad)

        elif stats_rect.collidepoint(event.pos) and partida.pantalla_estadisticas == True:
            menu_stats(partida,trad)

        comprar_mejora(partida,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey,event)

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            menu_escape(partida,trad)
    
    #Codigo que desplaza el scroll
    elif event.type == pygame.MOUSEWHEEL:
        if upgrade_list_rect.collidepoint(pygame.mouse.get_pos()):  
            scroll_y -= event.y * scroll_speed
            scroll_y = max(0, min(scroll_y, surface_height - upgrade_list_rect.height))

    
    elif event.type == RECURSOS_TICK:
        partida.oro += partida.oro_por_segundo  # Sumar oro automáticamente
        partida.oro_total += partida.oro_por_segundo
        partida.madera += partida.madera_por_segundo
        partida.madera_total += partida.madera_por_segundo
        partida.magia += partida.magia_por_segundo
        partida.magia_total += partida.magia_por_segundo

    elif event.type == PICARO_TICK:
        try:
            picaros = contarMejoras.contarPicaros(partida)
            if picaros > 0:
                for upgrade in partida.mejoras:
                    if isinstance(upgrade, Picaro):
                        produccion = upgrade.calculo_produccion()
                        print(produccion)
                        partida.oro += produccion
                        partida.oro_total += produccion
        except Exception as e:
            print(f"Error processing Picaro tick: {e}")



# Función comprar_mejora simplificada:
def comprar_mejora(partida, aldeano, lenyador, arquero, picaro, mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey,event):
    # Comprobar si el click está dentro del área de mejoras
    if not upgrade_list_rect.collidepoint(event.pos):
        return
        
    # Calcular posición relativa del mouse en el área desplazable
    rel_x = event.pos[0] - upgrade_list_rect.x
    rel_y = event.pos[1] - upgrade_list_rect.y + scroll_y
    
    # Comprobar colisión con cada botón de mejora, ajustado al scroll
    
    # Aldeano
    if tarjetasMejoras[0].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= aldeano.coste:
            comprarMejoras.comprar_aldeano(partida, aldeano)
            return
    
    # Leñador
    if tarjetasMejoras[1].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= lenyador.coste:
            comprarMejoras.comprar_lenyador(partida, lenyador)
            return
    
    # Arquero
    if tarjetasMejoras[2].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= arquero.coste and partida.madera >= arquero.coste:
            comprarMejoras.comprar_arquero(partida, arquero)
            return
    
    # Pícaro
    elif tarjetasMejoras[3].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= picaro.coste:
            comprarMejoras.comprar_picaro(partida, picaro)
            return
    
    # Mago
    if tarjetasMejoras[4].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= mago.coste:
            comprarMejoras.comprar_mago(partida, mago)
            return
        
    # Bardo
    if tarjetasMejoras[5].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= bardo.coste and partida.magia >= bardo.coste:
            comprarMejoras.comprar_bardo(partida, aldeano,lenyador,bardo)
            return
        
    # Soldado
    if tarjetasMejoras[6].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= soldado.coste:
            comprarMejoras.comprar_soldado(partida, soldado)
            return
        
    # Clerigo
    if tarjetasMejoras[7].collidepoint((rel_x, rel_y), scroll_y):
        if partida.magia >= clerigo.coste:
            comprarMejoras.comprar_clerigo(partida, clerigo)
            return
        
    # Druida
    if tarjetasMejoras[8].collidepoint((rel_x, rel_y), scroll_y):
        if partida.madera >= druida.coste and partida.magia >= druida.coste:
            comprarMejoras.comprar_druida(partida, mago,clerigo,druida)
            return
        
    # Bruja
    if tarjetasMejoras[9].collidepoint((rel_x, rel_y), scroll_y):
        if partida.magia >= bruja.coste:
            comprarMejoras.comprar_bruja(partida, bruja)
            return
        
    # Noble
    if tarjetasMejoras[10].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= noble.coste:
            comprarMejoras.comprar_noble(partida, noble)
            return
        
        # Princesa
    if tarjetasMejoras[11].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= princesa.coste:
            comprarMejoras.comprar_princesa(partida, princesa)
            return
        
        #Reina
    if tarjetasMejoras[12].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= reina.coste:
            comprarMejoras.comprar_reina(partida, reina)
            return
        
        #Rey
    if tarjetasMejoras[13].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= rey.coste:
            comprarMejoras.comprar_rey(partida, aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey)
            return


def menu_escape(partida,trad):
    while True:
        fondo = pygame.image.load('graphics/background/pantalla_pausa.png')
        fondo = pygame.transform.scale(fondo,(1000,1236))
        screen.blit(fondo,(0,-250))
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(55).render(trad.t("game_paused"),True,"#916429")
        menu_rect = menu_text.get_rect(center=(520,70))
        screen.blit(menu_text,menu_rect)

        bot_guardar_partida = Boton(None,(510,160),trad.t("save_game"),get_font(35),"#8f836e","#f0c67d")
        bot_cargar_partida = Boton(None,(500,270),trad.t("load_game"),get_font(35),"#8f836e","#f0c67d")
        bot_volver_juego = Boton(None,(500,390),trad.t("resume_game"),get_font(35),"#8f836e","#f0c67d")
        bot_salir_juego = Boton(None,(500,510),trad.t("exit_game"),get_font(35),"#8f836e","#f0c67d")

        for button in [bot_guardar_partida,bot_cargar_partida,bot_volver_juego,bot_salir_juego]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if bot_guardar_partida.checkForInput(mouse_pos):
                    nombre_guardado = ""
                    escribiendo = True

                    while escribiendo:
                        for event2 in pygame.event.get():
                            if event2.type == pygame.QUIT:
                                pygame.quit()
                                exit()

                            if event2.type == pygame.KEYDOWN:
                                if event2.key == pygame.K_RETURN:
                                    escribiendo = False
                                elif event2.key == pygame.K_BACKSPACE:
                                    nombre_guardado = nombre_guardado[:-1]
                                else:
                                    if len(nombre_guardado) < 15:
                                        nombre_guardado += event2.unicode

                        # Redibujar fondo
                        screen.blit(fondo, (0, -250))  # Mantener la misma posición
                        screen.blit(menu_text, menu_rect)

                        # Dibujar los botones de nuevo
                        for button in [bot_guardar_partida, bot_cargar_partida, bot_volver_juego, bot_salir_juego]:
                            button.changeColor(mouse_pos)
                            button.update(screen)

                        # Dibujar caja de entrada
                        texto_input = get_font(30).render(f'{trad.t("game_name")} {nombre_guardado}', True, "#ffffff")
                        pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(300, 600, 540, 40))  # fondo de input
                        screen.blit(texto_input, (310, 605))
                        
                        pygame.display.update()
                        fps.tick(60)

                    # Guardar con el nombre ingresado
                    if nombre_guardado != "":
                        partida.nombre = nombre_guardado
                        try:
                            fresh_partida = guardar_partida(partida)
                            if fresh_partida:
                                partida = fresh_partida
                                mensaje = get_font(20).render(trad.t("game_saved"), True, (0, 255, 0))
                            else:
                                raise ValueError("Guardar partida devolvió nulo o valor no válido.")
                        except Exception as e:
                            print(traceback.format_exc())
                            mensaje = get_font(20).render(trad.t("game_not_saved"), True, (255, 0, 0))

                        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 660))
                        pygame.display.update()
                        pygame.time.delay(1000)
                    else:
                        mensaje = get_font(20).render(trad.t("game_empty"), True, (255, 0, 0))
                        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 660))
                        pygame.display.update()
                        pygame.time.delay(1000)

                            
                elif bot_cargar_partida.checkForInput(mouse_pos):
                    partida_cargada = pantalla_cargar_partida(trad)
                    if partida_cargada:
                        return partida_cargada  
                
                elif bot_volver_juego.checkForInput(mouse_pos):
                    return partida  
                
                elif bot_salir_juego.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()
        fps.tick(60)

def menu_tienda(partida,trad):
    while True:
        fondo = pygame.image.load('graphics/background/Background.png')
        pantalla_principal_surface = pygame.image.load('graphics/icons/mazmorra.png')
        pantalla_principal_rect = pantalla_principal_surface.get_rect(topleft=(40,625))
        screen.blit(fondo,(0,0))
        screen.blit(pantalla_principal_surface,pantalla_principal_rect)
        mouse_pos = pygame.mouse.get_pos()
        

        caja1_s1= pygame.Surface((240,10))
        caja1_r1 = caja1_s1.get_rect(topleft=(30,40))
        caja1_s2= pygame.Surface((10,240))
        caja1_r2 = caja1_s2.get_rect(topleft=(30,40))
        caja1_s3= pygame.Surface((240,10))
        caja1_r3 = caja1_s3.get_rect(topleft=(30,280))
        caja1_s4= pygame.Surface((10,240))
        caja1_r4 = caja1_s4.get_rect(topleft=(260,40))

        caja2_s1= pygame.Surface((240,10))
        caja2_r1 = caja2_s1.get_rect(topleft=(360,40))
        caja2_s2= pygame.Surface((10,240))
        caja2_r2 = caja2_s2.get_rect(topleft=(360,40))
        caja2_s3= pygame.Surface((240,10))
        caja2_r3 = caja2_s3.get_rect(topleft=(360,280))
        caja2_s4= pygame.Surface((10,240))
        caja2_r4 = caja2_s4.get_rect(topleft=(590,40))  

        #caja3_s1= pygame.Surface((240,10))
        #caja3_r1 = caja3_s1.get_rect(topleft=(690,40))
        #caja3_s2= pygame.Surface((10,240))
        #caja3_r2 = caja3_s2.get_rect(topleft=(690,40))
        #caja3_s3= pygame.Surface((240,10))
        #caja3_r3 = caja3_s3.get_rect(topleft=(690,280))
        #caja3_s4= pygame.Surface((10,240))
        #caja3_r4 = caja3_s4.get_rect(topleft=(920,40))

        #caja4_s1= pygame.Surface((240,10))
        #caja4_r1 = caja4_s1.get_rect(topleft=(30,340))
        ##caja4_s2= pygame.Surface((10,240))
        #caja4_r2 = caja4_s2.get_rect(topleft=(30,340))
        #caja4_s3= pygame.Surface((240,10))
        #caja4_r3 = caja4_s3.get_rect(topleft=(30,580))
        #caja4_s4= pygame.Surface((10,240))
        #caja4_r4 = caja4_s4.get_rect(topleft=(260,340))

        #caja5_s1= pygame.Surface((240,10))
        #caja5_r1 = caja5_s1.get_rect(topleft=(360,340))
       # caja5_s2= pygame.Surface((10,240))
       # caja5_r2 = caja5_s2.get_rect(topleft=(360,340))
       # caja5_s3= pygame.Surface((240,10))
       # caja5_r3 = caja5_s3.get_rect(topleft=(360,580))
       # caja5_s4= pygame.Surface((10,240))
       # caja5_r4 = caja5_s4.get_rect(topleft=(590,340))

       # caja6_s1= pygame.Surface((240,10))
        #caja6_r1 = caja6_s1.get_rect(topleft=(690,340))
        #caja6_s2= pygame.Surface((10,240))
       # caja6_r2 = caja6_s2.get_rect(topleft=(690,340))
       # caja6_s3= pygame.Surface((240,10))
        #caja6_r3 = caja6_s3.get_rect(topleft=(690,580))
        #caja6_s4= pygame.Surface((10,240))
        #caja6_r4 = caja6_s4.get_rect(topleft=(920,340))

        caja1 = Caja(caja1_s1,caja1_r1,caja1_s2,caja1_r2,caja1_s3,caja1_r3,caja1_s4,caja1_r4)
        caja2 = Caja(caja2_s1,caja2_r1,caja2_s2,caja2_r2,caja2_s3,caja2_r3,caja2_s4,caja2_r4)
       # caja3 = Caja(caja3_s1,caja3_r1,caja3_s2,caja3_r2,caja3_s3,caja3_r3,caja3_s4,caja3_r4)
       # caja4 = Caja(caja4_s1,caja4_r1,caja4_s2,caja4_r2,caja4_s3,caja4_r3,caja4_s4,caja4_r4)
       # caja5 = Caja(caja5_s1,caja5_r1,caja5_s2,caja5_r2,caja5_s3,caja5_r3,caja5_s4,caja5_r4)
       # caja6 = Caja(caja6_s1,caja6_r1,caja6_s2,caja6_r2,caja6_s3,caja6_r3,caja6_s4,caja6_r4)

        caja1.draw(screen)
        caja2.draw(screen)
        #caja3.draw(screen)
       # caja4.draw(screen)
       # caja5.draw(screen)
       # caja6.draw(screen)

        estadisticas_surface = pygame.image.load('graphics/icons/stats.png')
        estadisticas_comprar_bot = Boton(None, (150, 240), trad.t("buy_stats_screen"), get_font(20), "#8f836e", "#f0c67d")
        estadisticas_cost_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(50000)} {trad.t("of_gold")}',True,(255,255,0))
        screen.blit(estadisticas_surface,(140,140))
        screen.blit(estadisticas_cost_text,(40,60))
        estadisticas_comprar_bot.changeColor(mouse_pos)
        estadisticas_comprar_bot.update(screen)

        refrescar_surface = pygame.image.load('graphics/icons/refresh-icon.png')
        refrescar_comprar_bot = Boton(None, (480, 240), trad.t("buy_refresh_screen"), get_font(20), "#8f836e", "#f0c67d")
        refrescar_cost_text = get_font(15).render(f'{trad.t("cost")} {formatear_numero(3000)} {trad.t("of_gold")}',True,(255,255,0))

        screen.blit(refrescar_surface,(470,140))
        screen.blit(refrescar_cost_text,(370,60))

        refrescar_comprar_bot.changeColor(mouse_pos)
        refrescar_comprar_bot.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if pantalla_principal_rect.collidepoint(mouse_pos):
                    jugar_partida(partida,trad)
                elif estadisticas_comprar_bot.checkForInput(mouse_pos) and (partida.oro >= 50000 and partida.pantalla_estadisticas == False):
                    partida.oro -= 50000
                    partida.pantalla_estadisticas = True
                    partida.oro_gastado += 50000
                elif refrescar_comprar_bot.checkForInput(mouse_pos) and (partida.oro >= 3000 and partida.pantalla_refrescar == False):
                    partida.oro -= 3000
                    partida.pantalla_refrescar = True
                    partida.oro_gastado += 3000
                    
        pygame.display.update()
        fps.tick(60)



def menu_stats(partida,trad):
    
    while True:
        fondo = pygame.image.load('graphics/background/Background.png')
        pantalla_principal_surface = pygame.image.load('graphics/icons/mazmorra.png')
        pantalla_principal_rect = pantalla_principal_surface.get_rect(topleft=(40,625))
        screen.blit(fondo,(0,0))
        screen.blit(pantalla_principal_surface,pantalla_principal_rect)
        mouse_pos = pygame.mouse.get_pos()

        total_oro_text = get_font(20).render(f'{trad.t("total_gold_earned")} {formatear_numero(partida.oro_total)}',True,(255,255,0))
        gastado_oro_text = get_font(20).render(f'{trad.t("total_gold_spent")} {formatear_numero(partida.oro_gastado)}',True,(255,255,0))
        oro_segundo_text = get_font(20).render(f'{trad.t("total_gold_second")} {formatear_numero(partida.oro_por_segundo)}',True,(255,255,0))
        oro_click_text = get_font(20).render(f'{trad.t("total_gold_click")} {formatear_numero(partida.oro_por_click)}',True,(255,255,0))

        total_madera_text = get_font(20).render(f'{trad.t("total_wood_earned")} {formatear_numero(partida.madera_total)}',True,(28,105,21))
        gastada_madera_text = get_font(20).render(f'{trad.t("total_wood_spent")} {formatear_numero(partida.madera_gastada)}',True,(28,105,21))
        madera_segundo_text = get_font(20).render(f'{trad.t("total_wood_second")} {formatear_numero(partida.madera_por_segundo)}',True,(28,105,21))
        madera_click_text = get_font(20).render(f'{trad.t("total_wood_click")} {formatear_numero(partida.madera_por_click)}',True,(28,105,21))

        total_magia_text = get_font(20).render(f'{trad.t("total_magic_earned")} {formatear_numero(partida.magia_total)}',True,(223, 186, 245))
        gastada_magia_text = get_font(20).render(f'{trad.t("total_magic_spent")} {formatear_numero(partida.magia_gastada)}',True,(223, 186, 245))
        magia_segundo_text = get_font(20).render(f'{trad.t("total_magic_second")} {formatear_numero(partida.magia_por_segundo)}',True,(223, 186, 245))

        total_mejoras_text = get_font(20).render(f'{trad.t("total_upgrades_bought")} {contarMejoras.contarMejoras(partida)}',True,(255,255,255))

        screen.blit(total_oro_text,(100,100))
        screen.blit(gastado_oro_text,(100,130))
        screen.blit(oro_segundo_text,(100,160))
        screen.blit(oro_click_text,(100,190))

        screen.blit(total_madera_text,(100,260))
        screen.blit(gastada_madera_text,(100,290))
        screen.blit(madera_segundo_text,(100,320))
        screen.blit(madera_click_text,(100,350))

        screen.blit(total_magia_text,(100,420))
        screen.blit(gastada_magia_text,(100,450))
        screen.blit(magia_segundo_text,(100,480))
        screen.blit(total_mejoras_text,(100,550))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if pantalla_principal_rect.collidepoint(mouse_pos):
                    
                    jugar_partida(partida,trad)

        pygame.display.update()
        fps.tick(60)

menu_principal()