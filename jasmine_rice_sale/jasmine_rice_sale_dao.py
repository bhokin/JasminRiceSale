from abc import ABC
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


class JasmineRiceSaleDao(Dao):
    def get_sale_by_id(self, id: int) -> JasmineRiceSale:
        return self.get_session.query(JasmineRiceSale).filter(JasmineRiceSale.id == id)[0]