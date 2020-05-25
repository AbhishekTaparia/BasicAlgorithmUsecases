

def myPow(a, b):
    # if n == 0:   # Base Case
    #     return 1
    # N = n * -1 if n < 0 else n    # Make negative power positive
    # m = myPow(x,  N // 2)    # Calculate x^(N//2) recursively
    # ans = m * m * (x if N % 2 == 1 else 1)    # Handling of odd powers
    # return ans if n > 0 else 1 / ans
    # return x**n
    if(b == 0):
        return 1

    answer = a
    increment = a

    for i in range(1, b):
        for j in range(1, a):
            answer += increment
        increment = answer
    return answer


print(myPow(2, -2))
