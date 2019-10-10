def BinarySearch(arr,lb,ub,val) :
	while ub>=lb :
		mid = int((lb+ub)/2)
		if arr[mid]==val :
			return mid+1
		elif arr[mid]<val :
			lb = mid+1
		else :
			ub = mid-1
	return -1
arr = list(map(int,input().split()))
val = int(input("Enter value do you want to search "))
r = -1
r = BinarySearch(sorted(arr),0,len(arr)-1,val)
print("Sorted array is ",*sorted(arr))
if r==-1 :
	print("Element is not present.")
else :
	print("Element is present index number ",r)
