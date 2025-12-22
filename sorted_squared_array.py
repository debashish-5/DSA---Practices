# def sorted_squared(array):
#     n = len(array)
#     res = [0] * n
#     for i in range(n):
#         res[i] = array[i]**2
#     res.sort()
#     return res

# arr = [1,4,3,5,2]
# print(sorted_squared(arr))


def sorted_array(array):
    n = len(array)
    res = [0]*n
    for i in range(n):
        res[i] = array[i] ** 2
    res.sort()
    return res

arr = [5,4,6,3,2,1]

print(sorted_array(arr))

