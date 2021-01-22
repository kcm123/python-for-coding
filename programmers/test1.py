def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i != 0:
            if arr[i] != answer[-1]:
                answer.append(arr[i])
        else:
            answer.append(arr[i])
    return answer

arr = [4,4,4,3,3]
print(solution(arr))