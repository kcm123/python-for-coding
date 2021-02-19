def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        for j in participant:
            if completion[i] == j:
                participant.remove(j)
    answer = participant[0]
    return answer

participant = 	["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]