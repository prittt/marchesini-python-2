def media_v1(my_list: list[int]) -> float:
    somma = 0
    i = 0
    while i < len(my_list):
        somma += my_list[i]
        i += 1
    return somma / len(my_list)


def media_v2(my_list: list[int]):
    somma = 0
    for i in range(len(my_list)):
        somma += my_list[i]
    return somma / len(my_list)


def media_v3(my_list: list[int]):
    somma = 0
    for e in my_list:
        somma += e
    return somma / len(my_list)


def media_v4(my_list: list[int]):
    return sum(my_list) / len(my_list)

import statistics
def media_v5(my_list: list[int]):
    return statistics.mean(my_list)


def varianza_v1(my_list):
    m = media_v3(my_list)
    var = 0
    for i in range(len(my_list)):
        var += (m - my_list[i])**2
    return var/len(my_list)

def varianza_v2(my_list):
    return statistics.pvariance(my_list)


my_list = [1, 2, 3, 4, 5]
print(media_v1(my_list))
print(media_v2(my_list))
print(media_v3(my_list))
print(media_v4(my_list))
print(media_v5(my_list))
print(varianza_v1(my_list))
print(varianza_v2(my_list))