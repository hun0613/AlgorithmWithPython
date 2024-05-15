# 정수 N이 입력되면 0시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구한느 프로그램을 작성하시오

# 정수 받기
h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): # in으로 문자열 내 특정 문자가 포함되어있는지 확인할 수 있다.
                count += 1

print(count)