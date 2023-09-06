def ribalta_v1(a: list):
    res = []
    for e in a:
        res = e + res 
    return res






















def ribalta_v2(a: list):
    b = a[:]  # b = a.copy() 
    b.reverse()
    return b

def ribalta_v3(a: list):
    return a[::-1]


a = [1, 2, 3, 4, 5]
print('La lista', a, 'al contrario è ', ribalta_v1(a))
print('La lista', a, 'al contrario è ', ribalta_v2(a))
print('La lista', a, 'al contrario è ', ribalta_v3(a))