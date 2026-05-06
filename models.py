from database import Base
from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from uuid import uuid4
class Category (Base):
    __tablename__='categories'
    id = Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    name= Column (String(100))
    description=Column(Text)
    wines=relationship("Wine",back_populates="category")
class Producers (Base):
    __tablename__='producers'
    id =Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    name=Column(String(100)) #El vino con el nombre más grande son 85 letras
    country=Column(String(50)) #El país con el nombre más largo y produce vino tiene 48 letras
    region=Column(String(100)) #La región con el nombre más largo contiene 85 letras
    wines = relationship("Wine", back_populates="producer")
    notes=Column(Text) 
    created_at=Column(DateTime, default=lambda:datetime.now(UTC))
class Vendors (Base):
    __tablename__='vendors'
    id =Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    name=Column(String(100)) #El vino con el nombre más grande son 85 letras
    contact=Column(String(100))
    email=Column(String(100))
    phone=Column(String(20))
    country=Column(String(50))
    notes=Column(Text)
    created_at=Column(DateTime, default=lambda:datetime.now(UTC))
    wines=relationship("Wine", back_populates="vendor")
class Cellar_zones (Base):
    __tablename__='cellar_zones'
    id=Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    name=Column(String(100))
    temp_target=Column(Integer)
    humidity_target=Column(Integer)
    temp_current=Column(Integer)
    humidity_current=Column(Integer)
    created_at=Column(DateTime, default=lambda:datetime.now(UTC))
    wines=relationship("Wine", back_populates="zone")
class Wine (Base):
    __tablename__='wines'
    id=Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    producer_id=Column(UUID(as_uuid=True),ForeignKey('producers.id'))
    category_id=Column(UUID(as_uuid=True),ForeignKey('categories.id'))
    vendor_id=Column(UUID(as_uuid=True),ForeignKey('vendors.id'))
    zone_id=Column(UUID(as_uuid=True),ForeignKey('cellar_zones.id'))
    name=Column(String(100))
    category=relationship("Category",back_populates="wines")
    appellation=Column(String(100))
    vintage=Column(Integer)
    varietal=Column(String(100))
    type=Column(String(100))
    producer = relationship("Producers", back_populates="wines")
    vendor = relationship("Vendors", back_populates="wines")
    zone = relationship("Cellar_zones", back_populates="wines")
    stock=Column(Integer)
    price=Column(Numeric)
    bin_location=Column(String(50))
    tasting_notes=Column(Text)
    created_at=Column(DateTime, default=lambda:datetime.now(UTC))
    movements = relationship("Movements", back_populates="wine")
class Users (Base):
    __tablename__="users"
    id=Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    email=Column(String(100))
    password_hash=Column(Text) #Para que le puedan meter una contraseña segura
    role=Column(Integer)
    clearance_level=Column(Integer)
    created_at=Column(DateTime, default=lambda:datetime.now(UTC))
    movements = relationship("Movements", back_populates="user")
class Movements (Base):
    __tablename__="movements"
    id=Column(UUID(as_uuid=True),primary_key=True, default=uuid4)
    wines_id=Column(UUID(as_uuid=True),ForeignKey('wines.id'))
    users_id=Column(UUID(as_uuid=True),ForeignKey('users.id'))
    type=Column(String(100))
    quantity=Column(Integer)    
    reason=Column(Text)
    created_at=Column(DateTime, default=lambda:datetime.now(UTC))    
    wine= relationship("Wine", back_populates="movements")
    users=relationship("Users",back_populates="movements")
