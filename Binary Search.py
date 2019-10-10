def BinarySearch(arr,lb,ub,val) :
	if ub>=lb :
		mid = int((lb+ub)/2)
		if arr[mid]==val :
			return mid+1
		elif arr[mid]<val :
			return BinarySearch(arr,mid+1,ub,val)
		elif arr[mid]>val :
			return BinarySearch(arr,lb,mid-1,val)
	return -1
arr = list(map(int,input().split()))
val = int(input("Enter value do you want to search"))
r = -1
r = BinarySearch(sorted(arr),0,len(arr)-1,val)
if r==-1 :
	print("Element is not present.")
else :
	print("Element is present index number ",r)
