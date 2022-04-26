from jasmine_rice_sale.jasmine_rice_sale_db import JasmineRiceSale


jasmine_rice_sale = JasmineRiceSale()

print(jasmine_rice_sale.customer().get_customer_by_id(15))
print(jasmine_rice_sale.jasmine_rice_sale_dao().get_sale_by_id(10))
