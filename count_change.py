def count_changes(money, coins, i=0):
    if money == 0:
        return 1
    elif money < 0:
        return None
    else:
        s = 0
        for i in range(i, len(coins)):
            coin = coins[i]
            if money - coin < coin:
                c = count_changes(money - coin, coins, i+1)
            else:
                c = count_changes(money - coin, coins, i)

            if c:
                s += c
        return s

def count_change(money, coins):
    return count_changes(money, coins)

print(count_change(11, [5,7]))