from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Enum, Text, desc
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import json

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

class Foto(Base):
    __tablename__ = "foto"
    __table_args__ = {'schema': 'tarea2'}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    actividad_id = Column(Integer, ForeignKey('tarea2.aviso_adopcion.id'), nullable=False)

    aviso_adopcion = relationship("Aviso_Adopcion", back_populates="foto")

class Contactar_Por(Base):
    __tablename__ = "contactar_por"
    __table_args__ = {'schema': 'tarea2'}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(Enum('whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra'), nullable=False)
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(Integer, ForeignKey('tarea2.aviso_adopcion.id'), nullable=False)

    aviso_adopcion = relationship("Aviso_Adopcion", back_populates="contactar_por")


print(Base.metadata.tables.keys())

# --- Database Functions ---

def get_avisos(page_size):
    session = SessionLocal()
    avisos = session.query(Aviso_Adopcion).order_by(desc(Aviso_Adopcion.fecha_ingreso)).limit(page_size).all()
    session.close()
    return avisos

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
    confesiones = session.query(Comuna).filter_by(id=id).first()
    session.close()
    return confesiones

def get_foto_by_actv_id(id):
    session = SessionLocal()
    confesiones = session.query(Foto).filter_by(id=id).first()
    session.close()
    return confesiones



        
    





