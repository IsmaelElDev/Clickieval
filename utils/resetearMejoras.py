def resetear_mejoras(aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey):
    mejoras = [aldeano,lenyador,arquero,picaro,mago,bardo,soldado,clerigo,druida,bruja,noble,princesa,reina,rey]
    for m in mejoras:
        m.produccion = m.produccion_base
        
