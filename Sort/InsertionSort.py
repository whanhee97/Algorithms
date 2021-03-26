def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = i
        for j in range(i-1,-1,-1):
            if arr[key] <= arr[j]:
                arr[key], arr[j] = arr[j], arr[key]
                key = j
        

arr = [8, 5, 6, 2, 4,1,3,7,9]
insertionSort(arr)
print(arr)