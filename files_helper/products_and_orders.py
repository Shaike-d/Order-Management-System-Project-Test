orders = []
PRODUCTS = [
    {"id" : 1, "name" : "Keyboard", "price" : 120},
    {"id" : 2, "name" : "Mouse", "price" : 80},
    {"id" : 3, "name" : "Monitor", "price" : 900},
    {"id" : 4, "name" : "Headphones", "price" : 200},
    {"id" : 5, "name" : "Usb Cable", "price" : 30}
    ]

def id_order():
    return len(orders)+1


def original_price(items:list[dict]): #-> int
    orig_price = 0
    for item in items: #item = dict
        for product in PRODUCTS: #product = dict
            if item["product_id"] == product["id"]:
                orig_price += product["price"]*item["quantity"]
    return orig_price


def total_price(items):
    org_price = original_price(items)
    if org_price < 300:
        return org_price
    elif org_price < 700:
        return org_price-((org_price/100)*5)
    elif org_price < 1500:
        return org_price-((org_price/100)*10)
    else:
        return org_price-((org_price/100)*15)
    
    
def create_new_order(id:int,items:list[dict],total:int,status = "open"):# -> dict
    order = {}
    order["id"] = id
    order["items"] = items
    order["total"] = total
    order["status"] = status
    return order

def add_new_order(order:dict): #מוסיף הזמנה לרשימת הזמנות
    orders.append(order)
