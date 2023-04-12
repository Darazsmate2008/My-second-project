t = list(map(lambda x: list(map(int, x.split("-"))),open("input.txt").read().split("\n")))

print("2. feladat")
t1 = t[0]
print(f'Az 1. sorban szereplő számok összege: {sum(t1)}')
