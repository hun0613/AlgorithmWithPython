# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 만 사용 가능
# O(N + K)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 1. 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성한다.
count = [0] * (max(array) + 1)

# 2. 각 데이터에 해당하는 인덱스 값 증가
for i in range(len(array)):
    count[array[i]] += 1


# 3. 등장한 횟수만큼 인덱스 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')