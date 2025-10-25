from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Enum, Text, desc, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import json
from datetime import datetime

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# --- Models ---

class Region(Base):
    __tablename__ = 'region'
    __table_args__ = {'schema': 'tarea2'}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(200), nullable=False)

    comuna=relationship("Comuna", back_populates="region")

class Comuna(Base):
    __tablename__ = 'comuna'
    __table_args__ = {'schema': 'tarea2'}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(200), nullable=False)
    region_id = Column(Integer, ForeignKey('tarea2.region.id'), nullable=False)

    region = relationship("Region", back_populates="comuna")
    aviso_adopcion = relationship("Aviso_Adopcion", back_populates="comuna")


class Aviso_Adopcion(Base):
    __tablename__ = "aviso_adopcion"
    __table_args__ = {'schema': 'tarea2'}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fecha_ingreso = Column(DateTime, nullable=False)
    comuna_id = Column(Integer, ForeignKey('tarea2.comuna.id'), nullable=False)
    sector = Column(String(100), nullable=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=True)
    tipo = Column(Enum('gato', 'perro'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    edad = Column(Integer, nullable=False)
    unidad_medida = Column(Enum('a', 'm'), nullable=False)
    fecha_entrega = Column(DateTime, nullable=False)
    descripcion = Column(Text, nullable=True)

    comuna = relationship("Comuna", back_populates="aviso_adopcion")
    foto = relationship("Foto", back_populates="aviso_adopcion")
    contactar_por = relationship("Contactar_Por", back_populates="aviso_adopcion")
    comentario = relationship("Comentario", back_populates="aviso_adopcion")

class Foto(Base):
    __tablename__ = "foto"
    __table_args__ = {'schema': 'tarea2'}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    aviso_id = Column(Integer, ForeignKey('tarea2.aviso_adopcion.id'), nullable=False)

    aviso_adopcion = relationship("Aviso_Adopcion", back_populates="foto")


class Contactar_Por(Base):
    __tablename__ = "contactar_por"
    __table_args__ = {'schema': 'tarea2'}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra'), nullable=False)
    identificador = Column(String(150), nullable=False)
    aviso_id = Column(Integer, ForeignKey('tarea2.aviso_adopcion.id'), nullable=False)

    aviso_adopcion = relationship("Aviso_Adopcion", back_populates="contactar_por")

class Comentario(Base):
    __tablename__ = "comentario"
    __table_args__ = {'schema': 'tarea2'}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(80), nullable=False)
    texto = Column(String(300), nullable=False)
    fecha = Column(DateTime, nullable=False)
    aviso_id = Column(Integer, ForeignKey('tarea2.aviso_adopcion.id'), nullable=False)

    aviso_adopcion = relationship("Aviso_Adopcion", back_populates="comentario")

    


# --- Database Functions ---

def get_avisos(page=1, page_size=5):
    session = SessionLocal()
    offset = (page - 1)*page_size
    avisos = session.query(Aviso_Adopcion).order_by(desc(Aviso_Adopcion.fecha_ingreso)).offset(offset).limit(page_size).all()
    session.close()
    return avisos

def count_avisos():
    session = SessionLocal()
    total = session.query(Aviso_Adopcion).count()
    session.close()
    return total

def get_comunas():
    session = SessionLocal()
    comunas = session.query(Comuna).all()
    session.close()
    return comunas

def get_regiones():
    session = SessionLocal()
    regiones = session.query(Region).all()
    session.close()
    return regiones

def get_comuna_by_id(id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=id).first()
    session.close()
    return comuna

def get_region_by_id(id):
    session = SessionLocal()
    region = session.query(Region).filter_by(id=id).first()
    session.close()
    return region

def get_foto_by_aviso_id(id):
    session = SessionLocal()
    confesiones = session.query(Foto).filter_by(id=id).first()
    session.close()
    return confesiones

def get_contacto_by_aviso_id(id):
    session = SessionLocal()
    redes_sociales = session.query(Contactar_Por).filter_by(aviso_id=id).all()
    session.close()
    return redes_sociales

def get_comentarios_by_aviso_id(id):
    session = SessionLocal()
    comentarios = session.query(Comentario).filter_by(aviso_id=id).all()
    session.close()
    return comentarios

def create_aviso(comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion):
    session = SessionLocal()
    new_aviso = Aviso_Adopcion(fecha_ingreso=datetime.now(), comuna_id=comuna_id, sector=sector, nombre=nombre, email=email, celular=celular, tipo=tipo, cantidad=cantidad, edad=edad, unidad_medida=unidad_medida, fecha_entrega=fecha_entrega, descripcion=descripcion)
    session.add(new_aviso)
    session.commit()
    id = new_aviso.id
    print(id)
    session.close()
    return id


def create_foto(ruta_archivo, nombre_archivo, aviso_id):
    session = SessionLocal()
    new_foto = Foto(ruta_archivo=ruta_archivo,nombre_archivo=nombre_archivo, aviso_id=aviso_id)
    session.add(new_foto)
    session.commit()
    session.close()



#----Database functions for Estadisticas

def get_count_avisos_por_día():
    session = SessionLocal()
    aviso_por_dia= (
        session.query(
            func.date(Aviso_Adopcion.fecha_ingreso).label("fecha"),
            func.count(Aviso_Adopcion.id).label("count")
        )
        .group_by(func.date(Aviso_Adopcion.fecha_ingreso))
        .all()
    )
    session.close()
    return [{"fecha": fecha, "count": count} for fecha, count in aviso_por_dia] 

def get_count_avisos_por_tipo():
    session = SessionLocal()
    aviso_por_tipo= (
        session.query(
            Aviso_Adopcion.tipo.label("name"),
            func.count(Aviso_Adopcion.id).label("y")
        )
        .group_by(Aviso_Adopcion.tipo)
        .all()
    )
    session.close()
    return [{"name": name, "y": y} for name, y in aviso_por_tipo]

def get_count_avisos_por_tipo_y_mes():
    session = SessionLocal()

    results = (
        session.query(
            Aviso_Adopcion.tipo.label("tipo"),
            func.month(Aviso_Adopcion.fecha_ingreso).label("mes"),
            func.count(Aviso_Adopcion.id).label("cantidad")
        )
        .group_by(Aviso_Adopcion.tipo, func.month(Aviso_Adopcion.fecha_ingreso))
        .order_by(func.month(Aviso_Adopcion.fecha_ingreso))
        .all()
    )

    session.close()

    tipos = {}

    for tipo, mes, cantidad in results:
        if tipo not in tipos:
            tipos[tipo] = [0] * 12  # 12 months
        tipos[tipo][mes - 1] = cantidad  # month index starts at 0

 

    return [{"name": tipo, "data": data} for tipo, data in tipos.items()]
    




        
    





