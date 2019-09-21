class node :
	def __init__(self,data) :
		self.data = data
		self.next = None
class linkedList :
	def __init__(self) :
		self.start = None
	def insertList(self,value) :
		newNode = node(value)
		if self.start is None :
			self.start =  newNode
		else :
			temp = self.start
			while temp.next is not None :
				temp = temp.next
			temp.next = newNode
	def getCountRec(self , node) :
		if (not node ) :
			return 0
		else :
			return 1+self.getCountRec(node.next)
	def getCount(self) :
		return self.getCountRec(self.start)
ll = linkedList()
ll.insertList(100)
ll.insertList(20)
ll.insertList(2323)
print(ll.getCount())
