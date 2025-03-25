def solution(a, b):
    dayOfWeek = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    dayCountOfMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 금요일
    initDayOfWeek = 5
    diff = 0

    if a > 1:
        for i in range(a - 1):
            diff += dayCountOfMonth[i]
    diff += b

    finalDayOfWeek = (initDayOfWeek + diff % 7) % 7 - 1

    answer = dayOfWeek[finalDayOfWeek]
    return answer