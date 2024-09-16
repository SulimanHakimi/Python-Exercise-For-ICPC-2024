n = int(input("enter time: "))
number = list(input("enter numbers: ").split())
res = []
for i in number:
    res.append(int(i))
print(max(res))

