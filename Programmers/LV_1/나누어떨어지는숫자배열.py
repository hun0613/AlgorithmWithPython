def solution(arr, divisor):
    answer = sorted([n for n in arr if n % divisor == 0])
    return answer or [-1]