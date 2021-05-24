import sys

def min_coins(coins, v):
    # print("v = ", v)
    if v == 0:
        return (0, [])
    res = sys.maxsize
    mcs = []
    for c in coins:
        if v >= c:
            (sub_res, cs) = min_coins(coins, v - c)
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
                cs.append(c)
                mcs = cs
    return (res, mcs)

if __name__ == '__main__':
    coins = [50,100,250,500]
    v = 350
    (minc, mcs) = min_coins(coins, v)
    print("Min number of coins for", v, "is:", minc, mcs)