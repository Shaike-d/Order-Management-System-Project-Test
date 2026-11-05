
def start_menu_choice():
    while True:
        from .validation import is_this_a_number
        print("========== ORDER MANAGER ==========")
        print("1. Create order")
        print("2. Show all orders")
        print("3. Find order by ID")
        print("4. Close order")
        print("5. Show sales report")
        print("0. Exit")
        choice = input("please enter your choice: ")
        if is_this_a_number(choice) == True:
            return int(choice)
        else:
            print("please enter a whole number")

def user_product_List(): #-> list of dict
    print("Welcome to new order creation menu")
    product_List = []
    while True:
        product = {}
        id = input("please enter the ID product that you wont: ")
        product["product_id"] = int(id)
        amount = input("please enter how mani units: ")
        product["quantity"] = int(amount)
        product_List.append(product)
        while True:
            more = input("Are you interested in another product? ")
            if more == "yes":
                break
            elif more == "no":
                return product_List
            else:
                print("please enter yes/no only")

def show_all_orders():
    from .products_and_orders import orders
    for order in orders:
        print(order)



def find_order_by_id():
    from .validation import is_this_a_number
    from .products_and_orders import orders
    order_id = input("Enter the order id")
    if is_this_a_number(order_id) == True:
        for order in orders:
            if order["id"] == order_id:
                print(order)
    else:
        print("please enter a whole number")

            


















    # from products_and_orders import orders
    # id = len(orders)+1

    
    
