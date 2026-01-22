# def monotonic_array(array):
#     n = len(array)
#     first = array[0]
#     last = array[n-1]
#     if first > last:
#         for k in range(n-1):
#             if array[k]<array[k+1]:
#                 return False
#     elif first == last:
#         for k in  range(n-1):
#             if array[k]!=array[k+1]:
#                 return False
#     else :
#         for k in range(n-1):
#             if array[k] > array[k+1]:
#                 return False
#     return True

# array = [3,2,1]
# print(monotonic_array(array))

# def monotonic_array(array):
#     n = len(array)
#     first = array[0]
#     last = array[n-1]
#     if first > last:
#         for k in range(n-1):
#             if array[k] < array[k+1]:
#                 return False
#     elif first == last:
#         for k in range(n-1):
#             if array[k] != array[k+1]:
#                 return False
#     else:
#         for k in range(n-1):
#             if array[k] > array[k+1]:
#                 return False
#     return True

# array = [1,2,3,4]
# print(monotonic_array(array))



#practicessssssssssssssssssssssssssssssssssssssssssssssssssssss
# def monotonic_array(array):
#     n = len(array)
#     first = array[0]
#     last = array[n-1]
#     if first > last:
#         for k in range(n-1):
#             if array[k] < array[k+1]:
#                 return False
#     elif first == last:
#         for k in range(n-1):
#             if array[k] != array[k+1]:
#                 return False
#     else:
#         for k in range(n-1):
#             if array[k]>array[k+1]:
#                 return False
#     return True

# array = [1,2,3,4,5]
# print(monotonic_array(array))

#practices
def monotonic_array(array):
    n = len(array)
    first = array[0]
    last = array[n-1]
    if first>last:
        for k in range(n-1):
            if array[k]<array[k+1]:
                return False
    elif first == last:
        for k in range(n-1):
            if array[k]!=array[k+1]:
                return False
    else:
        for k in range(n-1):
            if array[k]>array[k+1]:
                return False
    return True

array = [1,2,3,4,5,6]
print(monotonic_array(array))