def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i,n):
            if arr[min] >= arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]


arr = [9,6,7,3,5]
selectionSort(arr)
print(arr)