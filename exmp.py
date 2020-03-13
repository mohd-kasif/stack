def removeAdjacent(str):
	stkptr=-1
	i=0
	size=len(str)
	while i<size:
		if (stkptr==-1 or str[stkptr]!=str[i]):
			stkptr+=1
			str[stkptr]=str[i]
			i+=1
		else:
			while i<size and str[stkptr]==str[i]:
				i+=1
			stkptr-=1
	stkptr+=1
	str=str[0:stkptr]
	print(str)
def nextgretar(A):
	nextgreat=float("-inf")
	i=j=0
	for i in range(0,len(A)-1):
		nextgreat=float("-inf")
		for j in range(i+1,len(A)-1):
			if A[i]<A[j]:
				nextgreat=A[j]
				break
		print("for "+str(A[i])+", "+str(nextgreat)+" is the greatest element")
					

nextgretar("658736875658")
# removeAdjacent(["c","a","r","e","e","r","m","o","n","k"])

