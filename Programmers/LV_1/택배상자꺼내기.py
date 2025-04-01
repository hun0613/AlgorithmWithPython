import math


def solution(n, w, num):
    indexMap = list(range(1, w + 1))
    reverseIndexMap = indexMap[::-1]

    totalRowCnt = math.ceil(n / w)
    targetRow = math.ceil(num / w)

    topRowCnt = totalRowCnt - (targetRow - 1)

    targetIdx = (reverseIndexMap[num % w - 1] if targetRow % 2 == 0 else num % w or w)
    lastIdx = (reverseIndexMap[(n % w or w) - 1] if totalRowCnt % 2 == 0 else n % w or w)

    if totalRowCnt % 2 == 0:
        if targetIdx < lastIdx:
            topRowCnt -= 1
    else:
        if targetIdx > lastIdx:
            topRowCnt -= 1

    return topRowCnt

