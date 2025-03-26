def solution(s):
    mid_index = len(s) // 2
    answer = ''

    if len(s) % 2 == 0:
        answer = s[mid_index - 1: mid_index + 1]
    else:
        answer = s[mid_index]

    return answer