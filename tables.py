from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


couriers_regions = Table(
    "couriers_regions", Base.metadata,
    Column("courier_id", ForeignKey("couriers.id")),
    Column("region_id", ForeignKey("regions.id"))
)


orders_hours = Table(
    "orders_hours", Base.metadata,
    Column("order_id", ForeignKey("orders.id")),
    Column("hour_id", ForeignKey("hours.id"))
)


couriers_hours = Table(
    "couriers_hours", Base.metadata,
    Column("courier_id", ForeignKey("couriers.id")),
    Column("hour_id", ForeignKey("hours.id"))
)


class Courier(Base):
    __tablename__ = "couriers"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    courier_type = Column(String)

    regions = relationship("Region", secondary=couriers_regions, back_populates="couriers")
    working_hours = relationship("Hour", secondary=couriers_hours, back_populates="couriers")
    orders = relationship("Order", back_populates="courier")


class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    region = Column(Integer, nullable=False, unique=True)

    couriers = relationship("Courier", secondary=couriers_regions, back_populates="regions")
    orders = relationship("Order", back_populates="region")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=False)
    weight = Column(Integer)
    assign_time = Column(DateTime)
    complete_time = Column(DateTime)
    courier_id = Column(Integer, ForeignKey("couriers.id"))
    region_id = Column(Integer, ForeignKey("regions.id"))

    courier = relationship("Courier", back_populates="orders")
    region = relationship("Region", back_populates="orders")
    delivery_hours = relationship("Hour", secondary=orders_hours, back_populates="orders")


class Hour(Base):
    __tablename__ = "hours"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    hour = Column(String, unique=True)

    couriers = relationship("Courier", secondary=couriers_hours, back_populates="working_hours")
    orders = relationship("Order", secondary=orders_hours, back_populates="delivery_hours")
