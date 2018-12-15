def numbertoordinal(number):
    n = int(number)
    if n == 0:
        return "0"
    elif n == 1:
        suffix = "st"
    elif n == 2:
        suffix = "nd"
    elif n == 3:
        suffix = "rd"
    elif (n % 10) == 1 and n < 20 and n != 11:
        suffix = "st"
    elif (n % 10) == 2 and n != 12 and n < 20:
        suffix = "nd"
    elif (n % 10) == 3 and n != 13 and n < 20:
        suffix = "rd"
    else:
        suffix = "th"
    return str(n) + suffix

print(numbertoordinal(21))
print(numbertoordinal(1000000001))
