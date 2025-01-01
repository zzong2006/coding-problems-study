a = []
for i in range(9):
    a.append(int(input()))

for i in range(9):
    for j in range(i + 1, 9):
        sum = 0
        for k in range(9):
            if k != i and k != j:
                sum += a[k]
        if sum == 100:
            a.remove(a[j])
            a.remove(a[i])
            a = sorted(a)
            for w in a:
                print(w)
            break
    if len(a) == 7:
        break
