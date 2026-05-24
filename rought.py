# def sorted_squared(array):
#     n  = len(array)
#     res = [0] * n
#     for i in range(n):
#         res[i] = array[i] ** 2
#     res.sort()
#     return res

# print(sorted_squared([1,2,3]))



#monotonic array
# def monotonic_array(array):
#     n = len(array)
#     first = array[0]
#     last = array[n-1]
#     if first > last:
#         for k in range(n-1):
#             if array[k] < array[k+1]:
#                 return False

#     if last > first:
#         for k in range(n-1):
#             if array[k] > array[k+1]:
#                 return False


#     if first == last:
#         for k in range(n-1):
#             if array[k] != array[k+1]:
#                 return False


#     return True

# print(monotonic_array([1,2,3]))

# def kth_sorted(n,k):
#     if n==1:return 0
#     length = 2 ** (n-1)
#     mid = length//2
#     if k <= mid:
#         return kth_sorted(n-1,k)
#     else:
#         return int(not kth_sorted(n-1,k-mid))

# def FindTheWinner(n,k):
#     arr = [i+1 for i in range(n)]
#     def helper(arr,start_index):
#         if len(arr) == 1:
#             return arr[0]
#         index_to_remove = (start_index+k-1) % len(arr)
#         del arr[index_to_remove]
#         return helper(arr,index_to_remove)
#     return helper(arr,0)


def findTheWinner(n,k):
    def josephus(n):
        if n == 1:
            return 0
        return (josephus(n-1)+k)%n
    return josephus(n)+1

