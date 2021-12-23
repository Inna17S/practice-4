def factorial(n):
    if int(n)!=n or n<0:
        return 'number should be a natural.'
    elif n == 0:
        return 0
    else:
        n=int(n)
        k = 1
        for i in range(1, n + 1):
            k *= i
        return k