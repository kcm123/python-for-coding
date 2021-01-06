n = int(input())
route = list(input().split())
x = 1
y = 1
for i in route:
    if i == "L":
        if x == 1: continue
        x -= 1
    elif i == "R":
        if x == n: continue
        x += 1
    elif i == "U":
        if y == 1: continue
        y -= 1
    elif i == "D":
        if y == n: continue
        y += 1
print(y, x)