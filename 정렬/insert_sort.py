array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#
# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j - 1]:
#             array[j], array[j - 1] = array[j - 1], array[j]
#         else:
#             break
#
# print(array)

# 왼쪽은 이미 정렬이 끝난 상태로 간주
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)

# O(N^2 ~ N)