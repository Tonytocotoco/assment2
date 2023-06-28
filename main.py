from BST import *
from LinkedList import * 
from Product import *
from Employee import *
from Customer import *
from Order import *
import os
def check_file_exists(filename):
    return os.path.isfile(filename)
#def

def display_menu():
    print("What category are you interested in?:")
    print("1. Product")
    print("2. Customer")
    print("3. Order")
    print("4. Manager employee")
    print("0. Exit")
#def 

def display_product():
    print("Inventory Management:")
    print("1. Add product")
    print("2. Update product")
    print("3. Inorder Traverse")
    print("4. Breadth-first Traverse")
    print("5. Search by Productcode ")
    print("6. Delete by Productcode")
    print("7. Product most sold ")
    print("8. Count number of products")
    print("0. Exit")
#def

def display_customer():
    print("Customer Management:")
    print("1. Add customer")
    print("2. Display customer list")
    print("3. Search customer by code")
    print("4. Delete customer by code")
    print("0. Exit")
#def

def display_order():
    print("Order Management")
    print("1. Add Order")
    print("2. Display Order list")
    print("3. Complete Order")
    print("4. Print Invoice")
    print("5. Sort by pcode + ccode")
    print("0. Exit")
#def

def display_employee():
    print("Employee Management")
    print("1. Add employee")
    print("2. Display employee list")
    print("3. Dispaly employees with most sales ")
    print("0. Exit")
#def

def run():
    if check_file_exists("Product_List_BF.txt"):
        pTree = loadTree("Product_List_BF.txt")
    else:
        pTree = BSTree()
    if check_file_exists("Customer_List.txt"):
        cList = loadCustomer("Customer_List.txt")
    else:
        cList = LinkedList() 
    if check_file_exists("Order_List.txt"):
        oList = loadOrder("Order_List.txt")
    else:
        oList = LinkedList()
    if check_file_exists("Employee_List.txt"):
        eList = loadEmployee("Employee_List.txt")
    else:
        eList = LinkedList()
    
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            while True:
                display_product()
                choice1 = input("Enter your choice 1: ")
                if choice1 == "1":
                    addProduct(pTree)

                elif choice1 == "2":
                    updateProduct(pTree)
                elif choice1 == "3":
                    inOrderTraversal("Product_List_IO.txt")
                elif choice1 == "4":
                    breathFirstTraversal("Product_List_BF.txt")
                elif choice1 == "5":
                    searchPcode(pTree)
                elif choice1 == "6":
                    deletePcode(pTree)
                elif choice1 == "7":
                    pTree.mostSold()
                elif choice1 == "8":
                    countProduct("Product_List_IO.txt")
                elif choice1 == "0":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 2:
            while True:
                display_customer()
                choice2 = input("Enter your choice 2: ")
                if choice2 == "1":
                    addCustomer(cList)
                elif choice2 == "2":
                    displayCustomer()
                elif choice2 == "3":
                    searchCcode(cList)
                elif choice2 == "4":
                    deleteCcode(cList)
                elif choice2 == '0':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 3:
            while True:
                display_order()
                choice3 = input("Enter your choice 3: ")
                if choice3 == "1":
                    createOrder(pTree, cList, eList, oList)
                elif choice3 == "2":
                    displayOrder()
                elif choice3 == "3":
                    completeOrder(oList,pTree, eList)
                elif choice3 == "4":
                    invoice(oList,pTree, cList)
                elif choice3 == "5":
                    sortOrder(oList)
                    displayOrder()
                elif choice3 == '0':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 4:
            while True:
                display_employee()
                choice4 = input("Enter your choice 4: ")
                if choice4 == "1":
                    addEmplyee(eList)
                elif choice4 == "2":
                    displayEmployee()
                elif choice4 == "3":
                    findMaxRevenue(eList)
                elif choice4 == '0':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == 0:
                    break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    run()

