from utils.contarMejoras import contarMejoras
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

class recuperarCostes:
    
    @staticmethod
    def recuperar_costes_aldeanos(aldeano, partida):
    
        max_coste = aldeano.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Aldeano) and mejora.coste > max_coste:
                max_coste = mejora.coste
        aldeano.coste = max_coste
        if(contarMejoras.contarAldeanos(partida) !=0):
            aldeano.actualizarPrecio()  

    @staticmethod
    def recuperar_costes_lenyadores(lenyador,partida):

        max_coste = lenyador.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Lenyador) and mejora.coste > max_coste:
                max_coste = mejora.coste
        lenyador.coste = max_coste
        if(contarMejoras.contarLenyadores(partida) !=0):
            lenyador.actualizarPrecio()  
        
    @staticmethod
    def recuperar_costes_arqueros(arquero,partida):

        max_coste = arquero.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Arquero) and mejora.coste > max_coste:
                max_coste = mejora.coste
        arquero.coste = max_coste
        if(contarMejoras.contarArqueros(partida) !=0):
            arquero.actualizarPrecio() 
    
    @staticmethod
    def recuperar_costes_picaros(picaro,partida):

        max_coste = picaro.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Picaro) and mejora.coste > max_coste:
                max_coste = mejora.coste
        picaro.coste = max_coste
        if(contarMejoras.contarPicaros(partida) !=0):
            picaro.actualizarPrecio()  
    
    @staticmethod
    def recuperar_costes_magos(mago,partida):

        max_coste = mago.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Mago) and mejora.coste > max_coste:
                max_coste = mejora.coste
        mago.coste = max_coste
        if(contarMejoras.contarMagos(partida) !=0):
            mago.actualizarPrecio()  
    
    @staticmethod
    def recuperar_costes_bardos(bardo, partida):
        
        max_coste = bardo.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Bardo) and mejora.coste > max_coste:
                max_coste = mejora.coste
        bardo.coste = max_coste
        if(contarMejoras.contarBardos(partida) !=0):
            bardo.actualizarPrecio() 

    @staticmethod
    def recuperar_costes_soldados(soldado,partida):

        max_coste = soldado.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Soldado) and mejora.coste > max_coste:
                max_coste = mejora.coste
        soldado.coste = max_coste
        if(contarMejoras.contarSoldados(partida) !=0):
            soldado.actualizarPrecio()   

    @staticmethod
    def recuperar_costes_clerigos(clerigo,partida):

        max_coste = clerigo.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Clerigo) and mejora.coste > max_coste:
                max_coste = mejora.coste
        clerigo.coste = max_coste
        if(contarMejoras.contarClerigos(partida) !=0):
            clerigo.actualizarPrecio()   

    @staticmethod
    def recuperar_costes_druidas(druida,partida):

        max_coste = druida.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Druida) and mejora.coste > max_coste:
                max_coste = mejora.coste
        druida.coste = max_coste
        if(contarMejoras.contarDruidas(partida) !=0):
            druida.actualizarPrecio()   

    @staticmethod
    def recuperar_costes_brujas(bruja,partida):

        max_coste = bruja.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Bruja) and mejora.coste > max_coste:
                max_coste = mejora.coste
        bruja.coste = max_coste
        if(contarMejoras.contarBrujas(partida) !=0):
            bruja.actualizarPrecio()  

    @staticmethod
    def recuperar_costes_nobles(noble,partida):

        max_coste = noble.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Noble) and mejora.coste > max_coste:
                max_coste = mejora.coste
        noble.coste = max_coste
        if(contarMejoras.contarNobles(partida) !=0):
            noble.actualizarPrecio()  

    @staticmethod
    def recuperar_costes_princesas(princesa, partida):
        
        max_coste = princesa.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Princesa) and mejora.coste > max_coste:
                max_coste = mejora.coste
        princesa.coste = max_coste
        if(contarMejoras.contarPrincesas(partida) !=0):
            princesa.actualizarPrecio()  

    @staticmethod
    def recuperar_costes_reinas(reina, partida):
        
        max_coste = reina.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Reina) and mejora.coste > max_coste:
                max_coste = mejora.coste
        reina.coste = max_coste
        if(contarMejoras.contarReinas(partida) !=0):
            reina.actualizarPrecio()  

    @staticmethod
    def recuperar_costes_reyes(rey, partida):
        
        max_coste = rey.coste
        for mejora in partida.mejoras:
            if isinstance(mejora, Rey) and mejora.coste > max_coste:
                max_coste = mejora.coste
        rey.coste = max_coste
        if(contarMejoras.contarReyes(partida) !=0):
            rey.actualizarPrecio()  

    @staticmethod
    def recuperar_multiplicadores_bardos(aldeano,lenyador,bardo,partida):

        bardos = contarMejoras.contarBardos(partida)
        prod_bardo = bardo.produccion
        multiplicador = prod_bardo**bardos

        print(contarMejoras.contarBardos(partida))
        aldeano.produccion *= multiplicador
        print(aldeano.produccion)
        lenyador.produccion *= multiplicador
        print(lenyador.produccion)
        #partida.oro_por_segundo = aldeano.produccion
        #partida.madera_por_segundo = lenyador.produccion

    @staticmethod
    def recuperar_multiplicadores_reyes(aldeano,lenyador,arquero,picaro,bardo,mago,soldado,clerigo,druida,bruja,noble,princesa,reina,rey,partida):

        reyes = contarMejoras.contarReyes(partida)
        prod_rey = rey.produccion
        multiplicador = prod_rey**reyes

        
        aldeano.produccion *= multiplicador
        lenyador.produccion *= multiplicador
        arquero.produccion *= multiplicador
        picaro.produccion *= multiplicador
        bardo.produccion *= multiplicador
        mago.produccion *= multiplicador
        soldado.produccion *= multiplicador
        clerigo.produccion *= multiplicador
        druida.produccion *= multiplicador
        bruja.produccion *= multiplicador
        noble.produccion *= multiplicador
        princesa.produccion *= multiplicador
        reina.produccion *= multiplicador

        #partida.oro_por_segundo = aldeano.produccion
        #partida.madera_por_segundo = lenyador.produccion