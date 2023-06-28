from Customer import *
from Employee import *
from Product import *
import datetime
class Order: 
    def __init__(self,ocode, pcode, pname, ccode, cname, quantity, ename, status, time):
        self.pcode = pcode
        self.ocode = ocode
        self.pname = pname
        self.cname = cname
        self.ename = ename
        self.ccode = ccode
        self.quantity = quantity
        self.status = status
        self.time = time
    #def

#class

def createOrder(pTree, cList, eList, oList):
    while True:
        ocode = input("Enter the order code: ")
        if oList.searchoCode(ocode) is not None:
            print("Order already exists")
        else:
            break
    while True:
        pcode = input("Enter the product code: ")
        if pTree.searchBST(pcode) is None:
            print("Product does not exist!")
        else:
            product = pTree.searchBST(pcode)
            pname = product.key.pname
            break
    while True:
        ccode = input("Enter the customer code: ")
        if cList.searchcCode(ccode) is None:
            print("Customer does not exist!")
            ask = input("Do you want to add customer(y/n)?: ")
            if ask == "y":
                addCustomer(cList)
                customer = cList.searchcCode(ccode)
                cname = customer.cname
                break
            else:
                continue
        else:
            customer = cList.searchcCode(ccode)
            cname = customer.cname
            break
    while True:
        ecode = input("Enter the employee code: ")
        if eList.searcheCode(ecode) is None:
            print("Employee does not exist!")
        else:
            employee = eList.searcheCode(ecode)
            ename = employee.ename
            break
    quantity = int(input("Enter the number of product you want to order: "))
    status = "Ordering"
    time = datetime.datetime.now()
    order = Order(ocode, pcode, pname, ccode, cname, quantity, ename, status, time)
    oList.insert(order)
    oList.txtOrder()
    return "Create order successfully"
#def

def displayOrder():
    print("This is Employee List: ")
    with open("Order_List.txt", 'r') as file:
        content = file.read()
        print(content)
#def

def completeOrder(oList,pTree, eList):
    while True:
        ocode = input("Enter the order code: ")
        order = oList.searchoCode(ocode)
        if order is None:
            print("Order does not exist")
        else:
            break
    checkStatus = order.status
    if checkStatus == "Ordering":
        product = pTree.searchBST(order.pcode)
        available = product.key.quantity - product.key.saled
        if order.quantity <= available:
            order.status = "Completed"
            time = datetime.datetime.now()
            order.time = time
            updateProductSaled(pTree, order.pcode, order.quantity)
            employee = eList.searcheName(order.ename)
            employee.revenue += order.quantity*product.key.price
            oList.txtOrder()
            eList.txtEmployee()
            print(f"Completed the order {ocode}")
        else:
            ask = input("The number of goods in stock is not enough, do you want to wait or reduce the quantity?(w/r): ")
            if ask == "w":
                print("Sorry for the late")
            else:
                order.quatity = available
                order.status = "Completed"
                time = datetime.datetime.now()
                order.time = time
                product.key.saled = product.key.quantity
                employee = eList.searcheName(order.ename)
                employee.revenue += order.quantity*product.key.price
                oList.txtOrder()
                return "Completed the order {ocode}"
#def

def invoice(oList,pTree, cList):
    while True:
        ocode = input("Enter the order code to issue the invoice: ")
        order = oList.searchoCode(ocode)
        if order is not None and order.status != "Ordering": 
            product = pTree.searchBST(order.pcode)
            customer = cList.searchcCode(order.ccode)
            time = order.time
            print("+----------------+---------------+---------------+---------------+---------------+")
            print("INVOICE")
            print("+----------------+---------------+---------------+---------------+---------------+")
            print("1. Customer Information:")
            print(f"Name: {order.cname}")
            print(f"Sdt: {customer.phone}")
            print("+----------------+---------------+---------------+---------------+---------------+")
            print("Invoice Information")
            result = [[product.key.pcode, product.key.pname, order.quantity, product.key.price, order.quantity*product.key.price, time]]
            headers = ["Product code", "Product name", "Quantity", "Price", "Total", "Time"]
            table_str = tabulate(result, headers, tablefmt="grid")
            print(table_str)
            print("+----------------+---------------+---------------+---------------+---------------+")
            print("Order officer")
            print(f"Name: {order.ename}")
            print("+----------------+---------------+---------------+---------------+---------------+")    
        else:
            print("Order does not exist")
            break
#def


def sortOrder(oList):
    sort_code = input(' Sort for Ccode enter 1, Sort for Pcode enter 2')
    if sort_code == '1':
        oList.sort_order(cCode = True)
    elif sort_code == '2':
        oList.sort_order(cCode = False)
    elif sort_code == '0':
        return oList
    else:
        sortOrder(oList)
    oList.txtOrder()
    pass

