from __future__ import annotations
from typing_extensions import Self


class Vector:
    def __init__(self, init_data : list[int, float]) -> None:
        self.__data = list(init_data)

    def __len__(self) -> int:
        return len(self.__data)

    def __str__(self) -> str:
        return f"{self.__data}"
    
    def __getitem__(self, index) -> Self | int | float:
        if isinstance(index, slice):
            return self.__class__(self.__data[index])
        else:
            return self.__data[index]
            
    def __add__(self, other: Self) -> Self:
        if len(other) != len(self):
            raise Exception(f"{other} differs in len from {self}.")

        out = []
        for e1, e2 in zip(self.__data, other):
            out.append(e1 + e2)

        # out = []
        # for i in range(len(self)):
        #     out.append(self.__data[i] + other[i])

        return self.__class__(out)



if __name__ == "__main__":
    v1 = Vector([1, 2, 3, 4]) 
    v2 = Vector((1, 2, 3, 4)) 
    
    print(v1)
    print(v2)
    print(len(v1))

    print(v1[0])
    print(type(v1[0:2]))
    print(v1[0:2])

    vsum = v1 + v2
    print(vsum)

