arr = [23,56,22,67,9,1,34,15,98,345,987,67,332]
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        

print("Here is your sorted array:", arr)