import typing
from collections import Counter

def part1(input: typing.TextIO) -> int:
    answer = 0
    lista, listb = [], []
    for line in input:
        line = line.strip()
        a, b = line.split("   ")
        lista.append(int(a))
        listb.append(int(b))

    for a,b in zip(sorted(lista), sorted(listb)):
        answer += abs(a - b)

    return answer

def part2(input: typing.TextIO) -> int:
    answer = 0
    lista, listb = [], []
    for line in input:
        line = line.strip()
        a, b = line.split("   ")
        lista.append(int(a))
        listb.append(int(b))

    counter = Counter(listb)
    for num in lista:
        answer += num * counter[num]

    return answer

if __name__ == '__main__':
    with open("inputs/day1_input", "r") as infile:
        print(part1(infile))
        infile.seek(0)
        print(part2(infile))