# def fibonacci(n):
#     if n<=1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(4))

## Memoization

# def fibonacci_2(n,ht = {0:0,1:1}):
#     if n in ht:
#         return ht[n]
#     else:
#         ht[n] = fibonacci_2(n-1,ht) + fibonacci_2(n-2,ht)
#         return ht[n]
    
# print(fibonacci_2(4))


## Tabulation
# def fibonacci(n):
#     dp = [0] * (n+1)
#     if n>0:
#         dp[1] = 1
#     count = 1
#     while(count < n):
#         count +=1
#         dp[count] = dp[count-1] + dp[count -2]
#     return dp[n]


# print(fibonacci(5))

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
    
