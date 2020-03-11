class Istack:
	"""do limit=10ing for ClassName"""
	def __init__(self, limit=10):
		self.stk=[]
		self.limit=limit

	def is_empty(self):
		return len(self.stk)<=0

	def push(self,item):
		if len(self.stk)>=self.limit:
			print("stack is full")
		else:
			self.stk.append(item)

	def pop(self):
		if len(self.stk)<=0:
			print("stack is empty")
			return 0
		else:
			return self.stk.pop()
	def peek(self):
		return self.stk[-1]
	def printstk(self):
		if len(self.stk)<=0:
			print("stak is empty")
		else:
			# for i in range(len(self.stk)):
			print(self.stk[::-1])
	def checksymbol(self,input):
		sym=Istack()
		for i in input:
			if i in ["(","{","["]:
				sys.push(i)
			else:
				if len(self.stk)<=0:
					balanced=0
				else:
					topsym=

	def inifixtopost(inputexp): #method for infix to postfix conversion
		prec={}
		prec["*"]=3
		prec["/"]=3
		prec["+"]=2
		prec["-"]=2
		prec["("]=1
# 		postList=[]
		token=inputexp.split()
		for i in token:
			if i in "ABCDEFGHIJKLMNOPQRSTUVWXZ" or i in "0123456789":
				postList.append(i)
			elif i=="(":
				self.push(i)
			elif i==")":
				topToken=self.pop()
				while topToken!="(":
					postList.append(topToken)
					topToken=self.pop()
			else:
				while(not self.is_empty()) and (prec[self.peek()]>=prec[i]):
					postList.append(self.pop())
				self.push(i)
		while not self.is_empty():
			postList.append(self.pop())
			print(postList)
			
		def postfixevaluation(self,expr):  #PostFix Evaluation
		token=expr.split()
		for i in token:
			if i in "0123456789":
				self.push(int(i))
			else:
				op2=self.pop()
				op1=self.pop()
				# doMath(i,op1,op2)
				if i=="*":
					a=op1*op2
				elif i=="/":
					a=op1/op2
				elif i=="+":
					a=op1+op2
				else:
					a=op1-op2			
				self.push(a)
		print(self.stk)		
						
					
st=Istack()
st.push(12)
st.push(4)
st.push(3)				
st.push(90)
st.push(76)
st.push(43)
st.printstk()
print("--------------")
st.pop()
st.printstk()
