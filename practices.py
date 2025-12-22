# def sorted_array(array):
#     n = len(array)
#     res = [0]*n
#     for i in range(n):
#         res[i] = array[i] ** 2

#     res.sort()
#     return res
# array = [1,2,3]
# print(sorted_array(array))


# def sorted_array(array):
#     n = len(array)
#     res =[0] * n
#     for i in range(n):
#         res[i] = array[i] ** 2
#     res.sort()
#     return res
# array = [1,2,3]
# print(sorted_array(array))

# # method 2:
# def sorted_arraY(array):
#     n = len(array) 
#     i,j = 0,n-1
#     res = [0] * n
#     for k in reversed(range(n)):
#         if array[i]**2 > array[j] ** 2:
#             res[k] = array[i]**2
#             i+=1
#         else:
#             res[k] = array[j] ** 2
#             j-=1
#     return res

# array = [1,2,4,6]
# print(sorted_arraY(array))