from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from jasmine_rice_sale.jasmine_rice_sale_dao import CustomersDao, JasmineRiceSaleDao


class JasmineRiceSaleDb:

    def __init__(self) -> None:
        # SQLite connects to file-based databases
        self.__db_engine = create_engine("sqlite:///database.db")
        session_with_engine = sessionmaker(bind=self.__db_engine)
        self.__db_session = session_with_engine()

    def customer(self):
        return CustomersDao(self.__db_session)

    def jasmine_rice_sale_dao(self):
        return JasmineRiceSaleDao(self.__db_session)
