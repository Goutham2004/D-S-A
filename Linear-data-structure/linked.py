#linked list
#To craete a node 
class Node:
   def __init__(self, dataval):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
   def __init__(self):
      self.headval = None
#The code is to display 
   def listprint(self):
      while self.headval is not None:
         print (self.headval.dataval)
         self.headval= self.headval.nextval

#Proggram to add the node at the beginning
   def add_first(self,data):
      new_node = Node(data)
      new_node.nextval=self.headval
      self.headval=new_node
#Proggram to add the element at the last
   def add_last(self,data): 
      new_node = Node(data)
      if self.headval is None:
       self.headval = new_node      
      else:
       n=self.headval
       while n.nextval is not None:
          n=n.nextval
      n.nextval=new_node
#Proggram to add node before a specific Node:
   def add_before(self,x,data):
        if self.headval is None:
            print("ll is empty")
            return
         #here if the linked list contain only one node:
        if self.headval.dataval ==x:
               new_node=Node(data)
               new_node.nextval=self.headval
               self.headval=new_node
               return
            #if linked list contain multiple node:
        n = self.headval
        while n.nextval is not None:
            if n.nextval.dataval == x:
              break
            n = n.nextval
        new_node = Node(data)
        new_node.nextval = n.nextval
        n.nextval = new_node
#Proggram to add node after a specific Node:
   def add_after(self,target, dataval):
    if (self.headval.dataval == target):
        new_node = Node(dataval)
        new_node.nextval = self.headval
        self.headval = new_node
    else:
      n = self.headval
      while(n.dataval != target):
         n = n.nextval
      new_node = Node(dataval)
      new_node.nextval = n.nextval
      n.nextval = new_node
#This is for the delete the element at the first:
   def delbegging(self):
      if self.headval is None:
         print("ll is empty")
      else: 
         self.headval=self.headval.nextval
#This is for the delete the element at the End:
   def delend(self):
      if self.headval is None:
       print("ll is empty")
      else:
         n=self.headval
      while n.nextval.nextval is not None:
         n=n.nextval
      n.nextval=None
#This is to delete the specific element in a linked list:
   def remove_node(self, remove_data):
        n = self.headval

        # Remove if data is the first element
        if n is not None:
            if n.dataval == remove_data:
                self.headval = n.nextval
                n = None
                return

        # find out the data node and previous node
        while n is not None:
            if n.dataval == remove_data:
                break
            prev = n
            n = n.nextval

        # Return if head val is empty
        if n == None:
            return

        # Remove item from linked list
        prev.nextval = n.nextval
        n = None



list = LinkedList()

list.headval = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)
# Link first Node to second node
list.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3
# Link third Node to fourth node 
e3.nextval = e4
# Link four Node to five node
e4.nextval = e5
e5.nextval = e6
#list.add_before(1,499)
list.remove_node(2)
#list.add_last(7)
#list.add_first(0)
#list.delbegging()
#list.delend()
list.listprint()
