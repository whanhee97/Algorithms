def bubbleSort(arr, n):
    for i in range(1, n):
        for j in range(n-i):
            if arr[j+1] <= arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

arr = [7,4,5,1,3]
bubbleSort(arr, len(arr))
print(arr)
