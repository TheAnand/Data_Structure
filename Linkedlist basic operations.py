class node :
	# creating a node class
	def __init__(self,data) :
		self.data = data
		self.next = None
class linkedList :
	# creating a linkedlist class
	def __init__(self) :
		self.start = None
	# for view of the linked list
	def viewList(self) :
		# if node is empty then execute the if scope
		if self.start is None :
			print("Linked list is empty")
		# when node is not empty then execute the else scope
		else :
			temp = self.start
			while (temp): 
            			print(temp.data,end=' ')
            			temp = temp.next
		# insertlist is written for insert node in linkedlist
	def insertList(self , value) :
		newNode = node(value)
		# linkedlist is empty then execute the if scope otherwise else scope
		if self.start is None :
			self.start = newNode
		else :
			temp = self.start
			while temp.next is not None :
				temp = temp.next
			temp.next = newNode
		# This function is wriiten for delete elements from the linkedlist
	def deleteList(self) :
		temp = self.start
		if temp.next is None :
			print("Linkedlist is empty")
		else :
			self.start = self.start.next
		# This function is written for count of nodes in linkedlist
	def getCount(self) :
		temp = self.start
		count  = 0
		while temp :
			count +=1
			temp = temp.next
		return count
mylist = linkedList()
mylist.insertList(10)
mylist.insertList(20)
mylist.insertList(30)
mylist.insertList(40)
mylist.insertList(50)
print(mylist.getCount(), end='\n')
mylist.viewList()
print("\n______________")
mylist.deleteList()
mylist.deleteList()
mylist.viewList()
print("\n______________")
print(mylist.getCount())
