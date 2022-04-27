from models import JasmineRiceSale
from jasmine_rice_sale.jasmine_rice_sale_db import JasmineRiceSaleDb

jasmine_rice_per_kg = 31
jasmine_rice_weight_kg = 50

jasmine_rice_sale = JasmineRiceSaleDb()
print(jasmine_rice_sale.customer().get_customer_by_id(15))
print(jasmine_rice_sale.customer().get_all_customers())
# jasmine_rice_sale.customer().update_customer(id=10, age=18)
print(jasmine_rice_sale.jasmine_rice_sale().get_sale_by_id(10))
print(jasmine_rice_sale.jasmine_rice_sale().get_all_sale())
# jasmine_rice_sale.jasmine_rice_sale().update_sale(id=10, weight_kg=20)

# buying = JasmineRiceSale(weight_kg=jasmine_rice_weight_kg,
#                          cost=jasmine_rice_weight_kg * jasmine_rice_per_kg,
#                          time="114539",
#                          customer_id=16
#                          )
# jasmine_rice_sale.jasmine_rice_sale_dao().buy_jasmine_rice(buying)
