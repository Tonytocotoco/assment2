from tabulate import tabulate
from BST import *
class Product:
    def __init__(self,pcode, pname, quantity, saled, price):
        self.pcode = pcode
        self.pname = pname
        self.quantity = quantity
        self.saled = saled
        self.price = price
    #def

def updateProductSaled(pTree, pcode, upsaled):
    node = pTree.searchBST(pcode)
    node.key.saled += upsaled
    pTree.txtInOrder()
    pTree.txtBreadthFirst()
    return f"Update saled successfully!"

#def

def updateProduct(pTree):
    pcode = input("Enter the product code: ")
    checkp = pTree.searchBST(pcode)
    if checkp is not None: 
        upquantity = int(input(f"Enter the new quantity of product: "))
        upsaled = int(input(f"Enter the new saled of product: "))
        checkp.key.quantity += upquantity
        checkp.key.saled += upsaled
    else:
        print("The product does not exist in stock, choose add product option to add a new one")
    pTree.txtInOrder()
    pTree.txtBreadthFirst()
    return f"Update product successfully!"
#def

def addProduct(pTree):
    pcode = input("Enter the product code: ")
    checkp = pTree.searchBST(pcode)
    pname = input("Enter the product name: ")
    while True:
        quantity = int(input(f"Enter the quantity of {pname}: "))
        saled = int(input(f"Enter the number of {pname} sold: "))
        if saled > quantity: 
            print("You entered it wrong. Please re-enter")
        else:
            break
    price = float(input(f"Enter the price of {pname}: "))
    if checkp is not None:
        print("The product is already in stock, choose update option to update product!")
        return
    else:
        product = Product(pcode, pname, quantity, saled, price)
        pTree.insert(product)
        print(f"{pname} add successfully in stock")
    pTree.txtInOrder()
    pTree.txtBreadthFirst()
    return f"Add product successfully!"
#def add product and write in txt file with InOrder and BreadthFirst

def inOrderTraversal(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)
#def

def breathFirstTraversal(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)
#def

def searchPcode(pTree):
    pcode = input("Enter the product code you want to find: ")
    product = pTree.searchBST(pcode)
    if product is None:
        print(f"Can not find the product with product code {pcode}")
    else:
        result = [[product.key.pcode, product.key.pname, product.key.quantity, product.key.saled, product.key.price]]
        headers = ["Product code", "Product name", "Quantity", "Saled", "Price"]
        table_str = tabulate(result, headers, tablefmt="grid")
        print("This is information of product you want to find:")
        print(table_str)
#def

def deletePcode(pTree):
    pcode = input("Enter the product code you want to delete: ")
    product = pTree.searchBST(pcode)
    if product is None:
        print(f"Product {pcode} don't have in my stock")
    else:
        pTree.delete(pTree.root,pcode)
        pTree.txtInOrder()
        pTree.txtBreadthFirst()
        print(f"Deleted sucessfully product {pcode}")
#def

def countProduct(filename):
    with open(filename, "r") as file:
        table_str = file.read()
        lines = table_str.split('\n')
        count = 0
        for line in lines[3:-1:2]:
            count += 1
    print(f"Number of product is: {count}")

   
#def
