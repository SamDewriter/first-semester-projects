# Entry point for the MiniMart data reporting system
# Entry point for the student management system
from utils import  new_order, merge_product, convert_currency
import report_generator as rgt


print(" MiniMart Sales System")

while True:
    print("\n1. New_orders \n2. Merge_products \n3. Convert_currency \n4. Report Generator \n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        new_order()
    elif choice == "2":
        merge_product()
    elif choice == "3":
        convert_currency()
    elif choice == "4":
        rgt() 
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")