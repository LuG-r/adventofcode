answer = 0

with open("input.txt", "r") as infile:
    lista, listb = [], []
    for line in infile:
        line = line.strip()
        a, b = line.split("   ")
        lista.append(int(a))
        listb.append(int(b))

    for a, b in zip(sorted(lista), sorted(listb)):
        answer += abs(a - b)

    print(answer)