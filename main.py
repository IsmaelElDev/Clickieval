import pygame,random
from sys import exit
from servicios.database import Base, create_tables, SessionLocal
# Then other modules
from entidades.partida import Partida
from entidades.upgrade import Upgrade
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
from random import randrange
from ui.boton import Boton
from servicios.database_operations import guardar_partida,buscar_partidas,cargar_partida,conectar_db
from ui.mejoratarjeta import MejoraTarjeta
from ui.caja import Caja

def get_font(size): # Devuelve la fuente con el tamaño deseado
    return pygame.font.Font('graphics/fonts/georgiab.ttf', size)

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


gold_surface = pygame.Surface((240, 250),pygame.SRCALPHA)
gold_rect = gold_surface.get_rect(topleft=(380,275))
gold_surface.fill((0,0,0,0))

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
partida = Partida("Ismael")

# Sonido de monedas
gold_sound = pygame.mixer.Sound('fx/monedas.mp3')
sound_delay = 900  # 900 milisegundos de espera
last_sound_time = -sound_delay  # Última vez que se reprodujo el sonido

# Creacion eventos

evento_guerra = Evento('Guerra','Te quita aldeanos si no tienes tantos soldados',0.9,1,600000)
evento_despertar_ruinas = Evento('Despertar Ruinas','Genera mas oro por click',0.99,2,10000)

# Definir upgrades
aldeano = Aldeano('Aldeano', 50, 1, 'Aldeano', 1.24)
lenyador = Lenyador('Lenyador',150,5,'Suma',1.32)
arquero = Arquero('Arquero',100,5,'Suma',1.30)
picaro = Picaro('Picaro',1000,3000,35000,0,'Suma',1.20)
mago = Mago('Mago',2000,1000,'Suma',1.25)
bardo = Bardo('Bardo',500,2,'Bardo',1.10)
soldado = Soldado('Soldado',5000,50,'Soldado',1.20)
clerigo = Clerigo('Clerigo',2000,150,'Clerigo',1.19)
druida = Druida('Druida',4000,1.3,'Druida',1.18)
bruja = Bruja('Bruja',10000,500,'Bruja',1.16)
noble = Noble('Noble',50000,2000,'Noble',1.20)
princesa = Princesa('Princesa',160000,5300,'Princesa',1.30)
reina = Reina('Princesa',520000,10000,'Reina',1.50)
rey = Rey('Rey',1500000,1.1,'Rey',1.60)

scroll_y = 0
scroll_speed = 20
surface_height = 1000  # Altura total del contenido (ajústala)
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
pygame.time.set_timer(PICARO_TICK, 5000)
pygame.time.set_timer(GUERRA_TICK, evento_guerra.enfriamiento)
pygame.time.set_timer(DESPERTAR_TICK, evento_despertar_ruinas.enfriamiento)
# Crear tarjetas al inicio
mejoras = [
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
moneda_img = pygame.transform.scale(moneda_img, (16, 16))  # Ajusta tamaño si es necesario


particulas = []  # Lista para almacenar partículas activas







def recuperar_costes_aldeanos(aldeano, partida):
    
    max_coste = aldeano.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Aldeano) and mejora.coste > max_coste:
            max_coste = mejora.coste
    aldeano.coste = max_coste
    if(contarAldeanos(partida) !=0):
        aldeano.actualizarPrecio()  # Update the price for the next purchase

def recuperar_costes_lenyadores(lenyador,partida):

    max_coste = lenyador.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Lenyador) and mejora.coste > max_coste:
            max_coste = mejora.coste
    lenyador.coste = max_coste
    if(contarLenyadores(partida) !=0):
        lenyador.actualizarPrecio()  # Update the price for the next purchase
    
  

def recuperar_costes_arqueros(arquero,partida):

    max_coste = arquero.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Arquero) and mejora.coste > max_coste:
            max_coste = mejora.coste
    arquero.coste = max_coste
    if(contarArqueros(partida) !=0):
        arquero.actualizarPrecio()  # Update the price for the next purchase
    
def recuperar_costes_picaros(picaro,partida):

    max_coste = picaro.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Picaro) and mejora.coste > max_coste:
            max_coste = mejora.coste
    picaro.coste = max_coste
    if(contarPicaros(partida) !=0):
        picaro.actualizarPrecio()  # Update the price for the next purchase
    
def recuperar_costes_magos(mago,partida):

    max_coste = mago.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Mago) and mejora.coste > max_coste:
            max_coste = mejora.coste
    mago.coste = max_coste
    if(contarMagos(partida) !=0):
        mago.actualizarPrecio()  # Update the price for the next purchase 

def recuperar_costes_bardos(bardo, partida):
    
    max_coste = bardo.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Bardo) and mejora.coste > max_coste:
            max_coste = mejora.coste
    bardo.coste = max_coste
    if(contarBardos(partida) !=0):
        bardo.actualizarPrecio()  # Update the price for the next purchase

def recuperar_costes_soldados(soldado,partida):

    max_coste = soldado.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Soldado) and mejora.coste > max_coste:
            max_coste = mejora.coste
    soldado.coste = max_coste
    if(contarSoldados(partida) !=0):
        soldado.actualizarPrecio()  # Update the price for the next purchase 

def recuperar_costes_clerigos(clerigo,partida):

    max_coste = clerigo.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Clerigo) and mejora.coste > max_coste:
            max_coste = mejora.coste
    clerigo.coste = max_coste
    if(contarClerigos(partida) !=0):
        clerigo.actualizarPrecio()  # Update the price for the next purchase 

def recuperar_costes_druidas(druida,partida):

    max_coste = druida.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Druida) and mejora.coste > max_coste:
            max_coste = mejora.coste
    druida.coste = max_coste
    if(contarDruidas(partida) !=0):
        druida.actualizarPrecio()  # Update the price for the next purchase 

def recuperar_costes_brujas(bruja,partida):

    max_coste = bruja.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Bruja) and mejora.coste > max_coste:
            max_coste = mejora.coste
    bruja.coste = max_coste
    if(contarBrujas(partida) !=0):
        bruja.actualizarPrecio()  # Update the price for the next purchase 

def recuperar_costes_nobles(noble,partida):

    max_coste = noble.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Noble) and mejora.coste > max_coste:
            max_coste = mejora.coste
    noble.coste = max_coste
    if(contarNobles(partida) !=0):
        noble.actualizarPrecio()  # Update the price for the next purchase 

def recuperar_costes_princesas(princesa, partida):
    
    max_coste = princesa.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Princesa) and mejora.coste > max_coste:
            max_coste = mejora.coste
    princesa.coste = max_coste
    if(contarPrincesas(partida) !=0):
        princesa.actualizarPrecio()  # Update the price for the next purchase

def recuperar_costes_reinas(reina, partida):
    
    max_coste = reina.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Reina) and mejora.coste > max_coste:
            max_coste = mejora.coste
    reina.coste = max_coste
    if(contarReinas(partida) !=0):
        reina.actualizarPrecio()  # Update the price for the next purchase

def recuperar_costes_reyes(rey, partida):
    
    max_coste = rey.coste
    for mejora in partida.mejoras:
        if isinstance(mejora, Rey) and mejora.coste > max_coste:
            max_coste = mejora.coste
    rey.coste = max_coste
    if(contarReyes(partida) !=0):
        rey.actualizarPrecio()  # Update the price for the next purchase

def recuperar_multiplicadores_bardos(aldeano,lenyador,partida):

    bardos = contarBardos(partida)
    multiplicador = 2**bardos

    print(contarBardos(partida))
    aldeano.produccion *= multiplicador
    print(aldeano.produccion)
    lenyador.produccion *= multiplicador
    print(lenyador.produccion)
    #partida.oro_por_segundo = aldeano.produccion
    #partida.madera_por_segundo = lenyador.produccion

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

    recuperar_multiplicadores_bardos(aldeano,lenyador,partida)
    recuperar_costes_aldeanos(aldeano,partida)
    recuperar_costes_lenyadores(lenyador,partida)
    recuperar_costes_arqueros(arquero,partida)
    recuperar_costes_picaros(picaro,partida)
    recuperar_costes_magos(mago,partida)
    recuperar_costes_soldados(soldado,partida)
    recuperar_costes_clerigos(clerigo,partida)
    recuperar_costes_druidas(druida,partida)
    recuperar_costes_brujas(bruja,partida)
    recuperar_costes_nobles(noble,partida)
    recuperar_costes_princesas(princesa,partida)
    recuperar_costes_reinas(reina,partida)
    recuperar_costes_reyes(rey,partida)
    recuperar_costes_bardos(bardo, partida)
    

def pantalla_cargar_partida():
    """Muestra una pantalla para seleccionar partidas guardadas"""
    
    # Obtener todas las partidas guardadas
    db = conectar_db()
    partidas = db.query(Partida).all()
    db.close()
    
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
        titulo = get_font(50).render("Cargar Partida", True, "#ffffff")
        titulo_rect = titulo.get_rect(center=(500, 100))
        screen.blit(titulo, titulo_rect)
        
        # Mostrar partidas de la página actual
        inicio = pagina_actual * partidas_por_pagina
        fin = min(inicio + partidas_por_pagina, len(partidas))
        
        for i, partida in enumerate(partidas[inicio:fin]):
            y_pos = 200 + i * 60
            
            # Crear texto para cada partida
            texto = f"ID: {partida.id} - Jugador: {partida.nombre_jugador} - Oro: {partida.oro}"
            color = "#f0c67d" if i == seleccion else "#8f836e"
            
            partida_text = get_font(25).render(texto, True, color)
            partida_rect = partida_text.get_rect(center=(500, y_pos))
            screen.blit(partida_text, partida_rect)
        
        # Botones de navegación y selección
        volver = Boton(None, (250, 600), "Volver", get_font(30), "#8f836e", "#f0c67d")
        siguiente = Boton(None, (750, 600), "Siguiente", get_font(30), "#8f836e", "#f0c67d")
        anterior = Boton(None, (500, 600), "Anterior", get_font(30), "#8f836e", "#f0c67d")
        cargar = Boton(None, (500, 500), "Cargar Seleccionada", get_font(30), "#8f836e", "#f0c67d")
        
        mouse_pos = pygame.mouse.get_pos()
        
        for boton in [volver, siguiente, anterior, cargar]:
            boton.changeColor(mouse_pos)
            boton.update(screen)
        
        # Indicador de página
        pagina_text = get_font(20).render(f"Página {pagina_actual + 1}/{total_paginas}", True, "#ffffff")
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                    jugar_partida(partidacargada)

        pygame.display.update()
        fps.tick(60)


def menu_principal():
    create_tables()
    buscar_partidas()
    while True:
        fondo = pygame.image.load('graphics/background/Background.png')
        screen.blit(fondo,(0,0))
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(60).render("Menu principal",True,"#ffffff")
        menu_rect = menu_text.get_rect(center=(500,100))
        nueva_partida = Boton(None,(500,250),"Nueva partida",get_font(35),"#8f836e","#f0c67d")
        cargar_partida = Boton(None,(500,370),"Cargar partida",get_font(35),"#8f836e","#f0c67d")


        for button in [nueva_partida,cargar_partida]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nueva_partida.checkForInput(mouse_pos):
                    partidanueva = Partida("Ismael")
                    jugar_partida(partidanueva)
                elif cargar_partida.checkForInput(mouse_pos):
                    pantalla_cargar_partida()

        screen.blit(menu_text,menu_rect)
        pygame.display.update()
        fps.tick(60)

def contarAldeanos(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Aldeano))

def contarLenyadores(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Lenyador))

def contarArqueros(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Arquero))

def contarPicaros(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Picaro))

def contarMagos(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Mago))

def contarBardos(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Bardo))

def contarSoldados(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Soldado))

def contarClerigos(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Clerigo))

def contarDruidas(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Druida))

def contarBrujas(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Bruja))

def contarNobles(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Noble))

def contarPrincesas(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Princesa))

def contarReinas(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Reina))

def contarReyes(partida):
     return sum (1 for mejora in partida.mejoras if isinstance(mejora, Rey))

def contarMejoras(partida):
    return sum (1 for mejora in partida.mejoras if isinstance(mejora, Upgrade))


def jugar_partida(partida):
    global aldeano_rect
    while True:
        #screen.fill((30, 30, 30))  # Fondo
        screen.blit(fondo_actual)

        # Obtener tiempo actual
        current_time = pygame.time.get_ticks()

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guardar_partida(partida)
                pygame.quit()
                exit()
                

            gestion_eventos(event,partida,current_time,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble)
            eventoActivado = activador_evento(evento_guerra,evento_despertar_ruinas,partida,event)
            verificarDurEventos(evento_despertar_ruinas,partida,current_time)
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


        upgrade_list_surface.fill('Red')  # Fondo (opcional)
        background_image = pygame.image.load('graphics/background/Background.png')
        background_image = pygame.transform.scale(background_image, (upgrade_list_surface.get_width(), upgrade_list_surface.get_height()))
        upgrade_list_surface.blit(background_image, (0, 0))
    



        pintarMejoras(partida,aldeano_surface,lenyador_surface,arquero_surface,picaro_surface,mago_surface,bardo_surface,soldado_surface,clerigo_surface,druida_surface,bruja_surface,noble_surface,princesa_surface,reina_surface,rey_surface,upgrade_list_surface,scroll_y)



        screen.blit(gold_surface, gold_rect.topleft)
        screen.blit(refrescar_surface,refrescar_rect.topleft)
        screen.blit(tienda_surface,tienda_rect.topleft)
        if(partida.pantalla_estadisticas == True):
            screen.blit(stats_surface,stats_rect)


        # Mostrar el oro en pantalla
        fuente_mejoras = get_font(20)
        gold_text = font.render(f'Oro: {formatear_numero(partida.oro)}', True, (255, 255, 0))
        madera_text = font.render(f'Madera: {formatear_numero(partida.madera)} ',True, (28,105,21))
        magia_text = font.render(f'Magia: {formatear_numero(partida.magia)} ',True, (223, 186, 245))




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

def gestion_eventos(event,partida,current_time,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble):
    global last_sound_time  # Permite modificar la variable global
    global scroll_speed
    global scroll_y
    global fondo_actual

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
        if gold_rect.collidepoint(event.pos) and fondo_actual == mazmorra_surface:  # Si clic en el cofre
            partida.oro += partida.oro_por_click
            partida.oro_total += partida.oro_por_click
            # ✅ Esto crea varias partículas (por ejemplo 10)
            for _ in range(10):
                pos = [event.pos[0], event.pos[1]]
                vel = [random.uniform(-2.4, 1.4), random.uniform(-2.5, -1)]
                particulas.append(Particula(pos, vel,pygame.image.load("fx/moneda.png").convert_alpha()))



            # ✅ Reproducir sonido SOLO si han pasado 2 segundos desde el último
            if current_time - last_sound_time >= sound_delay:
                gold_sound.play()
                last_sound_time = current_time  # Actualizar tiempo del último sonido

        elif gold_rect.collidepoint(event.pos) and fondo_actual == arbol_surface:
            partida.madera += partida.madera_por_click
            partida.madera_total += partida.madera_por_click
            for _ in range(10):
                pos = [event.pos[0], event.pos[1]]
                vel = [random.uniform(-2.4, 1.4), random.uniform(-2.5, -1)]
                particulas.append(Particula(pos, vel,pygame.image.load("fx/tronco.png").convert_alpha()))


        
        elif refrescar_rect.collidepoint(event.pos):
            if fondo_actual == mazmorra_surface:
                fondo_actual = arbol_surface
            else:
                fondo_actual = mazmorra_surface

        elif tienda_rect.collidepoint(event.pos):
            menu_tienda(partida)

        elif stats_rect.collidepoint(event.pos) and partida.pantalla_estadisticas == True:
            menu_stats(partida)

        # ✅ Solo llamar comprar_mejora si se hace clic
        comprar_mejora(partida,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey,event)

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            menu_escape(partida)
    
    

    
    elif event.type == pygame.MOUSEWHEEL:
        if upgrade_list_rect.collidepoint(pygame.mouse.get_pos()):  # Solo si el ratón está sobre el Surface
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
            picaros = contarPicaros(partida)
            if picaros > 0:
                for upgrade in partida.mejoras:
                    if isinstance(upgrade, Picaro):
                        produccion = upgrade.calculo_produccion()
                        print(produccion)
                        partida.oro += produccion
                        partida.oro_total += produccion
        except Exception as e:
            print(f"Error processing Picaro tick: {e}")

def comprar_aldeano(partida,aldeano,event):
    # Guardar el coste actual antes de comprar
    current_cost = aldeano.coste
    current_production = aldeano.produccion
    current_inc_precio = aldeano.incPrecio
    
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    partida.oro_por_segundo += current_production

    partida.oro_gastado += current_cost
        
    # Nueva instancia de aldeano para añadir a la lista 
    new_aldeano = Aldeano('Aldeano', current_cost, current_production, 'Aldeano', current_inc_precio)
    new_aldeano.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_aldeano)  # Añadir a la lista
        
    print(f"Aldeanos: {contarAldeanos(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {aldeano.coste}")

    # Actualizar el precio para la próxima compra
    aldeano.actualizarPrecio()

def comprar_lenyador(partida,lenyador,event):
    # Guardar el coste actual antes de comprar
    current_cost = lenyador.coste
    current_production = lenyador.produccion
    current_inc_precio = lenyador.incPrecio
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    partida.madera_por_segundo += current_production

    partida.oro_gastado += current_cost
        
    # Nueva instancia de lenyador para añadir a la lista 
    new_lenyador = Lenyador('Lenyador', current_cost, current_production, 'Lenyador', current_inc_precio)
    new_lenyador.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_lenyador)  # Añadir a la lista
        
    print(f"Lenyadores: {contarLenyadores(partida)}, Madera por segundo: {partida.madera_por_segundo}, Coste: {lenyador.coste}")

    # Actualizar el precio para la próxima compra
    lenyador.actualizarPrecio()

def comprar_arquero(partida,arquero,event):
    # Guardar el coste actual antes de comprar
    current_cost = arquero.coste
    current_production = arquero.produccion
    current_inc_precio = arquero.incPrecio
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    partida.madera -= current_cost
    partida.oro_por_segundo += current_production
    partida.oro_por_click += current_production

    partida.oro_gastado += current_cost
    partida.madera_gastada += current_cost
        
    # Nueva instancia de lenyador para añadir a la lista 
    new_arquero = Arquero('Arquero', current_cost, current_production, 'Arquero', current_inc_precio)
    new_arquero.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_arquero)  # Añadir a la lista
        
    print(f"Arqueros: {contarArqueros(partida)}, Oro por segundo: {partida.oro_por_segundo}, Oro por click:{partida.oro_por_click}, Coste: {arquero.coste}")

    # Actualizar el precio para la próxima compra
    arquero.actualizarPrecio()

def comprar_picaro(partida,picaro,event):
    # Guardar el coste actual antes de comprar
    current_cost = picaro.coste
    current_produccion = picaro.produccion
    current_inc_precio = picaro.incPrecio
    current_min_produccion = picaro.min_produccion
    current_max_produccion = picaro.max_produccion
        
    # Actualizar variables del juego
    partida.oro -= current_cost

    partida.oro_gastado += current_cost
        
    # Nueva instancia de lenyador para añadir a la lista 
    new_picaro = Picaro('Picaro', current_cost, current_min_produccion,current_max_produccion,current_produccion, 'Picaro', current_inc_precio)
    new_picaro.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_picaro)  # Añadir a la lista
        
    print(f"Picaros: {contarPicaros(partida)}, Coste: {picaro.coste}, Produccion: {picaro.produccion}")

    # Actualizar el precio para la próxima compra
    picaro.actualizarPrecio()

def comprar_mago(partida,mago,event):
    # Guardar el coste actual antes de comprar
    current_cost = mago.coste
    current_production = mago.produccion
    current_inc_precio = mago.incPrecio
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    partida.magia_por_segundo += current_production

    partida.oro_gastado += current_cost
        
    # Nueva instancia de aldeano para añadir a la lista 
    new_mago = Mago('Mago', current_cost, current_production, 'Mago', current_inc_precio)
    new_mago.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_mago)  # Añadir a la lista
        
    print(f"Magos: {contarMagos(partida)}, Magia por segundo: {partida.magia_por_segundo}, Coste: {mago.coste}")

    # Actualizar el precio para la próxima compra
    mago.actualizarPrecio()

def comprar_bardo(partida,bardo,event):
    # Guardar el coste actual antes de comprar
    current_cost = bardo.coste
    current_production = bardo.produccion
    current_inc_precio = bardo.incPrecio
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    partida.magia -= current_cost
    aldeano.produccion *= bardo.produccion
    lenyador.produccion *= bardo.produccion

    partida.oro_gastado += current_cost
    partida.magia_gastada += current_cost

    for mejora in partida.mejoras:
        if isinstance(mejora,Aldeano) or isinstance(mejora,Lenyador):
            mejora.produccion *= bardo.produccion
            if isinstance(mejora,Aldeano):
                partida.oro_por_segundo = aldeano.produccion
            elif isinstance(mejora,Lenyador):
                partida.madera_por_segundo = lenyador.produccion

    # Nueva instancia de aldeano para añadir a la lista 
    new_bardo = Bardo('Bardo', current_cost, current_production, 'Bardo', current_inc_precio)
    new_bardo.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_bardo)  # Añadir a la lista
        
    # Actualizar el precio para la próxima compra
    bardo.actualizarPrecio()

def comprar_soldado(partida,soldado,event):
    # Guardar el coste actual antes de comprar
    current_cost = soldado.coste
    current_production = soldado.produccion
    current_inc_precio = soldado.incPrecio
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    partida.oro_por_click += current_production

    partida.oro_gastado += current_cost
        
    # Nueva instancia de lenyador para añadir a la lista 
    new_soldado = Soldado('Soldado', current_cost, current_production, 'Soldado', current_inc_precio)
    new_soldado.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_soldado)  # Añadir a la lista
        
    print(f"Soldados: {contarSoldados(partida)}, Oro por click:{partida.oro_por_click}, Coste: {soldado.coste}")

    # Actualizar el precio para la próxima compra
    soldado.actualizarPrecio()

def comprar_clerigo(partida,clerigo,event):
    # Guardar el coste actual antes de comprar
    current_cost = clerigo.coste
    current_production = clerigo.produccion
    current_inc_precio = clerigo.incPrecio
        
    # Actualizar variables del juego
    partida.magia -= current_cost
    partida.magia_por_segundo += current_production

    partida.magia_gastada += current_cost
        
    # Nueva instancia de lenyador para añadir a la lista 
    new_clerigo = Clerigo('Clerigo', current_cost, current_production, 'Clerigo', current_inc_precio)
    new_clerigo.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_clerigo)  # Añadir a la lista
        
    print(f"Clerigos: {contarClerigos(partida)}, Oro por segundo:{partida.magia_por_segundo}, Coste: {clerigo.coste}")

    # Actualizar el precio para la próxima compra
    clerigo.actualizarPrecio()

def comprar_druida(partida,druida,event):
    # Guardar el coste actual antes de comprar
    current_cost = druida.coste
    current_production = druida.produccion
    current_inc_precio = druida.incPrecio
        
    # Actualizar variables del juego
    partida.madera -= current_cost
    partida.magia -= current_cost
    mago.produccion *= druida.produccion
    clerigo.produccion *= druida.produccion

    partida.madera_gastada += current_cost
    partida.magia_gastada += current_cost

    for mejora in partida.mejoras:
        if isinstance(mejora,Mago) or isinstance(mejora,Clerigo):
            mejora.produccion *= druida.produccion
            if isinstance(mejora,Mago):
                partida.magia_por_segundo = mago.produccion
            elif isinstance(mejora,Clerigo):
                partida.magia_por_segundo = clerigo.produccion

    # Nueva instancia de aldeano para añadir a la lista 
    new_druida = Druida('Druida', current_cost, current_production, 'Druida', current_inc_precio)
    new_druida.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_druida)  # Añadir a la lista
        
    # Actualizar el precio para la próxima compra
    druida.actualizarPrecio()

def comprar_bruja(partida,bruja,event):
    # Guardar el coste actual antes de comprar
    current_cost = bruja.coste
    current_production = bruja.produccion
    current_inc_precio = bruja.incPrecio
        
    # Actualizar variables del juego
    partida.magia -= current_cost
    partida.oro_por_segundo += current_production

    partida.magia_gastada += current_cost

        
    # Nueva instancia de aldeano para añadir a la lista 
    new_bruja = Bruja('Bruja', current_cost, current_production, 'Bruja', current_inc_precio)
    new_bruja.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_bruja)  # Añadir a la lista
        
    print(f"Brujas: {contarBrujas(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {bruja.coste}")

    # Actualizar el precio para la próxima compra
    bruja.actualizarPrecio()

def comprar_noble(partida,noble,event):
    # Guardar el coste actual antes de comprar
    current_cost = noble.coste
    current_production = noble.produccion
    current_inc_precio = noble.incPrecio
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    partida.oro_por_segundo += current_production

    partida.oro_gastado += current_cost
        
    # Nueva instancia de aldeano para añadir a la lista 
    new_noble = Noble('Noble', current_cost, current_production, 'Noble', current_inc_precio)
    new_noble.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_noble)  # Añadir a la lista
        
    print(f"Nobles: {contarNobles(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {noble.coste}")

    # Actualizar el precio para la próxima compra
    noble.actualizarPrecio()

def comprar_princesa(partida,princesa,event):
    # Guardar el coste actual antes de comprar
    current_cost = princesa.coste
    current_production = princesa.produccion
    current_inc_precio = princesa.incPrecio
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    partida.oro_por_click += current_production

    partida.oro_gastado += current_cost
        
    # Nueva instancia de aldeano para añadir a la lista 
    new_princesa = Princesa('Princesa', current_cost, current_production, 'Princesa', current_inc_precio)
    new_princesa.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_princesa)  # Añadir a la lista
        
    print(f"Princesas: {contarPrincesas(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {princesa.coste}")

    # Actualizar el precio para la próxima compra
    princesa.actualizarPrecio()

def comprar_reina(partida,reina,event):
    # Guardar el coste actual antes de comprar
    current_cost = reina.coste
    current_production = reina.produccion
    current_inc_precio = reina.incPrecio
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    partida.oro_por_segundo += current_production

    partida.oro_gastado += current_cost
        
    # Nueva instancia de aldeano para añadir a la lista 
    new_reina = Reina('Reina', current_cost, current_production, 'Reina', current_inc_precio)
    new_reina.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_reina)  # Añadir a la lista
        
    print(f"Reinas: {contarReinas(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {reina.coste}")

    # Actualizar el precio para la próxima compra
    reina.actualizarPrecio()

def comprar_rey(partida,rey,event):
    # Guardar el coste actual antes de comprar
    current_cost = rey.coste
    current_production = rey.produccion
    current_inc_precio = rey.incPrecio
        
    # Actualizar variables del juego
    partida.oro -= current_cost
    aldeano.produccion *= rey.produccion
    lenyador.produccion *= rey.produccion
    arquero.produccion *= rey.produccion
    picaro.produccion *= rey.produccion
    mago.produccion *= rey.produccion
    bardo.produccion *= rey.produccion
    soldado.produccion *= rey.produccion
    clerigo.produccion *= rey.produccion
    druida.produccion *= rey.produccion
    bruja.produccion *= rey.produccion
    noble.produccion *= rey.produccion
    princesa.produccion *= rey.produccion
    reina.produccion *= rey.produccion

    partida.oro_gastado += current_cost

    for mejora in partida.mejoras:
        if isinstance(mejora,Rey):
            pass
        else: mejora.produccion *= rey.produccion
            
        
    # Nueva instancia de aldeano para añadir a la lista 
    new_rey = Rey('Rey', current_cost, current_production, 'Rey', current_inc_precio)
    new_rey.partida = partida  # Establecer relacion para la bd
    partida.mejoras.append(new_rey)  # Añadir a la lista
        
    print(f"Reyes: {contarReyes(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {rey.coste}")

    # Actualizar el precio para la próxima compra
    rey.actualizarPrecio()

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
    if mejoras[0].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= aldeano.coste:
            comprar_aldeano(partida, aldeano, event)
            return
    
    # Leñador
    if mejoras[1].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= lenyador.coste:
            comprar_lenyador(partida, lenyador, event)
            return
    
    # Arquero
    if mejoras[2].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= arquero.coste and partida.madera >= arquero.coste:
            comprar_arquero(partida, arquero, event)
            return
    
    # Pícaro
    elif mejoras[3].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= picaro.coste:
            comprar_picaro(partida, picaro, event)
            return
    
    # Mago
    if mejoras[4].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= mago.coste:
            comprar_mago(partida, mago, event)
            return
        
    # Bardo
    if mejoras[5].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= bardo.coste and partida.magia >= bardo.coste:
            comprar_bardo(partida, bardo, event)
            return
        
    # Soldado
    if mejoras[6].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= soldado.coste:
            comprar_soldado(partida, soldado, event)
            return
        
    # Clerigo
    if mejoras[7].collidepoint((rel_x, rel_y), scroll_y):
        if partida.magia >= clerigo.coste:
            comprar_clerigo(partida, clerigo, event)
            return
        
    # Druida
    if mejoras[8].collidepoint((rel_x, rel_y), scroll_y):
        if partida.madera >= druida.coste and partida.magia >= druida.coste:
            comprar_druida(partida, druida, event)
            return
        
    # Bruja
    if mejoras[9].collidepoint((rel_x, rel_y), scroll_y):
        if partida.magia >= bruja.coste:
            comprar_bruja(partida, bruja, event)
            return
        
    # Noble
    if mejoras[10].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= noble.coste:
            comprar_noble(partida, noble, event)
            return
        
        # Noble
    if mejoras[11].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= princesa.coste:
            comprar_princesa(partida, princesa, event)
            return
        
        # Noble
    if mejoras[12].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= reina.coste:
            comprar_reina(partida, reina, event)
            return
        
        # Noble
    if mejoras[13].collidepoint((rel_x, rel_y), scroll_y):
        if partida.oro >= rey.coste:
            comprar_rey(partida, rey, event)
            return

# Función tooltip_mejoras simplificada:
def tooltip_mejoras(aldeano_locked,lenyador_locked,arquero_locked,picaro_locked,mago_locked,bardo_locked,soldado_locked,clerigo_locked,druida_locked,bruja_locked,noble_locked,princesa_locked,reina_locked,rey_locked):
    mouse_pos = pygame.mouse.get_pos()
    
    # Solo mostrar tooltips cuando el ratón está en el área de mejoras
    if not upgrade_list_rect.collidepoint(mouse_pos):
        return
        
    # Calcular posición relativa del ratón
    rel_x = mouse_pos[0] - upgrade_list_rect.x
    rel_y = mouse_pos[1] - upgrade_list_rect.y + scroll_y
    
    # Comprobar cada área de mejora
    
    # Aldeano
    if aldeano_rect.collidepoint(rel_x, rel_y) and aldeano_locked == False:
        texto = f'Produce: {formatear_numero(aldeano.produccion)} de \noro por segundo'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Leñador
    if lenyador_rect.collidepoint(rel_x, rel_y) and lenyador_locked == False:
        texto = f'Produce: {formatear_numero(lenyador.produccion)} de \nmadera \npor segundo'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Arquero
    if arquero_rect.collidepoint(rel_x, rel_y) and arquero_locked == False:
        texto = f'Produce: {formatear_numero(arquero.produccion)} de \noro por segundo \ny por click'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Pícaro
    if picaro_rect.collidepoint(rel_x, rel_y) and picaro_locked == False:
        texto = f'Produce entre: \n{formatear_numero(picaro.min_produccion)} y {formatear_numero(picaro.max_produccion)} de \noro cada minuto'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Mago
    if mago_rect.collidepoint(rel_x, rel_y) and mago_locked == False:
        texto = f'Produce: {formatear_numero(mago.produccion)} de \nmagia por segundo'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Bardo
    if bardo_rect.collidepoint(rel_x, rel_y) and bardo_locked == False:
        texto = f'Duplica la produccion de \naldeanos y leñadores'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Soldado
    if soldado_rect.collidepoint(rel_x, rel_y) and soldado_locked == False:
        texto = f'Produce: {formatear_numero(soldado.produccion)} de \noro por click'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Clerigo
    if clerigo_rect.collidepoint(rel_x, rel_y) and clerigo_locked == False:
        texto = f'Produce: {formatear_numero(clerigo.produccion)} de \nmagia por segundo'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return

    # Druida
    if druida_rect.collidepoint(rel_x, rel_y) and druida_locked == False:
        texto = f'Duplica la produccion de \nmagos y clerigos'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Bruja
    if bruja_rect.collidepoint(rel_x, rel_y) and bruja_locked == False:
        texto = f'Produce: {formatear_numero(bruja.produccion)} de \noro por segundo'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Noble
    if noble_rect.collidepoint(rel_x, rel_y) and noble_locked == False:
        texto = f'Produce: {formatear_numero(noble.produccion)} de \noro por segundo'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Princesa
    if princesa_rect.collidepoint(rel_x, rel_y) and princesa_locked == False:
        texto = f'Produce: {formatear_numero(princesa.produccion)} de \noro por click'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Reina
    if reina_rect.collidepoint(rel_x, rel_y) and reina_locked == False:
        texto = f'Produce: {formatear_numero(reina.produccion)} de \noro por segundo'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return
    
    # Rey
    if rey_rect.collidepoint(rel_x, rel_y) and rey_locked == False:
        texto = f'Mejora la\n produccion de\n todas las mejoras\n por: {rey.produccion}'
        screen.blit(get_font(12).render(texto, True, (255,255,255)), 
                   (mouse_pos[0] - 125, mouse_pos[1] - 30))
        return

#SIN IMPLEMENTAR!!!!!!111 1 1 1 1 1!! 1 !! !!!
#
#
def incremento_mejoras_exponencial():
    
    incremento_aldeano_exponencial(aldeano,partida)
    incremento_lenyador_exponencial(lenyador,partida)
    incremento_arquero_exponencial(arquero,partida)
    incremento_picaro_exponencial(picaro,partida)
    incremento_mago_exponencial(mago,partida)
    pass

def incremento_aldeano_exponencial(aldeano,partida):
    contador=0
    for mejora in partida.mejoras:
        if mejora.isinstance(mejora,Aldeano):
            contador += 1

def incremento_lenyador_exponencial(lenyador,partida):
    contador=0
    for mejora in partida.mejoras:
        if mejora.isinstance(mejora,Lenyador):
            contador += 1

def incremento_arquero_exponencial(arquero,partida):
    contador=0
    for mejora in partida.mejoras:
        if mejora.isinstance(mejora,Arquero):
            contador += 1

def incremento_picaro_exponencial(picaro,partida):
    contador=0
    for mejora in partida.mejoras:
        if mejora.isinstance(mejora,Picaro):
            contador += 1

def incremento_mago_exponencial(mago,partida):
    contador=0
    for mejora in partida.mejoras:
        if mejora.isinstance(mejora,Mago):
            contador += 1

def menu_escape(partida):
    while True:
        fondo = pygame.image.load('graphics/background/Background.png')
        screen.blit(fondo,(0,0))
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(60).render("Juego en pausa",True,"#ffffff")
        menu_rect = menu_text.get_rect(center=(520,70))
        screen.blit(menu_text,menu_rect)

        bot_guardar_partida = Boton(None,(500,190),"Guardar partida",get_font(35),"#8f836e","#f0c67d")
        bot_cargar_partida = Boton(None,(490,300),"Cargar partida",get_font(35),"#8f836e","#f0c67d")
        bot_volver_juego = Boton(None,(490,420),"Volver al juego",get_font(35),"#8f836e","#f0c67d")
        bot_salir_juego = Boton(None,(490,540),"Salir del juego",get_font(35),"#8f836e","#f0c67d")

        for button in [bot_guardar_partida,bot_cargar_partida,bot_volver_juego,bot_salir_juego]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                guardar_partida(partida)
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bot_guardar_partida.checkForInput(mouse_pos):
                    # Save the game and get a fresh connected copy
                    fresh_partida = guardar_partida(partida)
                    if fresh_partida:
                        partida = fresh_partida
                    # Show confirmation message
                    mensaje = get_font(20).render("¡Partida guardada con éxito!", True, (0, 255, 0))
                    screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
                    pygame.display.update()
                    pygame.time.delay(1000)  # Show message for 1 second
                    
                elif bot_cargar_partida.checkForInput(mouse_pos):
                    loaded_partida = pantalla_cargar_partida()
                    if loaded_partida:
                        recuperar_costes_mejoras(loaded_partida)
                        return loaded_partida  # Return loaded partida to jugar_partida
                
                elif bot_volver_juego.checkForInput(mouse_pos):
                    return partida  # Return current partida
                
                elif bot_salir_juego.checkForInput(mouse_pos):
                    guardar_partida(partida)  # Save before exit
                    pygame.quit()
                    exit()

        pygame.display.update()
        fps.tick(60)

def menu_tienda(partida):
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

        estadisticas_surface = pygame.image.load('graphics/icons/stats.png')
        estadisticas_comprar_bot = Boton(None, (150, 240), "Comprar pantalla\nde estadisticas", get_font(20), "#8f836e", "#f0c67d")
        screen.blit(estadisticas_surface,(140,140))
        estadisticas_comprar_bot.changeColor(mouse_pos)
        estadisticas_comprar_bot.update(screen)

 

        caja2_s1= pygame.Surface((240,10))
        caja2_r1 = caja2_s1.get_rect(topleft=(360,40))
        caja2_s2= pygame.Surface((10,240))
        caja2_r2 = caja2_s2.get_rect(topleft=(360,40))
        caja2_s3= pygame.Surface((240,10))
        caja2_r3 = caja2_s3.get_rect(topleft=(360,280))
        caja2_s4= pygame.Surface((10,240))
        caja2_r4 = caja2_s4.get_rect(topleft=(590,40))  

        caja3_s1= pygame.Surface((240,10))
        caja3_r1 = caja3_s1.get_rect(topleft=(690,40))
        caja3_s2= pygame.Surface((10,240))
        caja3_r2 = caja3_s2.get_rect(topleft=(690,40))
        caja3_s3= pygame.Surface((240,10))
        caja3_r3 = caja3_s3.get_rect(topleft=(690,280))
        caja3_s4= pygame.Surface((10,240))
        caja3_r4 = caja3_s4.get_rect(topleft=(920,40))

        caja4_s1= pygame.Surface((240,10))
        caja4_r1 = caja4_s1.get_rect(topleft=(30,340))
        caja4_s2= pygame.Surface((10,240))
        caja4_r2 = caja4_s2.get_rect(topleft=(30,340))
        caja4_s3= pygame.Surface((240,10))
        caja4_r3 = caja4_s3.get_rect(topleft=(30,580))
        caja4_s4= pygame.Surface((10,240))
        caja4_r4 = caja4_s4.get_rect(topleft=(260,340))

        caja5_s1= pygame.Surface((240,10))
        caja5_r1 = caja5_s1.get_rect(topleft=(360,340))
        caja5_s2= pygame.Surface((10,240))
        caja5_r2 = caja5_s2.get_rect(topleft=(360,340))
        caja5_s3= pygame.Surface((240,10))
        caja5_r3 = caja5_s3.get_rect(topleft=(360,580))
        caja5_s4= pygame.Surface((10,240))
        caja5_r4 = caja5_s4.get_rect(topleft=(590,340))

        caja6_s1= pygame.Surface((240,10))
        caja6_r1 = caja6_s1.get_rect(topleft=(690,340))
        caja6_s2= pygame.Surface((10,240))
        caja6_r2 = caja6_s2.get_rect(topleft=(690,340))
        caja6_s3= pygame.Surface((240,10))
        caja6_r3 = caja6_s3.get_rect(topleft=(690,580))
        caja6_s4= pygame.Surface((10,240))
        caja6_r4 = caja6_s4.get_rect(topleft=(920,340))

        caja1 = Caja(caja1_s1,caja1_r1,caja1_s2,caja1_r2,caja1_s3,caja1_r3,caja1_s4,caja1_r4)
        caja2 = Caja(caja2_s1,caja2_r1,caja2_s2,caja2_r2,caja2_s3,caja2_r3,caja2_s4,caja2_r4)
        caja3 = Caja(caja3_s1,caja3_r1,caja3_s2,caja3_r2,caja3_s3,caja3_r3,caja3_s4,caja3_r4)
        caja4 = Caja(caja4_s1,caja4_r1,caja4_s2,caja4_r2,caja4_s3,caja4_r3,caja4_s4,caja4_r4)
        caja5 = Caja(caja5_s1,caja5_r1,caja5_s2,caja5_r2,caja5_s3,caja5_r3,caja5_s4,caja5_r4)
        caja6 = Caja(caja6_s1,caja6_r1,caja6_s2,caja6_r2,caja6_s3,caja6_r3,caja6_s4,caja6_r4)

        caja1.draw(screen)
        caja2.draw(screen)
        caja3.draw(screen)
        caja4.draw(screen)
        caja5.draw(screen)
        caja6.draw(screen)

            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if pantalla_principal_rect.collidepoint(mouse_pos):
                    jugar_partida(partida)
                elif estadisticas_comprar_bot.checkForInput(mouse_pos) and partida.oro >= 1000:
                    partida.oro -= 1000
                    partida.pantalla_estadisticas = True
                    partida.oro_gastado += 1000
                    
           
        
        pygame.display.update()
        fps.tick(60)

def formatear_numero(numero):
    if numero < 1000:
        return str(int(numero))  # aseguramos entero
    elif numero < 1_000_000:
        valor = round(numero / 1000, 1)
        return f"{valor}k".replace(".0k", "k")
    elif numero < 1_000_000_000:
        valor = round(numero / 1_000_000, 1)
        return f"{valor}M".replace(".0M", "M")
    else:
        valor = round(numero / 1_000_000_000, 1)
        return f"{valor}B".replace(".0B", "B")

    
def activador_evento(evento_guerra, evento_despertar_ruinas, partida, event):
    if not evento_guerra.activo and contarSoldados(partida) < 5 and event.type == GUERRA_TICK and evento_guerra.sucedeEvento():
        evento_guerra.efectoEvento(partida)
        mensaje = get_font(20).render(f"El evento {evento_guerra.nombre} ha comenzado.\n{evento_despertar_ruinas.descripcion}", True, (0, 255, 0))
        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
        pygame.display.update()
        pygame.time.delay(1500)  # Show message for 1 second
        partida.eventos.append(evento_guerra.nuevaInstancia())
        return True

    elif not evento_despertar_ruinas.activo and event.type == DESPERTAR_TICK and evento_despertar_ruinas.sucedeEvento(): 
        evento_despertar_ruinas.efectoEvento(partida)
        
        mensaje = get_font(20).render(f"El evento {evento_despertar_ruinas.nombre} ha comenzado.\n{evento_despertar_ruinas.descripcion}", True, (0, 255, 0))
        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
        pygame.display.update()
        pygame.time.delay(1500)  # Show message for 1 second
        partida.eventos.append(evento_despertar_ruinas.nuevaInstancia())
        return True
    
    
    return False


def verificarDurEventos(evento_despertar_ruinas,partida,current_time):
    if evento_despertar_ruinas.verificarDuracion(partida,current_time) == True:
        mensaje = get_font(20).render(f"El evento {evento_despertar_ruinas.nombre} ha terminado.", True, (0, 255, 0))
        screen.blit(mensaje, (500 - mensaje.get_width() // 2, 600))
        pygame.display.update()
        pygame.time.delay(1500)  # Show message for 1 second

def pintarMejoras(partida,aldeano_surface,lenyador_surface,arquero_surface,picaro_surface,mago_surface,bardo_surface,soldado_surface,clerigo_surface,druida_surface,bruja_surface,noble_surface,princesa_surface,reina_surface,rey_surface,upgrade_list_surface,scroll_y):

    aldeano_locked = False
    lenyador_locked = False
    arquero_locked = False
    picaro_locked = False
    mago_locked = False
    bardo_locked = False
    soldado_locked = False
    clerigo_locked = False
    druida_locked = False
    bruja_locked = False
    noble_locked = False
    princesa_locked = False
    reina_locked = False
    rey_locked = False

    if partida.oro >= aldeano.coste:
        aldeano_nombre_text = get_font(20).render(f"Aldeanos: {contarAldeanos(partida)}", True, (255, 255, 0))
        aldeano_coste_text = get_font(15).render(f'Coste: {formatear_numero(aldeano.coste)} de oro',True,(255,255,0))
        aldeano_surface = pygame.image.load('graphics/icons/aldeano.png')
    elif partida.oro < aldeano.coste and contarAldeanos(partida) > 0: 
        aldeano_coste_text = get_font(15).render(f'Coste: {formatear_numero(aldeano.coste)} de oro',True,( 101, 101, 101 )) 
        aldeano_nombre_text = get_font(20).render(f"Aldeanos: {contarAldeanos(partida)}", True, (101,101,101))
        aldeano_surface = pygame.image.load('graphics/icons/aldeano_baw.png')
    else:
        aldeano_coste_text = get_font(15).render(f'Coste: ?? de oro',True,( 101, 101, 101 )) 
        aldeano_nombre_text = get_font(20).render(f"????????", True, (101,101,101))
        aldeano_locked = True

    

    if partida.oro >= lenyador.coste:
        lenyador_nombre_text = get_font(20).render(f"Leñadores: {contarLenyadores(partida)}", True, (255, 255, 0))
        lenyador_coste_text = get_font(15).render(f'Coste: {formatear_numero(lenyador.coste)} de oro',True,(255,255,0))
        lenyador_surface = pygame.image.load('graphics/icons/lenyador.png')

    elif partida.oro <= lenyador.coste and contarLenyadores(partida) > 0: 
        lenyador_coste_text = get_font(15).render(f'Coste: {formatear_numero(lenyador.coste)} de oro',True,( 101, 101, 101 )) 
        lenyador_nombre_text = get_font(20).render(f"Leñadores: {contarLenyadores(partida)}", True, (101,101,101))
        lenyador_surface = pygame.image.load('graphics/icons/lenyador_baw.png')
    else:
        lenyador_coste_text = get_font(15).render(f'Coste: ??? de oro',True,( 101, 101, 101 )) 
        lenyador_nombre_text = get_font(20).render(f"????????", True, (101,101,101))
        lenyador_locked = True



    if partida.oro >= arquero.coste and partida.madera >= arquero.coste:
        arquero_nombre_text = get_font(20).render(f"Arqueros: {contarArqueros(partida)}", True, (255, 255, 0))
        arquero_coste_text = get_font(15).render(f'Coste: {formatear_numero(arquero.coste)} de \nmadera y oro',True,(255,255,0))
        arquero_surface = pygame.image.load('graphics/icons/arquero.png')

    elif partida.oro < arquero.coste and contarArqueros(partida) > 0: 
        arquero_coste_text = get_font(15).render(f'Coste: {formatear_numero(arquero.coste)} de \nmadera y oro',True,(101,101,101))
        arquero_nombre_text = get_font(20).render(f"Arqueros: {contarArqueros(partida)}", True, (101,101,101))
        arquero_surface = pygame.image.load('graphics/icons/arquero_baw.png')

    else:
        arquero_coste_text = get_font(15).render(f'Coste: ??? de \nmadera y oro',True,( 101, 101, 101 )) 
        arquero_nombre_text = get_font(20).render(f"????????", True, (101,101,101))
        arquero_locked = True



    if partida.oro >= picaro.coste:
        picaro_nombre_text = get_font(20).render(f"Picaros: {contarPicaros(partida)}", True, (255, 255, 0))
        picaro_coste_text = get_font(15).render(f'Coste: {formatear_numero(picaro.coste)} de oro',True,(255,255,0))
        picaro_surface = pygame.image.load('graphics/icons/picaro.png')

    elif partida.oro < picaro.coste and contarPicaros(partida) > 0: 
        picaro_coste_text = get_font(15).render(f'Coste: {formatear_numero(picaro.coste)} de oro',True,(101,101,101))
        picaro_nombre_text = get_font(20).render(f"Picaros: {contarPicaros(partida)}", True, (101,101,101))
        picaro_surface = pygame.image.load('graphics/icons/picaro_baw.png')

    else: 
        picaro_coste_text = get_font(15).render(f'Coste: ???? de oro',True,(101,101,101))
        picaro_nombre_text = get_font(20).render(f"???????: ", True, (101,101,101))
        picaro_locked = True


    if partida.oro >= mago.coste:
        mago_nombre_text = get_font(20).render(f"Magos: {contarMagos(partida)}", True, (255, 255, 0))
        mago_coste_text = get_font(15).render(f'Coste: {formatear_numero(mago.coste)} de oro',True,(255,255,0))
        mago_surface = pygame.image.load('graphics/icons/mago.png')

    elif partida.oro < mago.coste and contarMagos(partida) > 0: 
        mago_coste_text = get_font(15).render(f'Coste: {formatear_numero(mago.coste)} de oro',True,(101,101,101))
        mago_nombre_text = get_font(20).render(f"Magos: {contarMagos(partida)}", True, (101,101,101))
        mago_surface = pygame.image.load('graphics/icons/mago_baw.png')

    else: 
        mago_coste_text = get_font(15).render(f'Coste: ???? de oro',True,(101,101,101))
        mago_nombre_text = get_font(20).render(f"?????", True, (101,101,101))
        mago_locked = True


    if partida.oro >= bardo.coste and partida.magia >= bardo.coste:
        bardo_nombre_text = get_font(20).render(f"Bardos: {contarBardos(partida)}", True, (255, 255, 0))
        bardo_coste_text = get_font(15).render(f'Coste: {formatear_numero(bardo.coste)} de \noro y magia',True,(255,255,0))
        bardo_surface = pygame.image.load('graphics/icons/bardo.png')

    elif partida.oro < bardo.coste and partida.magia < bardo.coste and contarBardos(partida) > 0: 
        bardo_coste_text = get_font(15).render(f'Coste: {formatear_numero(bardo.coste)} de \noro y magia',True,(101,101,101))
        bardo_nombre_text = get_font(20).render(f"Bardos: {contarBardos(partida)}", True, (101,101,101))
        bardo_surface = pygame.image.load('graphics/icons/bardo_baw.png')

    else: 
        bardo_coste_text = get_font(15).render(f'Coste: ??? de \noro y magia',True,(101,101,101))
        bardo_nombre_text = get_font(20).render(f"???????", True, (101,101,101))
        bardo_locked = True


    if partida.oro >= soldado.coste:
        soldado_nombre_text = get_font(20).render(f"Soldados: {contarSoldados(partida)}", True, (255, 255, 0))
        soldado_coste_text = get_font(15).render(f'Coste: {formatear_numero(soldado.coste)} de \noro',True,(255,255,0))
        soldado_surface = pygame.image.load('graphics/icons/soldado.png')

    elif partida.oro < soldado.coste and contarSoldados(partida) > 0: 
        soldado_coste_text = get_font(15).render(f'Coste: {formatear_numero(soldado.coste)} de \noro',True,(101,101,101))
        soldado_nombre_text = get_font(20).render(f"Soldados: {contarSoldados(partida)}", True, (101,101,101))
        soldado_surface = pygame.image.load('graphics/icons/soldado_baw.png')

    else: 
        soldado_coste_text = get_font(15).render(f'Coste: ???? de \noro',True,(101,101,101))
        soldado_nombre_text = get_font(20).render(f"????????", True, (101,101,101))
        soldado_locked = True


    if partida.magia >= clerigo.coste:
        clerigo_nombre_text = get_font(20).render(f"Clerigos: {contarClerigos(partida)}", True, (255, 255, 0))
        clerigo_coste_text = get_font(15).render(f'Coste: {formatear_numero(clerigo.coste)} de \nmagia',True,(255,255,0))
        clerigo_surface = pygame.image.load('graphics/icons/clerigo.png')

    elif partida.magia < clerigo.coste and contarClerigos(partida) > 0: 
        clerigo_coste_text = get_font(15).render(f'Coste: {formatear_numero(clerigo.coste)} de \nmagia',True,(101,101,101))
        clerigo_nombre_text = get_font(20).render(f"Clerigos: {contarClerigos(partida)}", True, (101,101,101))
        clerigo_surface = pygame.image.load('graphics/icons/clerigo_baw.png')

    else: 
        clerigo_coste_text = get_font(15).render(f'Coste: ???? de \nmagia',True,(101,101,101))
        clerigo_nombre_text = get_font(20).render(f"????????", True, (101,101,101))
        clerigo_locked = True


    if partida.magia >= druida.coste and partida.madera >= druida.coste:
        druida_nombre_text = get_font(20).render(f"Druidas: {contarDruidas(partida)}", True, (255, 255, 0))
        druida_coste_text = get_font(15).render(f'Coste: {formatear_numero(druida.coste)} de \n madera y magia',True,(255,255,0))
        druida_surface = pygame.image.load('graphics/icons/druida.png')

    elif partida.magia < druida.coste and partida.madera < druida.coste and contarDruidas(partida) > 0: 
        druida_coste_text = get_font(15).render(f'Coste: {formatear_numero(druida.coste)} de \n madera y magia',True,(101,101,101))
        druida_nombre_text = get_font(20).render(f"Druidas: {contarDruidas(partida)}", True, (101,101,101))
        druida_surface = pygame.image.load('graphics/icons/druida_baw.png')

    else: 
        druida_coste_text = get_font(15).render(f'Coste: ???? de \n madera y magia',True,(101,101,101))
        druida_nombre_text = get_font(20).render(f"???????", True, (101,101,101))
        druida_locked = True


    if partida.magia >= bruja.coste:
        bruja_nombre_text = get_font(20).render(f"Brujas: {contarBrujas(partida)}", True, (255, 255, 0))
        bruja_coste_text = get_font(15).render(f'Coste: {formatear_numero(bruja.coste)} de \n magia',True,(255,255,0))
        bruja_surface = pygame.image.load('graphics/icons/bruja.png')

    elif partida.magia < bruja.coste and contarBrujas(partida) > 0: 
        bruja_coste_text = get_font(15).render(f'Coste: {formatear_numero(bruja.coste)} de \n magia',True,(101,101,101))
        bruja_nombre_text = get_font(20).render(f"Brujas: {contarBrujas(partida)}", True, (101,101,101))
        bruja_surface = pygame.image.load('graphics/icons/bruja_baw.png')

    else: 
        bruja_coste_text = get_font(15).render(f'Coste: ???? de \n magia',True,(101,101,101))
        bruja_nombre_text = get_font(20).render(f"??????", True, (101,101,101))
        bruja_locked = True

    if partida.oro >= noble.coste:
        noble_nombre_text = get_font(20).render(f"Nobles: {contarNobles(partida)}", True, (255, 255, 0))
        noble_coste_text = get_font(15).render(f'Coste: {formatear_numero(noble.coste)} de \n oro',True,(255,255,0))
        noble_surface =pygame.image.load('graphics/icons/noble.png')

    elif partida.oro < noble.coste and contarNobles(partida) > 0: 
        noble_coste_text = get_font(15).render(f'Coste: {formatear_numero(noble.coste)} de \n oro',True,(101,101,101))
        noble_nombre_text = get_font(20).render(f"Nobles: {contarNobles(partida)}", True, (101,101,101))
        noble_surface =pygame.image.load('graphics/icons/noble_baw.png')

    else:
        noble_coste_text = get_font(15).render(f'Coste: ????? de \n oro',True,(101,101,101))
        noble_nombre_text = get_font(20).render(f"??????", True, (101,101,101))
        noble_locked = True

    if partida.oro >= princesa.coste:
        princesa_nombre_text = get_font(20).render(f"Princesas: {contarPrincesas(partida)}", True, (255, 255, 0))
        princesa_coste_text = get_font(15).render(f'Coste: {formatear_numero(princesa.coste)} de \n oro',True,(255,255,0))
        princesa_surface =pygame.image.load('graphics/icons/princesa.png')

    elif partida.oro < princesa.coste and contarPrincesas(partida) > 0: 
        princesa_coste_text = get_font(15).render(f'Coste: {formatear_numero(princesa.coste)} de \n oro',True,(101,101,101))
        princesa_nombre_text = get_font(20).render(f"Princesas: {contarPrincesas(partida)}", True, (101,101,101))
        princesa_surface =pygame.image.load('graphics/icons/princesa_baw.png')

    else:
        princesa_coste_text = get_font(15).render(f'Coste: ?????? de \n oro',True,(101,101,101))
        princesa_nombre_text = get_font(20).render(f"??????", True, (101,101,101))
        princesa_locked = True

    if partida.oro >= reina.coste:
        reina_nombre_text = get_font(20).render(f"Reinas: {contarReinas(partida)}", True, (255, 255, 0))
        reina_coste_text = get_font(15).render(f'Coste: {formatear_numero(reina.coste)} de \n oro',True,(255,255,0))
        reina_surface =pygame.image.load('graphics/icons/reina.png')

    elif partida.oro < reina.coste and contarReinas(partida) > 0: 
        reina_coste_text = get_font(15).render(f'Coste: {formatear_numero(reina.coste)} de \n oro',True,(101,101,101))
        reina_nombre_text = get_font(20).render(f"Reinas: {contarReinas(partida)}", True, (101,101,101))
        reina_surface =pygame.image.load('graphics/icons/reina_baw.png')

    else:
        reina_coste_text = get_font(15).render(f'Coste: ?????? de \n oro',True,(101,101,101))
        reina_nombre_text = get_font(20).render(f"??????", True, (101,101,101))
        reina_locked = True

    if partida.oro >= rey.coste:
        rey_nombre_text = get_font(20).render(f"Reyes: {contarReyes(partida)}", True, (255, 255, 0))
        rey_coste_text = get_font(15).render(f'Coste: {formatear_numero(rey.coste)} de \n oro',True,(255,255,0))
        rey_surface =pygame.image.load('graphics/icons/rey.png')

    elif partida.oro < rey.coste and contarReyes(partida) > 0: 
        rey_coste_text = get_font(15).render(f'Coste: {formatear_numero(rey.coste)} de \n oro',True,(101,101,101))
        rey_nombre_text = get_font(20).render(f"Reyes: {contarReyes(partida)}", True, (101,101,101))
        rey_surface =pygame.image.load('graphics/icons/rey_baw.png')

    else:
        rey_coste_text = get_font(15).render(f'Coste: ?????? de \n oro',True,(101,101,101))
        rey_nombre_text = get_font(20).render(f"??????", True, (101,101,101))
        rey_locked = True


    # Dibujar cada mejora con datos actualizados
    datos_mejoras = [
        (mejoras[0],contarAldeanos(partida),aldeano_surface,aldeano_nombre_text,aldeano_coste_text),
        (mejoras[1],contarLenyadores(partida),lenyador_surface,lenyador_nombre_text,lenyador_coste_text),
        (mejoras[2],contarArqueros(partida),arquero_surface,arquero_nombre_text,arquero_coste_text),
        (mejoras[3],contarPicaros(partida),picaro_surface,picaro_nombre_text,picaro_coste_text),
        (mejoras[4],contarMagos(partida),mago_surface,mago_nombre_text,mago_coste_text),
        (mejoras[5],contarBardos(partida),bardo_surface,bardo_nombre_text,bardo_coste_text),
        (mejoras[6],contarSoldados(partida),soldado_surface,soldado_nombre_text,soldado_coste_text),
        (mejoras[7],contarClerigos(partida),clerigo_surface,clerigo_nombre_text,clerigo_coste_text),
        (mejoras[8],contarDruidas(partida),druida_surface,druida_nombre_text,druida_coste_text),
        (mejoras[9],contarBrujas(partida),bruja_surface,bruja_nombre_text,bruja_coste_text),
        (mejoras[10],contarNobles(partida),noble_surface,noble_nombre_text,noble_coste_text),
        (mejoras[11],contarPrincesas(partida),princesa_surface,princesa_nombre_text,princesa_coste_text),
        (mejoras[12],contarReinas(partida),reina_surface,reina_nombre_text,reina_coste_text),
        (mejoras[13],contarReyes(partida),rey_surface,rey_nombre_text,rey_coste_text)
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




    tooltip_mejoras(aldeano_locked,lenyador_locked,arquero_locked,picaro_locked,mago_locked,bardo_locked,soldado_locked,clerigo_locked,druida_locked,bruja_locked,noble_locked,princesa_locked,reina_locked,rey_locked)

    # ...etc
def contarEventos(partida):
    numevent = sum (1 for evento in partida.eventos if isinstance(evento, Evento))
    print(numevent)

def menu_stats(partida):
    
    
    
    while True:
        fondo = pygame.image.load('graphics/background/Background.png')
        pantalla_principal_surface = pygame.image.load('graphics/icons/mazmorra.png')
        pantalla_principal_rect = pantalla_principal_surface.get_rect(topleft=(40,625))
        screen.blit(fondo,(0,0))
        screen.blit(pantalla_principal_surface,pantalla_principal_rect)
        mouse_pos = pygame.mouse.get_pos()

        

        total_oro_text = get_font(20).render(f'Oro total ganado: {partida.oro_total}',True,(255,255,0))
        gastado_oro_text = get_font(20).render(f'Oro total gastado: {partida.oro_gastado}',True,(255,255,0))
        total_madera_text = get_font(20).render(f'Madera total ganada: {partida.madera_total}',True,(28,105,21))
        gastada_madera_text = get_font(20).render(f'Madera total gastada: {partida.madera_gastada}',True,(28,105,21))
        total_magia_text = get_font(20).render(f'Magia total ganada: {partida.magia_total}',True,(223, 186, 245))
        gastada_magia_text = get_font(20).render(f'Magia total gastada: {partida.magia_gastada}',True,(223, 186, 245))
        total_mejoras_text = get_font(20).render(f'Numero de mejoras en total:{contarMejoras(partida)}',True,(255,255,255))

        screen.blit(total_oro_text,(100,100))
        screen.blit(gastado_oro_text,(100,130))
        screen.blit(total_madera_text,(100,200))
        screen.blit(gastada_madera_text,(100,230))
        screen.blit(total_magia_text,(100,300))
        screen.blit(gastada_magia_text,(100,330))
        screen.blit(total_mejoras_text,(100,400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                if pantalla_principal_rect.collidepoint(mouse_pos):
                    
                    jugar_partida(partida)

        
        pygame.display.update()
        fps.tick(60)

menu_principal()