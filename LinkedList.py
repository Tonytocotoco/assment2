from Customer import *
from Employee import *
from Order import *
from tabulate import tabulate
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def searchcCode(self,key):
        current = self.head

        while current:
            if current.data.ccode == key:
                return current.data
            current = current.next
        return None
    def sort_order (self,cCode = True):
        if self.is_empty():
            return None
        elif self.head.next is None:
            return self
        else:
            if cCode:
                sort_list = LinkedList ()
                sort_arr = []

                current = self.head
                while current is not None:
                    sort_arr.append(current.data)
                    current = current.next
                sorted_arr = sorted(sort_arr, key=lambda x: x.ccode)
                for i in sorted_arr:
                    sort_list.insert(i)
                self.head = sort_list.head
            else:
                sort_list = LinkedList ()
                sort_arr = []

                current = self.head
                while current is not None:
                    sort_arr.append(current.data)
                    current = current.next
                sorted_arr = sorted(sort_arr, key=lambda x: x.pcode)
                for i in sorted_arr:
                    sort_list.insert(i)
                self.head = sort_list.head                
        
        return self
    
    def searcheCode(self,key):
        current = self.head

        while current:
            if current.data.ecode == key:
                return current.data
            current = current.next
        return None
    
    def searcheName(self,key):
        current = self.head

        while current:
            if current.data.ename == key:
                return current.data
            current = current.next
        return None

    def searchoCode(self,key):
        current = self.head

        while current:
            if current.data.ocode == key:
                return current.data
            current = current.next
        return None
    
    def delete(self, ccode):
        if self.head is None:
            return None
        if ccode == self.head.data.ccode:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while True:
            if current.data.ccode == ccode:
                prev.next = current.next
                return
            prev = current
            current = current.next


    def display(filename):
        with open(filename, 'r') as file:
            content = file.read()
        print(content)
    
    #edit
    def txtCustomer(self):
        current = self.head
        result = []
        
        while current:
            cus = current.data
            result.append([cus.ccode, cus.cname, cus.phone])
            current = current.next
        
        headers = ["Customer Code", "Customer Name", "Phone number"]
        table_str = tabulate(result, headers, tablefmt="grid")
        with open("Customer_List.txt", "w") as file:
            file.write(table_str)
    #def

    def txtOrder(self):
        current = self.head
        result = []
        
        while current:
            order = current.data
            result.append([ order.ocode, order.pcode, order.pname, order.ccode,  order.cname, order.quantity, order.ename, order.status, order.time])
            current = current.next
        
        headers = ["Order Code", "Product Code", "Product Name", "Customer Code","Customer Name", "Quanlity", "Employee Name", "Order Status", "Order Time"]
        table_str = tabulate(result, headers, tablefmt="grid")
        with open("Order_List.txt", "w") as file:
            file.write(table_str)
    #def

    def txtEmployee(self):
        current = self.head
        result = []
        
        while current:
            employee = current.data
            result.append([employee.ecode, employee.ename, employee.revenue])
            current = current.next
        
        headers = ["Employee Code", "Employee Name", "Revennue"]
        table_str = tabulate(result, headers, tablefmt="grid")
        with open("Employee_List.txt", "w") as file:
            file.write(table_str)
    #def

    def orderList(self):
        current = self.head
        result = []
        
        while current:
            order = current.data
            result.append([ order.ocode, order.pcode, order.pname, order.ccode,  order.cname, order.quantity, order.ename, order.status, order.time])
            current = current.next
        
        return result

    #def

    def findMax(self):
        curr = self.head
        max = self.head
        while curr:
            if curr.data.revenue > max.data.revenue:
                max = curr
            curr = curr.next
        return max
    #def
    
def loadCustomer(filename):
    cList = LinkedList()
    with open(filename, "r") as file:
        table_str = file.read()
        lines = table_str.split('\n')
        for line in lines[3:-1:2]:
            data = line.split('|')[1:-1]  
            customer = Customer(data[0].strip(), data[1].strip(), data[2].strip())  
            cList.insert(customer)
    return cList
#def

def loadOrder(filename):
    oList = LinkedList()
    with open(filename, "r") as file:
        table_str = file.read()
        lines = table_str.split('\n')
        for line in lines[3:-1:2]:
            data = line.split('|')[1:-1]  
            order = Order(data[0].strip(), data[1].strip(), data[2].strip(), data[3].strip(), data[4].strip(), int(data[5].strip()), data[6].strip(), data[7].strip(), data[8].strip())  
            oList.insert(order)
    return oList
#def

def loadEmployee(filename):
    eList = LinkedList()
    with open(filename, "r") as file:
        table_str = file.read()
        lines = table_str.split('\n')
        for line in lines[3:-1:2]:
            data = line.split('|')[1:-1]  
            employee = Employee(data[0].strip(), data[1].strip(), float(data[2].strip()))  
            eList.insert(employee)
    return eList
#def
