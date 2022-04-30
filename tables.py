from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


couriers_regions = Table(
    "couriers_regions", Base.metadata,
    Column("courier_id", ForeignKey("couriers.id")),
    Column("region_id", ForeignKey("regions.id"))
)


class Courier(Base):
    __tablename__ = "couriers"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    courier_type = Column(String)
    regions = relationship("Region", secondary=couriers_regions, back_populates="couriers")
    orders = relationship("Order", back_populates="courier")


class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, unique=True)
    region = Column(Integer, nullable=False, unique=True)
    couriers = relationship("Courier", secondary=couriers_regions, back_populates="regions")
    orders = relationship("Order", back_populates="region")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    weight = Column(Integer)
    courier = relationship("Courier", back_populates="orders")
    region = relationship("Region", back_populates="orders")
