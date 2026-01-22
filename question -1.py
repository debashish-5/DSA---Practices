'''
You are given an array of integers in which each subsequent value is not less that previous value .Write a function
that takes this array as input and returns a new array containing squares of all the numbers of the input array in sorted order.

'''
# #Algorithim 1 (Best way)
# arr = [-6, -3, -1, 2, 4, 5]
# print(f"The answer is :{sorted([i**2 for i in arr])}")

# #Algorithim 2 (Using two pointer approach)
# def sortedSquares(arr):
#     n = len(arr)
#     result = [0] * n
#     left, right = 0, n - 1
#     for i in range(n - 1, -1, -1):
#         if abs(arr[left]) > abs(arr[right]):
#             result[i] = arr[left] ** 2
#             left += 1
#         else:
#             result[i] = arr[right] ** 2
#             right -= 1
#     return result



# #Algorithim 3 (Using simple approach)
# results = []
# def sorted_array(arr):
#     for i in arr:
#        result  =  i ** 2
#        results.append(result)
    
#     return result
# print(results)


#------------------------------------------------------------------------------------------------------------
#pratciess
# #Algorithm 1 
# arr = [-6, -3, -1, 2, 4, 5]
# print(f"The Answer is {sorted([i**2 for i in arr])}")


#Algorithm 2(using numpy arr)
# arr =[-6, -3, -1, 2, 4, 5]
# import numpy as np
# arr = np.array(arr)
# print(f'{sorted(arr ** 2)[1]}')

# #Algorithm 3(using for loop)

# arr = [-6, -3, -1, 2, 4, 5]

# for i in arr:
#     result = i**2
#     results = [result]
    
# print(results)



#praticesssssssssssssssssssssssssssssssssssss
def sorted_suqared(array):
    n = len(array)
    i,j = 0,n-1
    res = [0]*n
    for k in reversed(range(n)):
        if array[i] ** 2 > array[j] ** 2:
            res[k] = array[i]**2
            i+=1
        else:
            res[k] = array[j]**2
            j-=1
    return res
array = [-2,1,2,3]
print(sorted_suqared(array))





