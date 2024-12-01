from collections import Counter

answer = 0

with open("input.txt", "r") as infile:
    lista, listb = [], []
    for line in infile:
        line = line.strip()
        a, b = line.split("   ")
        lista.append(int(a))
        listb.append(int(b))

    counter = Counter(listb)
    for num in lista:
        answer += num * counter[num]
    

    print(answer)