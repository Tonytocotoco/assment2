from tabulate import tabulate
class Customer:
    def __init__(self, ccode, cname, phone):
        self.ccode = ccode
        self.cname = cname
        self.phone = phone
    #def

#class

def addCustomer(cList):
    ccode = input("Enter the customer code: ")
    cname = input("Enter the customer name: ")
    while True:
        phone = input("Enter the customer phone number: ")
        pcheck = phone.isdecimal()
        if pcheck == False:
            print("You entered it wrong, please re-enter!")
        else:
            break
    checkc = cList.searchcCode(ccode)
    if checkc is not None: 
        print(f"Customer {ccode} is already exist")
    else:
        customer = Customer(ccode, cname, phone)
        cList.insert(customer)
        print("Customer add successfully!")
    cList.txtCustomer()
#def

def displayCustomer():
    print("This is Customer List: ")
    with open("Customer_List.txt", 'r') as file:
        content = file.read()
        print(content)
#def

def searchCcode(cList):
    ccode = input("Enter the customer code you want to find: ")
    customer = cList.searchcCode(ccode)
    if customer is None:
        print(f"Can not find the customer with customer code {ccode}")
    else:
        result = [[customer.ccode, customer.cname, customer.phone]]
        headers = ["Customer Code", "Customer Name", "Phone Number"]
        table_str = tabulate(result, headers, tablefmt="grid")
        print("This is information of product you want to find:")
        print(table_str)
#def

def deleteCcode(cList):
    ccode = input("Enter the product code you want to delete: ")
    customer = cList.searchcCode(ccode)
    if customer is None:
        print(f"Product {ccode} don't have in my list")
    else:
        cList.delete(ccode)
        print(f"Deleted sucessfully customer {ccode}")
    cList.txtCustomer()
#def 