n = int(input())

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(len(array)):
    sum = 0
    for j in array[i]:
        if j % 2:
            sum += j

    print(f"#{i + 1} {sum}")