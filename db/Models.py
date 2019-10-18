# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, String, TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(INTEGER(11), primary_key=True)
    Category_Name = Column(String(45), nullable=False)
    Category_Creation = Column(TIMESTAMP, nullable=False)
    Category_User_Creator = Column(String(45), nullable=False)


class DatosContacto(Base):
    __tablename__ = 'datos_contacto'

    usuario_idusuario = Column(INTEGER(11), primary_key=True, nullable=False)
    id = Column(INTEGER(11), primary_key=True, nullable=False, unique=True)
    country = Column(String(40), nullable=False)
    City = Column(String(45), nullable=False)
    Celphone = Column(String(45), nullable=False)
    State_Comuna = Column('State/Comuna', String(45), nullable=False)


class Historial(Base):
    __tablename__ = 'historial'

    id = Column(INTEGER(11), primary_key=True)
    Request_Id = Column(INTEGER(11), nullable=False)
    User = Column(String(45), nullable=False)
    Category = Column(String(45), nullable=False)
    Description = Column(String(150), nullable=False)
    Price = Column(INTEGER(11), nullable=False)
    User_Solicitude = Column(String(45), nullable=False)


class MuroTarea(Base):
    __tablename__ = 'muro_tareas'

    id = Column(INTEGER(11), primary_key=True, nullable=False)
    Request_Name = Column(String(45), nullable=False)
    Request_Description = Column(String(45), nullable=False)
    Request_Category = Column(String(45), nullable=False)
    Name_Solicitud = Column(String(45), nullable=False)
    Description_Solicitud = Column(String(150), nullable=False)
    Price = Column(Float, nullable=False)
    Historial_id = Column(INTEGER(11), primary_key=True, nullable=False)


class Role(Base):
    __tablename__ = 'roles'

    id = Column(INTEGER(11), primary_key=True)
    Usuario = Column(String(45), nullable=False)
    Tipo = Column(String(45), nullable=False)
    usuario_idusuario = Column(INTEGER(11), nullable=False)


class Sesion(Base):
    __tablename__ = 'sesions'

    Id = Column(INTEGER(11), primary_key=True, unique=True)
    User = Column(String(45), nullable=False)
    Rol = Column(String(45), nullable=False)
    Sesion_start = Column(TIMESTAMP, nullable=False)
    Sesion_close = Column(DateTime, nullable=False)
    usuario_id = Column(INTEGER(11), nullable=False)


class SolicitudTarea(Base):
    __tablename__ = 'solicitud_tarea'

    id = Column(INTEGER(11), primary_key=True, nullable=False)
    User_Name = Column(String(45), nullable=False)
    User_Id = Column(INTEGER(11), nullable=False)
    User_Description = Column(String(150), nullable=False)
    User_Price = Column(Float, nullable=False)
    Status = Column(String(45), nullable=False)
    Muro_Tareas_id = Column(INTEGER(11), primary_key=True, nullable=False)


class Tarea(Base):
    __tablename__ = 'tarea'

    id = Column(INTEGER(11), primary_key=True, nullable=False)
    Categories_id = Column(INTEGER(11), primary_key=True, nullable=False)
    User = Column(String(45), nullable=False)
    Description = Column(String(150), nullable=False)
    Date = Column(Date, nullable=False)
    Time = Column(TIMESTAMP, nullable=False)
    Price = Column(Float, nullable=False)
    Categoria = Column(String(15), nullable=False)
    Status = Column(String(10), nullable=False)
    usuario_id = Column(INTEGER(11), nullable=False)
    Muro_Tareas_id = Column(INTEGER(11), primary_key=True, nullable=False)
    Muro_Tareas_Historial_id = Column(INTEGER(11), primary_key=True, nullable=False)


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(INTEGER(11), primary_key=True)
    First_Name = Column(String(45), nullable=False)
    Last_Name = Column(String(45), nullable=False)
    BirthDate = Column(Date, nullable=False)
    Rut = Column(INTEGER(11), nullable=False)
    DV = Column(String(45), nullable=False)
    username = Column(String(45), nullable=False)
    ImagePerfil = Column(String(100), nullable=False)
    mail = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    creation_date = Column(DateTime, nullable=False)
    Estado = Column(String(45), nullable=False)
