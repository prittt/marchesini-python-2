def add_n(n: int) -> int:
    somma = 0
    for i in range(n + 1):
        somma += i 
    return somma    

res = add_n(n)
print("La somma dei numeri da 1 a", n, "è", res)

