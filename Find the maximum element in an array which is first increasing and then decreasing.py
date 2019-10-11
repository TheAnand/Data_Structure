def BinarySearch(arr,low,high) :
	max = arr[low]
	i = low
	for i in range(0,high+1) :
		if arr[i] > max :
			max = arr[i]
	return max
arr = list(map(int,input().split()))
print("The maximum element is ",BinarySearch(arr,0,len(arr)-1))
