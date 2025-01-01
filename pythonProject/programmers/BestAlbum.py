def sum_up(gg):
    res = 0
    for val, _ in gg:
        res += val
    return res


def solution(genres, plays):
    answer = []
    gen_dict = dict()
    n = len(genres)
    for i in range(n):
        if genres[i] not in gen_dict:
            gen_dict[genres[i]] = [(plays[i], -i)]
        else:
            gen_dict[genres[i]] += [(plays[i], -i)]
    gen_tuples = []
    for k in gen_dict.keys():
        gen_tuples.append((sum_up(gen_dict[k]), k))
    gen_tuples.sort()

    for _, ke in reversed(gen_tuples):
        ls = sorted(gen_dict[ke], reverse=True)
        for j in range(len(ls)):
            if j < 2:
                _, idx = ls[j]
                answer.append(-idx)
            else:
                break
    # gen_dict[genres[i]]
    return answer


print(
    solution(
        ["classic", "pop", "classic", "classic", "pop"], [500, 2500, 150, 800, 2500]
    )
)
