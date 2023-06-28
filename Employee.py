from tabulate import tabulate
class Employee:
    def __init__(self, ecode, ename, revenue):
        self.ecode = ecode
        self.ename = ename
        self.revenue = revenue
    #def

#class

def addEmplyee(eList):
    ecode = input("Enter employee code: ")
    ename = input("Enter the customer name: ")
    revenue = 0
    checke = eList.searcheCode(ecode)
    if checke is not None: 
        print(f"Customer {ecode} is already exist")
    else:
        employee = Employee(ecode, ename, revenue)
        eList.insert(employee)
        print("Employee add successfully!")
    eList.txtEmployee()
#def

def displayEmployee():
    print("This is Employee List: ")
    with open("Employee_List.txt", 'r') as file:
        content = file.read()
        print(content)
#def

def findMaxRevenue(eList):
    maxRevenue = eList.findMax()
    result = [[maxRevenue.data.ecode, maxRevenue.data.ename, maxRevenue.data.revenue]]
    headers = ["Customer Code", "Customer Name", "Phone Number"]
    table_str = tabulate(result, headers, tablefmt="grid")
    print("This is the employee with the highest sales revenue:")
    print(table_str)
#def 