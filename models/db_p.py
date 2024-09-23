from sqlalchemy import TIMESTAMP, Integer, String, Table, Column, text, true, ForeignKey
from sqlalchemy.orm import relationship
from config.db import meta, engine, Base


class Model_Auto(Base):
    __tablename__ = "Autos_models"
    id = Column(Integer, primary_key=True)
    modelo = Column(String(255), nullable=False)


class Category(Base):
    __tablename__ = "categorys"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Vehiculos(Base):
    __tablename__ = "vehiculos"
    id = Column(Integer, primary_key=True)
    name_product = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categorys.id", ondelete="CASCADE"), nullable=False)
    modelo_id = Column(Integer, ForeignKey("Autos_models.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
