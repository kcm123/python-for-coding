n, k = map(int, input().split())
#n에서 1을 뺸다, #n에서 K를 나눈다
result = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n = n / k
        result += 1
    else:
        n -= 1
        result += 1
print(result) #결과