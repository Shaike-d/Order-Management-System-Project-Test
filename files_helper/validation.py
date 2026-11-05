

def is_this_a_number(user_input):
    return user_input.isdigit()

def closed_order():
    from .products_and_orders import orders
    closed = []
    for order in orders:
        if order["status"] == "close":
            closed.append(order)
    return closed

def best_sailer(how_mani):
    orders = closed_order()
    top = sorted(orders,key=lambda o: o["total"],reverse=True)
    if len(orders) == 0:
        return orders
    else:
        if how_mani == 1:
            return top[0]
        if how_mani == 3:
            return top[0],top[1],top[2]



def all_benefits_from_sail():
    orders = closed_order()
    total = 0
    for order in orders:
        total += order["total"]
    return total


