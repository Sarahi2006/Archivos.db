from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Estudiantes(Base):
    __tablename__ = 'tbl_estudiante'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, nullable=False, unique=True)

class Cursos(Base):
    __tablename__ = 'tbl_curso'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)

class Inscripciones(Base):
    __tablename__ = 'tbl_inscripcion'
    id = Column(Integer, primary_key=True)
    estudiante_id = Column(Integer, ForeignKey('tbl_estudiante.id'))
    curso_id = Column(Integer, ForeignKey('tbl_curso.id'))

    estudiante = relationship("Estudiantes", back_populates="inscripciones")
    curso = relationship("Cursos", back_populates="inscripciones")

Estudiantes.inscripciones = relationship("Inscripciones", back_populates="estudiante")
Cursos.inscripciones = relationship("Inscripciones", back_populates="curso")

engine = create_engine('sqlite:///univo.db', echo=True)
Base.metadata.create_all(engine)
