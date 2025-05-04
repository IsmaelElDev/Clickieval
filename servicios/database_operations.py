from servicios.database import SessionLocal
from entidades.partida import Partida
from sqlalchemy.orm import joinedload
from entidades.aldeano import Aldeano
from entidades.leñador import Lenyador
from entidades.arquero import Arquero
from entidades.picaro import Picaro
from entidades.mago import Mago
from entidades.bardo import Bardo

def conectar_db():
    db = SessionLocal()
    return db

def guardar_partida(partida):
    """
    Guarda una partida en la base de datos.
    
    Args:
        partida (Partida): La partida a guardar
        
    Returns:
        Partida: La partida actualizada y conectada a la sesión
    """
    session = SessionLocal()
    try:
        if partida.id is not None:
            # If the partida already exists in the database, merge it
            session.merge(partida)
        else:
            # Otherwise, add it as a new partida
            session.add(partida)
            
        session.commit()
        
        # Now fetch a fresh copy that's attached to the session
        if partida.id is not None:
            fresh_partida = session.query(Partida).options(
                joinedload(Partida.mejoras),joinedload(Partida.eventos)
            ).filter(Partida.id == partida.id).first()
            return fresh_partida
        else:
            # If we just added it, it should now have an ID
            session.refresh(partida)
            return partida
    except Exception as e:
        session.rollback()
        print(f"Error guardando partida: {e}")
        return partida
    finally:
        session.close()

def buscar_partidas():
    session = SessionLocal()
    try:
        partidas = session.query(Partida).all()
        print(partidas)
        return partidas
    finally:
        session.close()

def cargar_partida(partida_id):
    db = SessionLocal()
    try:
        partida = db.query(Partida).options(
            joinedload(Partida.mejoras), joinedload(Partida.eventos)
        ).filter(Partida.id == partida_id).first()

        if partida:
            # Reset production rates
            partida.oro_por_segundo = 0
            partida.madera_por_segundo = 0
            partida.magia_por_segundo = 0
            partida.oro_por_click = 1  # Base value

            # Recalculate based on loaded mejoras
            for mejora in partida.mejoras:
                
                # Update game stats based on mejora type
                if isinstance(mejora,Aldeano):
                    partida.oro_por_segundo += mejora.produccion
                elif isinstance(mejora,Lenyador):
                    partida.madera_por_segundo += mejora.produccion
                elif isinstance(mejora,Arquero):
                    partida.oro_por_segundo += mejora.produccion
                    partida.oro_por_click += mejora.produccion
                elif isinstance(mejora,Mago):
                    partida.magia_por_segundo += mejora.produccion
                elif isinstance(mejora,Bardo):
                    for bardo in partida.mejoras:
                        if isinstance(bardo,Bardo):
                            for m in partida.mejoras:
                                if isinstance(m,Aldeano) or isinstance(m,Lenyador):
                                    pass
                
                # No need to handle picaros here as they work differently
            
        return partida
    finally:
        db.close()

# Remove the refrescar_partida function as it's not needed anymore