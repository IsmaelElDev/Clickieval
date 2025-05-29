from servicios.database import SessionLocal
from entidades.partida import Partida
from sqlalchemy.orm import joinedload

def conectar_db():
    session = SessionLocal()
    return session

def cerrar_db(session):
    session.close()

def guardar_partida(partida):
    """
    Guarda una partida en la base de datos.
    
    Args:
        partida (Partida): La partida a guardar
        
    Returns:
        Partida: La partida actualizada y conectada a la sesión
    """
    session = conectar_db()
    try:
        if partida.id is not None:
            # Si la partida existe se sobreescribe
            session.merge(partida)
        else:
            session.add(partida)
            
        session.commit()
        
        # Si existe se traen todos sus datos y se devuelve
        if partida.id is not None:
            fresh_partida = session.query(Partida).options(
                joinedload(Partida.mejoras),joinedload(Partida.eventos)
            ).filter(Partida.id == partida.id).first()
            return fresh_partida
        else:
            # Si no existe se recarga y se devuelve
            session.refresh(partida)
            return partida
    except Exception as e:
        session.rollback()
        print(f"Error guardando partida: {e}")
        return partida
    finally:
        cerrar_db(session)

def buscar_partidas():
    session = conectar_db()
    try:
        partidas = session.query(Partida).all()
        print(partidas)
        return partidas
    finally:
        cerrar_db(session)

def cargar_partida(partida_id):
    session = SessionLocal()
    try:
        partida = session.query(Partida).options(
            joinedload(Partida.mejoras), joinedload(Partida.eventos)
        ).filter(Partida.id == partida_id).first()
                
        return partida
    finally:
        cerrar_db(session)

