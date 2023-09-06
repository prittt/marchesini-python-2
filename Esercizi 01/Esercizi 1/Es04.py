n = int(input("Dammi un numero intero:"))
# if n % 2 == 0: 
#     print("Il numero", n, "non è primo")
# if n % 3 == 0: 
#     print("Il numero", n, "non è primo")
# if n % 5 == 0: 
#     print("Il numero", n, "non è primo")

# primo = True
# i = 2 
# while i < n:
#     if n % i == 0:
#         primo = False
#         break
#     i += 1

print()

primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
        break


if primo: 
    print("Il numero", n, "è primo")
else: 
    print("Il numero", n, "non è primo")