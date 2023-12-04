with open("day01.in") as fin:
    data = fin.read()

for line in data.strip().split():
    first = None
    last = None
    for c in line:
        if c.isdigit() and first == None:
            first = c
        if c.isdigit():
            last = c

    num = int(first + last)
    ans += num

print(ans)