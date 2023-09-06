def potenze_v1(base, maxexp):
    ret = []
    for i in range(maxexp + 1):
        ret.append(base**i)
    return ret

def potenze_v2(base, maxexp):
    ret = []
    for i in range(maxexp + 1):
        ret.extend([base**i])
    return ret

def potenze_v3(base, maxexp):
    ret = []
    for i in range(maxexp + 1):
        ret += [base**i]
    return ret

print(potenze_v1(2, 10))
print(potenze_v2(2, 10))
print(potenze_v3(2, 10))