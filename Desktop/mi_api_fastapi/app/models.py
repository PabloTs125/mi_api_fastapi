from sqlalchemy import Column, Integer, String
from .database import Base

class Nombre(Base):
    __tablename__ = "0_nombre"  # Nombre exacto de la tabla

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    apellido = Column(String(50))