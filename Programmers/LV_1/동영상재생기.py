def solution(video_len, pos, op_start, op_end, commands):
    # "00:00" 이 형태를 int 형태(1234)로 변환 (값을 비교하기 위해서)
    def to_mmss_format(times):
        return times[0] * 100 + times[1]

    pos_times = list(map(int, pos.split(':')))  # 비교 시에만 int 형태로 전환

    len_times = list(map(int, video_len.split(':')))
    len_time = to_mmss_format(len_times)

    op_start_time = to_mmss_format(list(map(int, op_start.split(':'))))

    op_end_times = list(map(int, op_end.split(':')))
    op_end_time = to_mmss_format(op_end_times)

    # next 메소드 만들기
    def next(min, sec):
        # 1. 현재 재생위치(pos)에서 10초이후 값 구하기
        plus_sec = sec + 10
        res_times = [min + 1, plus_sec % 60] if plus_sec > 59 else [min, plus_sec]
        res_time = to_mmss_format(res_times)
        # 2. 만약 현재 재생위치가 영상 종료까지 10초 미만 남았을 경우 영상 마지막 위치로 이동
        # 3. skip 메소드 실행
        return len_times if res_time > len_time else skip(res_time, res_times)

    # prev 메소드 만들기
    def prev(min, sec):
        # 1. 현재 재생위치(pos)에서 10초이전 값 구하기
        minus_sec = sec - 10
        res_times = [min - 1, 60 + minus_sec] if minus_sec < 0 else [min, minus_sec]
        res_time = to_mmss_format(res_times)
        # 2. 만약 현재 재생위치가 10초 미만일 경우 영상의 처음 위치 (00:00)으로 이동
        # 3. skip 메소드 실행
        return [0, 0] if res_time < 10 else skip(res_time, res_times)

    # skip 메소드 만들기
    def skip(curr_pos_time, curr_pos_times):
        # 1. 현재 재생위치가 오프닝 스킵 구간에 있을 경우, 오프닝 종료 시각으로 이동
        return op_end_times if curr_pos_time >= op_start_time and curr_pos_time <= op_end_time else curr_pos_times

    # 현재위치 초기값이 오프닝 스킵구간에 있다면 오프닝 종료시각으로 셋팅
    pos_times = skip(to_mmss_format(pos_times), pos_times)

    # commands를 순회하며 메소드 실행
    for i in commands:
        if i == 'prev':
            pos_times = prev(pos_times[0], pos_times[1])
        else:
            pos_times = next(pos_times[0], pos_times[1])

    # 최종값을 "00:00" 형태로 변환
    def to_str_time_format(curr_pos_times):
        curr_min = "0" + str(curr_pos_times[0]) if curr_pos_times[0] < 10 else str(curr_pos_times[0])
        curr_sec = "0" + str(curr_pos_times[1]) if curr_pos_times[1] < 10 else str(curr_pos_times[1])
        return curr_min + ":" + curr_sec

    return to_str_time_format(pos_times)