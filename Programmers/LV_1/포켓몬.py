nums = [3, 3, 3, 2, 2, 4]

def solution(nums):
    getCount = len(nums) // 2

    dictOfNums = dict.fromkeys(nums)
    distinctNums = list(dictOfNums)

    if len(distinctNums) > getCount:
        return getCount
    else:
        return len(distinctNums)


def solution2(nums):
    return min(len(nums) // 2, len(set(nums)))

