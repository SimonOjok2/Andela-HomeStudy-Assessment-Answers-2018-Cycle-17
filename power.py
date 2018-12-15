def power(a,b):
    ans = a
    if b == 0:
        return 1
    while b > 1:
        ans *= a
        b -= 1
    return ans


print(power(2, 3))