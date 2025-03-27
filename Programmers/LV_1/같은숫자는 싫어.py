def solution(arr):
    answer = [arr[0]]
    previousNum = arr[0]

    for i in arr[1:]:
        if i != previousNum:
            answer.append(i)
            previousNum = i

    print(arr[-1:])

    return answer