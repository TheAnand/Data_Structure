def LinearSearch(arr,s,k):
	for i in range(0,s) :
		if(arr[i] == k) :
			return i
	else :
		return -1
arr = list(map(int,input().split()))
s = len(arr)
k = int(input("Enter search element "))
r = LinearSearch(arr,s,k)
if ( r==-1 ) :
	print("Element is not present")
else :
	print("Element is present index number ",r)
  
# Linear search is a very simple search algorithm. in this type of linear search a seqentially
# search is made over all item one by one.
# Every item is checked and if maa match is found then that particular item is returned ,otherwise the
# search continues till the end of the data collection."""
