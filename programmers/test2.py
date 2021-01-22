def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer

arr = [3,2,6]
divisor = 10
print(solution(arr, divisor))