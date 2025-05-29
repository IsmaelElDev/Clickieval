from entidades.aldeano import Aldeano
from entidades.leñador import Lenyador
from entidades.arquero import Arquero
from entidades.picaro import Picaro
from entidades.mago import Mago
from entidades.bardo import Bardo
from entidades.soldado import Soldado
from entidades.clerigo import Clerigo
from entidades.druida import Druida
from entidades.bruja import Bruja
from entidades.noble import Noble
from entidades.princesa import Princesa
from entidades.reina import Reina
from entidades.rey import Rey
from utils.contarMejoras import contarMejoras
from utils.actualizarProducciones import actualizar_producciones

class comprarMejoras:
    
    def comprar_aldeano(partida,aldeano):
        # Guardar el coste actual antes de comprar
        current_cost = aldeano.coste
        current_production = aldeano.produccion
        current_production_base = aldeano.produccion_base
        current_inc_precio = aldeano.incPrecio
        
            
        # Actualizar variables del juego
        partida.oro -= current_cost
        partida.oro_por_segundo += current_production

        partida.oro_gastado += current_cost
            
        # Nueva instancia de aldeano para añadir a la lista 
        new_aldeano = Aldeano('Aldeano', current_cost,current_production_base,current_production, current_inc_precio)
        new_aldeano.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_aldeano)  # Añadir a la lista
            
        print(f"Aldeanos: {contarMejoras.contarAldeanos(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {aldeano.coste}")

        # Actualizar el precio para la próxima compra
        aldeano.actualizarPrecio()

    def comprar_lenyador(partida,lenyador):
        # Guardar el coste actual antes de comprar
        current_cost = lenyador.coste
        current_production = lenyador.produccion
        current_production_base = lenyador.produccion_base
        current_inc_precio = lenyador.incPrecio
            
        # Actualizar variables del juego
        partida.oro -= current_cost
        partida.madera_por_segundo += current_production

        partida.oro_gastado += current_cost
            
        # Nueva instancia de lenyador para añadir a la lista 
        new_lenyador = Lenyador('Lenyador', current_cost,current_production_base,current_production, current_inc_precio)
        new_lenyador.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_lenyador)  # Añadir a la lista
            
        print(f"Lenyadores: {contarMejoras.contarLenyadores(partida)}, Madera por segundo: {partida.madera_por_segundo}, Coste: {lenyador.coste}")

        # Actualizar el precio para la próxima compra
        lenyador.actualizarPrecio()

    def comprar_arquero(partida,arquero):
        # Guardar el coste actual antes de comprar
        current_cost = arquero.coste
        current_production = arquero.produccion
        current_production_base = arquero.produccion_base
        current_inc_precio = arquero.incPrecio
            
        # Actualizar variables del juego
        partida.oro -= current_cost
        partida.madera -= current_cost
        partida.oro_por_segundo += current_production
        partida.oro_por_click += current_production

        partida.oro_gastado += current_cost
        partida.madera_gastada += current_cost
            
        # Nueva instancia de arquero para añadir a la lista 
        new_arquero = Arquero('Arquero', current_cost, current_production_base,current_production, current_inc_precio)
        new_arquero.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_arquero)  # Añadir a la lista
            
        print(f"Arqueros: {contarMejoras.contarArqueros(partida)}, Oro por segundo: {partida.oro_por_segundo}, Oro por click:{partida.oro_por_click}, Coste: {arquero.coste}")

        # Actualizar el precio para la próxima compra
        arquero.actualizarPrecio()

    def comprar_picaro(partida,picaro):
        # Guardar el coste actual antes de comprar
        current_cost = picaro.coste
        current_produccion = picaro.produccion
        current_production_base = picaro.produccion_base
        current_inc_precio = picaro.incPrecio
        current_min_produccion = picaro.min_produccion
        current_max_produccion = picaro.max_produccion
            
        # Actualizar variables del juego
        partida.oro -= current_cost

        partida.oro_gastado += current_cost
            
        # Nueva instancia de picaro para añadir a la lista 
        new_picaro = Picaro('Picaro', current_cost, current_min_produccion,current_max_produccion,current_production_base,current_produccion, current_inc_precio)
        new_picaro.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_picaro)  # Añadir a la lista
            
        print(f"Picaros: {contarMejoras.contarPicaros(partida)}, Coste: {picaro.coste}, Produccion: {picaro.produccion}")

        # Actualizar el precio para la próxima compra
        picaro.actualizarPrecio()

    def comprar_mago(partida,mago):
        # Guardar el coste actual antes de comprar
        current_cost = mago.coste
        current_production = mago.produccion
        current_production_base = mago.produccion_base
        current_inc_precio = mago.incPrecio
            
        # Actualizar variables del juego
        partida.oro -= current_cost
        partida.magia_por_segundo += current_production

        partida.oro_gastado += current_cost
            
        # Nueva instancia de mago para añadir a la lista 
        new_mago = Mago('Mago', current_cost,current_production_base, current_production, current_inc_precio)
        new_mago.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_mago)  # Añadir a la lista
            
        print(f"Magos: {contarMejoras.contarMagos(partida)}, Magia por segundo: {partida.magia_por_segundo}, Coste: {mago.coste}")

        # Actualizar el precio para la próxima compra
        mago.actualizarPrecio()

    def comprar_bardo(partida,aldeano,lenyador,bardo):
        # Guardar el coste actual antes de comprar
        current_cost = bardo.coste
        current_production = bardo.produccion
        current_production_base = bardo.produccion_base
        current_inc_precio = bardo.incPrecio
            
        # Actualizar variables del juego
        partida.oro -= current_cost
        partida.magia -= current_cost

        partida.oro_gastado += current_cost
        partida.magia_gastada += current_cost


        # Nueva instancia de bardo para añadir a la lista 
        new_bardo = Bardo('Bardo', current_cost,current_production_base, current_production, current_inc_precio)
        new_bardo.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_bardo)  # Añadir a la lista
        actualizar_producciones(partida)

        if contarMejoras.contarBardos(partida)!=0:
            aldeano.produccion *= bardo.produccion
            lenyador.produccion *= bardo.produccion

        # Actualizar el precio para la próxima compra
        bardo.actualizarPrecio()

    def comprar_soldado(partida,soldado):
        # Guardar el coste actual antes de comprar
        current_cost = soldado.coste
        current_production = soldado.produccion
        current_production_base = soldado.produccion_base
        current_inc_precio = soldado.incPrecio
            
        # Actualizar variables del juego
        partida.oro -= current_cost
        partida.oro_por_click += current_production

        partida.oro_gastado += current_cost
            
        # Nueva instancia de soldado para añadir a la lista 
        new_soldado = Soldado('Soldado', current_cost,current_production_base, current_production, current_inc_precio)
        new_soldado.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_soldado)  # Añadir a la lista
            
        print(f"Soldados: {contarMejoras.contarSoldados(partida)}, Oro por click:{partida.oro_por_click}, Coste: {soldado.coste}")

        # Actualizar el precio para la próxima compra
        soldado.actualizarPrecio()

    def comprar_clerigo(partida,clerigo):
        # Guardar el coste actual antes de comprar
        current_cost = clerigo.coste
        current_production = clerigo.produccion
        current_production_base = clerigo.produccion_base
        current_inc_precio = clerigo.incPrecio
            
        # Actualizar variables del juego
        partida.magia -= current_cost
        partida.magia_por_segundo += current_production

        partida.magia_gastada += current_cost
            
        # Nueva instancia de clerigo para añadir a la lista 
        new_clerigo = Clerigo('Clerigo', current_cost,current_production_base, current_production, current_inc_precio)
        new_clerigo.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_clerigo)  # Añadir a la lista
            
        print(f"Clerigos: {contarMejoras.contarClerigos(partida)}, Oro por segundo:{partida.magia_por_segundo}, Coste: {clerigo.coste}")

        # Actualizar el precio para la próxima compra
        clerigo.actualizarPrecio()

    def comprar_druida(partida,mago,clerigo,druida):
        # Guardar el coste actual antes de comprar
        current_cost = druida.coste
        current_production = druida.produccion
        current_production_base = druida.produccion_base
        current_inc_precio = druida.incPrecio
            
        # Actualizar variables del juego
        partida.madera -= current_cost
        partida.magia -= current_cost

        partida.madera_gastada += current_cost
        partida.magia_gastada += current_cost

        # Nueva instancia de druida para añadir a la lista 
        new_druida = Druida('Druida', current_cost,current_production_base, current_production, current_inc_precio)
        new_druida.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_druida)  # Añadir a la lista
        actualizar_producciones(partida)

        if contarMejoras.contarDruidas(partida)!=0:
            mago.produccion *= druida.produccion
            clerigo.produccion *= druida.produccion
        # Actualizar el precio para la próxima compra
        druida.actualizarPrecio()

    def comprar_bruja(partida,bruja):
        # Guardar el coste actual antes de comprar
        current_cost = bruja.coste
        current_production = bruja.produccion
        current_production_base = bruja.produccion_base
        current_inc_precio = bruja.incPrecio
            
        # Actualizar variables del juego
        partida.magia -= current_cost
        partida.oro_por_segundo += current_production

        partida.magia_gastada += current_cost

            
        # Nueva instancia de bruja para añadir a la lista 
        new_bruja = Bruja('Bruja', current_cost,current_production_base, current_production, current_inc_precio)
        new_bruja.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_bruja)  # Añadir a la lista
            
        print(f"Brujas: {contarMejoras.contarBrujas(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {bruja.coste}")

        # Actualizar el precio para la próxima compra
        bruja.actualizarPrecio()

    def comprar_noble(partida,noble):
        # Guardar el coste actual antes de comprar
        current_cost = noble.coste
        current_production = noble.produccion
        current_production_base = noble.produccion_base
        current_inc_precio = noble.incPrecio
            
        # Actualizar variables del juego
        partida.oro -= current_cost
        partida.oro_por_segundo += current_production

        partida.oro_gastado += current_cost
            
        # Nueva instancia de noble para añadir a la lista 
        new_noble = Noble('Noble', current_cost,current_production_base, current_production, current_inc_precio)
        new_noble.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_noble)  # Añadir a la lista
            
        print(f"Nobles: {contarMejoras.contarNobles(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {noble.coste}")

        # Actualizar el precio para la próxima compra
        noble.actualizarPrecio()

    def comprar_princesa(partida,princesa):
        # Guardar el coste actual antes de comprar
        current_cost = princesa.coste
        current_production = princesa.produccion
        current_production_base = princesa.produccion_base
        current_inc_precio = princesa.incPrecio
            
        # Actualizar variables del juego
        partida.oro -= current_cost
        partida.oro_por_click += current_production

        partida.oro_gastado += current_cost
            
        # Nueva instancia de princesa para añadir a la lista 
        new_princesa = Princesa('Princesa', current_cost,current_production_base,current_production, current_inc_precio)
        new_princesa.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_princesa)  # Añadir a la lista
            
        print(f"Princesas: {contarMejoras.contarPrincesas(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {princesa.coste}")

        # Actualizar el precio para la próxima compra
        princesa.actualizarPrecio()

    def comprar_reina(partida,reina):
        # Guardar el coste actual antes de comprar
        current_cost = reina.coste
        current_production = reina.produccion
        current_production_base = reina.produccion_base
        current_inc_precio = reina.incPrecio
            
        # Actualizar variables del juego
        partida.oro -= current_cost
        partida.oro_por_segundo += current_production

        partida.oro_gastado += current_cost
            
        # Nueva instancia de reina para añadir a la lista 
        new_reina = Reina('Reina', current_cost,current_production_base, current_production, current_inc_precio)
        new_reina.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_reina)  # Añadir a la lista
            
        print(f"Reinas: {contarMejoras.contarReinas(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {reina.coste}")

        # Actualizar el precio para la próxima compra
        reina.actualizarPrecio()

    def comprar_rey(partida,aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey):
        # Guardar el coste actual antes de comprar
        current_cost = rey.coste
        current_production = rey.produccion
        current_production_base = rey.produccion_base
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
        new_rey = Rey('Rey', current_cost,current_production_base, current_production, current_inc_precio)
        new_rey.partida = partida  # Establecer relacion para la bd
        partida.mejoras.append(new_rey)  # Añadir a la lista
        actualizar_producciones(partida)

        print(f"Reyes: {contarMejoras.contarReyes(partida)}, Oro por segundo: {partida.oro_por_segundo}, Coste: {rey.coste}")

        # Actualizar el precio para la próxima compra
        rey.actualizarPrecio()