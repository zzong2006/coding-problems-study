def find_max_value(arr: list, N: int):
    result = 0
    for i in range(1, N):
        if i == 1:
            result = max(arr)
            continue
        if i == N:
            result = max(sum(arr), result)
            continue
        # 1 < i < N 
        # 똑바로 삼각형
        points = [0]
        step = 1
        for j in range(i - 1):
            points.append(points[-1] + step)
            step += 2
        for k in range(1, N - i + 2):           # 삼각형 세로 개수
            for z in range(k):                  # 삼각형 가로 개수
                sums = 0
                for l in range(i):
                    sums += sum(arr[points[l]:points[l] + (l * 2 + 1)])
                result = max(sums, result)
                # 기준점을 가로쪽으로 옮김
                if z != k - 1:
                    for p in range(len(points)):
                        points[p] += 2
            # 기준점을 세로쪽으로 옮김
            if k != N - i + 1 :
                step = 1
                for p in range(len(points)):
                    points[p] += step
                    step += 2

        # 거꾸로 삼각형

    return result


T = 0
ans = []
while True:
    tries = list(map(int, input().split()))
    n = tries[0]
    tries = tries[1:]

    if len(tries) == 0 and n == 0:
        break
    else:
        T += 1
        ans.append(find_max_value(tries, n))

for i in range(T):
    print(str(i) + ". " + str(ans[i]))
