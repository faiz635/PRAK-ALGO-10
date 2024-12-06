# def bubbleSort(array):
#     n = len(array)
 
#     for i in range(n):
 
#         for j in range(0, n-i-1):
 
#             if array[j] > array[j+1] :
#                 array[j], array[j+1] = array[j+1], array[j]
                
# def binarySearch(array, l, r, x):
#     if r >= l:
 
#         mid = l + (r - l) // 2
 
#         if array[mid] == x:
#             return mid
 
#         elif array[mid] > x:
#             return binarySearch(array, l, mid-1, x)
 
#         else:
#             return binarySearch(array, mid + 1, r, x)
 
#     else:
#         return -1

# array = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
# x = input("Masukan Angka Targetnya: ")
# x = int(x)

# bubbleSort(array)

# result = binarySearch(array, 0, len(array)-1, x)
# result = int(result)
# print("Diurutkan:", array)


# if result != -1:
#     print("Angka Ada Pada Index", (result)+1)
# else:
#     print("Angka Tidak Ada")


def bubble_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return bubble_sort_recursive(arr[:-1]) + [arr[-1]]

input_data = input("Masukkan angka sebelum disortir : ")
data = [int(x) for x in input_data.split()]  
sorted_data = bubble_sort_recursive(data)
print("Angka yang sudah disortir :", sorted_data)
