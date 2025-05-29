from utils.contarMejoras import contarMejoras
def actualizar_bardos(partida,aldeano,lenyador,bardo):  
    if contarMejoras.contarBardos(partida)!=0:
        aldeano.produccion *= contarMejoras.contarBardos(partida)*bardo.produccion
        lenyador.produccion *= contarMejoras.contarBardos(partida)*bardo.produccion
    else: 
        aldeano.produccion = aldeano.produccion_base 
        lenyador.produccion = lenyador.produccion_base

def actualizar_druidas(partida,mago,clerigo,druida):  
    if contarMejoras.contarDruidas(partida)!=0:
        mago.produccion *= contarMejoras.contarMagos(partida)*druida.produccion
        clerigo.produccion *= contarMejoras.contarClerigos(partida)*druida.produccion
    else: 
        mago.produccion = mago.produccion_base 
        clerigo.produccion = clerigo.produccion_base
