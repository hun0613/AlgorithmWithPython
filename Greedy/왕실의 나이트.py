# 말 위치
pos = input()
row = int(pos[1])
column = int(ord(pos[0])) - int(ord('a')) + 1

# 말이 이동할 수 있는 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

count = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1

print(count)

