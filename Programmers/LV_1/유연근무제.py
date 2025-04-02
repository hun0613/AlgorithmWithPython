def solution(schedules, timelogs, startday):
    answer = 0

    # 인정가능 시각
    pass_time = []
    for i in schedules:
        min = i % 100
        hour = i // 100

        min += 10

        if min > 59:
            hour += 1
            min = min % 60

        pass_time.append(hour * 100 + min)

    # 시작요일로 부터 요일 리스트 생성
    day_of_week_list = list(range(startday, startday + 7))
    day_of_week_list = [n % 7 or 7 for n in day_of_week_list]

    # pass_time timelogs 대조
    for i in range(len(pass_time)):
        isLate = False
        for j in range(len(timelogs[i])):
            if day_of_week_list[j] == 6 or day_of_week_list[j] == 7:
                continue
            # 지각인지 아닌지 판별
            if pass_time[i] < timelogs[i][j]:
                isLate = True

        if not isLate: answer += 1

    return answer