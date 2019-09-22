class node :
	def __init__(self , data) :
		self.data = data
		self.next = None
class linkedList :
	def __init__(self) :
		self.start = None
	def insertList(self , value) :
		newNode = node(value)
		if self.start is None :
			self.start = newNode
		else :
			temp = self.start
			while temp.next is not None :
				temp = temp.next
			temp.next = newNode
	def viewList(self) :
		temp = self.start
		while temp :
			print(temp.data , end=' ')
			temp = temp.next
	def delList(self , key) :
		temp = self.start
		if ( temp is not None) :
			if (temp.data == key ) :
				self.start = temp.next
				temp = None
		while temp is not None :
			if temp.data == key :
				break
			prev = temp
			temp = temp.next
		if (temp == None) :
			print("\nEntry does not exist")
			return 0
		prev.next = temp.next
		temp = None
ll = linkedList()
print("Enter size of linkedList")
num = int(input())
for i in range(num) :
	print("Enter {0} number".format(i+1))
	ll.insertList(int(input()))
ll.viewList()
print("\nEnter number you want to delete :")
n = int(input())
ll.delList(n)
ll.viewList()
