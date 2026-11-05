import files_helper as f




def main():
    while True:
        choice = f.start_menu_choice()
        if choice == 1:
            id = f.id_order() #מספר בסדר עולה
            items = f.user_product_List() #רשימה של מילונים כל מילון מכיל מזהה של המוצר וכמות
            total = f.total_price(items) #מחיר מקורי פחות אחוזי הנחה 
            f.add_new_order(f.create_new_order(id,items,total)) #יוצר מילון של הזמנה חדשה ומוסיף אותו לתוך ההזמנות הקיימות
            continue
        elif choice == 2:
            if len(f.orders) < 1:
                print('No orders')
                continue
            else:
                f.show_all_orders()
                continue
        elif choice == 3:
            if len(f.orders) < 1:
                print('No orders')
                continue
            else: 
                  f.print_order_by_id()
                  continue
        elif choice == 4:
            if len(f.orders) < 1:
                print('No orders')
                continue
            else: 
                f.close_order_by_id()
                continue


        else:
            print("please enter a whole number")







































if __name__ == "__main__":
    main()