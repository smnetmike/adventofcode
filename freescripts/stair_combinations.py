global all_combs
all_combs = []

def com_count(n, steps, comb):
    if n == 0:
        all_combs.append(comb)
        return 1
    res = 0
    for s in steps:
        if s <= n:
            comb_copy = comb.copy()
            comb_copy.append(s)
            res += com_count(n-s, steps, comb_copy)
    return res


n = 5
steps = [1,2,3]

res = com_count(n, steps, [])
print(f"Number of combinations to climb {n} stairs using steps {steps} is {res}")
print(all_combs)