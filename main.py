import files_helper as f




def main():
    while True:
        if f.start_menu_choice() == 1:
            id = f.id_order() #מספר בסדר עולה
            items = f.user_product_List() #רשימה של מילונים כל מילון מכיל מזהה של המוצר וכמות
            total = f.total_price(items) #מחיר מקורי פחות אחוזי הנחה 
            f.add_new_order(f.create_new_order(id,items,total)) #יוצר מילון של הזמנה חדשה ומוסיף אותו לתוך ההזמנות הקיימות
        if f.start_menu_choice() == 2:
                f.show_all_orders()


        else:
            print("please enter a whole number")







































if __name__ == "__main__":
    main()