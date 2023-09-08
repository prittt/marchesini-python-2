def read_gruppi(filename: str) -> list[int]:
    out = []
    with open(filename, "r") as f:
        s = None
        for line in f:
            if line != '\n':
                #if s is None:
                #    s = 0
                s = (s or 0) + int(line)
            else:
                out.append(s)
                s = None
        if s is not None:
            out.append(s[0])
    return out
    

if __name__ == '__main__':
    lst = read_gruppi('Esercizi 07/gruppi.txt')
    print(lst)
