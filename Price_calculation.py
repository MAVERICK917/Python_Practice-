def Calculation_of_total_price(price_per_unit,quantity):
    Sub_total=price_per_unit*quantity
    VAT=Sub_total*0.13
    total_price=Sub_total+VAT
    return total_price

TOTAL_CHARGE_DEAR_CUSTOMER=Calculation_of_total_price(10,2)
print(TOTAL_CHARGE_DEAR_CUSTOMER)