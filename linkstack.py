class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Stack:
		def __init__(self):
			self.head=None

		def insert(self,data):
			if self.head==None:
				self.head=Node(data)
			else:
				newNode=Node(data)
				newNode.next=self.head
				self.head=newNode

		def pop(self):
			if self.head is None:
				print("Stack is empty")
			else:
				temp=self.head.next
				del self.head
				self.head=temp

		def printl(self):
			cur=self.head
			while cur:
				print(cur.data)
				cur=cur.next				
link=Stack()
link.insert(2)
link.insert(4)				
link.insert(5)
link.insert(7)
link.insert(9)
link.printl()
# link.pop()
print("after popping")
link.pop()
link.pop()
link.pop()
link.printl()
