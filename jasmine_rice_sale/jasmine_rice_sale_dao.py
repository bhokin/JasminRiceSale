from abc import ABC
from typing import List

from sqlalchemy.orm.session import Session
from models import Customers, JasmineRiceSale


class Dao(ABC):

    def __init__(self, session: Session) -> None:
        self.__session = session

    @property
    def get_session(self):
        return self.__session


class CustomersDao(Dao):
    def get_customer_by_id(self, id: int) -> Customers:
        return self.get_session.query(Customers).filter(Customers.id == id)[0]

    def get_all_customers(self) -> List[Customers]:
        return self.get_session.query(Customers).all()

    def add_customer(self, customer: Customers) -> None:
        self.get_session.add(customer)
        self.get_session.commit()

    def update_customer(self, id: int, first_name: str = None,
                        last_name: str = None, gender: str = None, age: int = None):
        customer = self.get_session.query(Customers).filter(Customers.id == id)
        if first_name is None:
            first_name = customer[0].first_name
        if last_name is None:
            last_name = customer[0].last_name
        if gender is None:
            gender = customer[0].gender
        if age is None:
            age = customer[0].age
        customer.update({Customers.first_name: first_name,
                         Customers.last_name: last_name,
                         Customers.gender: gender,
                         Customers.age: age})
        self.get_session.commit()


class JasmineRiceSaleDao(Dao):
    def get_sale_by_id(self, id: int) -> JasmineRiceSale:
        return self.get_session.query(JasmineRiceSale).filter(JasmineRiceSale.id == id)[0]

    def get_all_sale(self) -> List[JasmineRiceSale]:
        return self.get_session.query(JasmineRiceSale).all()

    def buy_jasmine_rice(self, buy: JasmineRiceSale) -> None:
        self.get_session.add(buy)
        self.get_session.commit()

    def update_sale(self, id: int, weight_kg: int = None,
                    time: str = None, customer_id: int = None):
        sale = self.get_session.query(JasmineRiceSale).filter(JasmineRiceSale.id == id)
        jasmine_rice_per_kg = 31
        if weight_kg is None:
            weight_kg = sale[0].weight_kg
        if time is None:
            time = sale[0].time
        if customer_id is None:
            customer_id = sale[0].customer_id
        sale.update({JasmineRiceSale.weight_kg: weight_kg,
                     JasmineRiceSale.cost: weight_kg * jasmine_rice_per_kg,
                     JasmineRiceSale.time: time,
                     JasmineRiceSale.customer_id: customer_id})
        self.get_session.commit()
