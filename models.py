from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    age = Column(Integer, nullable=False)

    jasmine_rice_sales = relationship("JasmineRiceSale", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"LottoTransaction (id={self.id}, first_name={self.first_name}, " \
               f"last_name={self.last_name}, gender={self.gender}, age={self.age})"


class JasmineRiceSale(Base):
    __tablename__ = "jasmine_rice_sale"

    id = Column(Integer, primary_key=True)
    weight_kg = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    time = Column(Text, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    customer = relationship("Customers", back_populates="jasmine_rice_sales")

    def __repr__(self):
        return f"JasmineRiceSale (id={self.id}, weight_kg={self.weight_kg}, " \
               f"cost={self.cost}, time={self.time}, customer_id={self.customer_id})"
