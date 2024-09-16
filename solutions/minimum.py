n = int(input("time: "))

numbers = list(input("numbers: ").split())
res = []
for i in numbers:
    res.append(int(i))
print(min(res))