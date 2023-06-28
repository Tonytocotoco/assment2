from tabulate import tabulate
from Product import *
from collections import deque
class Node:
    def __init__(self, key = None):
        self.key = key
        self.rt = None
        self.lt = None
    #def

    def insert(self, key):
        if self is None:
            root = Node(key)
            self = root
            return root
        elif key.pcode < self.key.pcode:
            if self.lt == None:
                self.lt = Node(key)
            else:
                self.lt.insert(key)
        elif key.pcode > self.key.pcode:
            if self.rt == None:
                self.rt = Node(key)
            else:
                self.rt.insert(key)
        else:
            print(f'Duplicated key {key}')
        #if
    #def
#class

class BSTree:
    def __init__(self, key = None):
        if key == None:
            self.root = None
        else:
            self.root = Node(key)
    #def

    def insert(self,key=0):
        if self.root == None:
            self.root = Node(key)
        else:
            self.root.insert(key)
    # def insert

    def deleteBST(self, key):
        fnode = None
        fc = None
        curr = self.root

        while curr != None:
            if curr.key.pcode > key:
                fnode = curr
                curr = curr.lt
                fc = 'Left'
            elif curr.key.pcode < key:
                fnode = curr
                curr = curr.rt
                fc = 'Right'
            else: #found
                if fnode == None:
                    
                    if curr.lt == None and curr.rt == None:
                       
                        self.root = None
                    elif curr.lt == None:
                       
                        self.root = curr.rt
                    elif curr.rt == None:
                     
                        self.root = curr.lt
                    else:
                      
                        self.root = curr.rt
                        temp = self.root
                        while temp.lt != None:
                            temp = temp.lt
                        temp.lt = curr.lt
                elif curr.lt == None and curr.rt == None:
               
                    if fc == 'Left':
                        fnode.lt = None
                    else:
                        fnode.rt = None
                elif curr.lt == None:
                  
                    if fc == 'Left':
                        fnode.lt = curr.rt
                    else:
                        fnode.rt = curr.rt 
                elif curr.rt == None:
                 
                    if fc == 'Left':
                        fnode.lt = curr.lt
                    else:
                        fnode.rt = curr.lt 
                else:
                  
               
                    if fc == 'Left':
                        fnode.lt = curr.rt
                    else:  
                        fnode.rt = curr.rt
                    if curr.rt.lt == None:
                        curr.rt.lt = curr.lt
                    else:
                        temp = curr.rt
                        while temp.lt != None:
                            temp = temp.lt
                        temp.lt = curr.lt
                del curr
                break
    def delete (self,p,value):
        if p is None:
            return p
        elif value > p.key.pcode:
            current = self.delete (p.rt,value)
            if p.rt is not None:
                if p.rt.key.pcode == value:
                    p.rt = current
            if p.lt is not None:
                if p.lt.key.pcode == value:
                    p.lt = current
        elif value <  p.key.pcode:
            current = self.delete (p.lt,value)
            
            if p.rt is not None:
                if p.rt.key.pcode == value:
                    p.rt = current
            if p.lt is not None:
                if p.lt.key.pcode == value:
                    p.lt = current
        else:
            if p.lt is None:
                return p.rt
            elif p.rt is None:
                return p.lt
            else:
                value_min = self.min_value(p.rt)
                self.delete (p.right,value_min)
                p.key = value_min
    def min_value(self,p):
        if p is None:
            return None
        else:
            current = p 
            while current.lt:
                current = current.lt
            return current.key             

    def preOrder(self, root = 0):
        curr = root
        if root == 0:
            curr = self.root
        if root == None:
            return []
        else:
            result = []
            result_lt = self.preOrder(curr.lt)
            result.append(curr.key)
            for x in result_lt:
                result.append(x)
            result_rt = self.preOrder(curr.rt)
            for x in result_rt:
                result.append(x)
        return result
    # def pre order traversal

    def inOrder(self, root = 0, result = []):
        curr = root
        if root == 0:
            curr = self.root
        if root == None:
            return None
        else:
            result = []
            result_lt = self.inOrder(curr.lt)
            if result_lt is not None:
                for x in result_lt:
                    result.append(x)
            result.append(curr.key)
            result_rt = self.inOrder(curr.rt)
            if result_rt is not None:
                for x in result_rt:
                    result.append(x)
            
            return result
    # def in order traversal

    def postOrder(self, root = 0):
        curr = root
        if root == 0:
            curr = self.root
        if root == None:
            return []
        else:
            result = []
            result_lt = self.postOrder(curr.lt)
            for x in result_lt:
                result.append(x)

            result_rt = self.postOrder(curr.rt)
            for x in result_rt:
                result.append(x)

            result.append(curr.key)
            return result
    # def post order traversal

    def searchBST(self, key):
        current = self.root

        while current is not None:
            if key == current.key.pcode:
                return current  
            elif key < current.key.pcode:
                current = current.lt  
            else:
                current = current.rt 

        return None
    # def search by key

    def txtInOrder(self, root = 0):
        curr = root
        if root == 0:
            curr = self.root
        if curr == None:
            return []
        else:
            result = []
            result_list = []

            result = self.inOrder(self.root)
            for x in result:
                product = x
                result_list.append([product.pcode, product.pname, product.quantity, product.saled, product.price])


        headers = ["Product code", "Product name", "Quantity", "Saled", "Price"]
        table_str = tabulate(result_list, headers, tablefmt="grid")
        with open("Product_List_IO.txt", "w") as file:
            file.write(table_str)
    # def write in order traversal in txt file

    def txtBreadthFirst(self):
        if self.root is None:
            return []

        nodes = [self.root]
        result = []

        while nodes:
            curr = nodes.pop(0)
            result.append([curr.key.pcode, curr.key.pname, curr.key.quantity, curr.key.saled, curr.key.price])

            if curr.lt:
                nodes.append(curr.lt)
            if curr.rt:
                nodes.append(curr.rt)
        headers = ["Product code", "Product name", "Quantity", "Saled", "Price"]
        table_str = tabulate(result, headers, tablefmt="grid")
        with open("Product_List_BF.txt", "w") as file:
            file.write(table_str)
    #def write breadth first traversal in txt file

    
    def mostSold(self):
        item = self.inOrder(self.root)
        pmostSold = item[0]
        for x in item:
            if pmostSold.saled <= x.saled:
                pmostSold = x
        result = [[pmostSold.pcode, pmostSold.pname, pmostSold.quantity, pmostSold.saled, pmostSold.price]]
        headers = ["Product code", "Product name", "Quantity", "Saled", "Price"]
        table_str = tabulate(result, headers, tablefmt="grid")
        print("This is the product most sold:")
        print(table_str)
        return 

def loadTree(filename):
    pTree = BSTree()
    with open(filename, "r") as file:
        table_str = file.read()
        lines = table_str.split('\n')
        for line in lines[3:-1:2]:
            data = line.split('|')[1:-1]  
            product = Product(data[0].strip(), data[1].strip(), int(data[2].strip()), int(data[3].strip()), float(data[4].strip()))  
            pTree.insert(product)
    return pTree   
#def Load BST from breadth first txt file
