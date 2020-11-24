# Enter your code here. Read input from STDIN. Print output to STDOUT


import sys
import math


def solution():
    get_input = sys.stdin.readline
    num_sim_user_topk = int(get_input().strip())  # N (최근접 유저를 계산할 계수)
    num_item_rec_topk = int(get_input().strip())  # 추천할 아이템 개수 N (top N개를 추천)
    num_users = int(get_input().strip())  # 유저 개수
    num_items = int(get_input().strip())  # 사용자 개수
    num_rows = int(get_input().strip())  # transaction 횟수

    users = [dict() for i in range(num_users)]

    for i in range(num_rows):
        user, item, rating = list(map(float, get_input().strip().split()))
        # convert to zero index
        user = int(user) - 1
        item = int(item) - 1
        users[user][item] = rating

    average_rating = [0] * num_users
    # 사용자 u 의 rating 한 모든 item에 대한 평균값 계산
    for i in range(num_users):
        average_rating[i] = sum(users[i].values()) / len(users[i].keys())

    # 최근접 이웃 집합 구성
    n_closest_users = [set() for i in range(num_users)]
    n_closest_value = dict()
    for i in range(num_users):
        temp_dict = {}  # 다른 유저 간 유사도
        for j in range(num_users):
            if i != j:
                temp_dict[j] = cosine_similiarty(users[i], users[j])

        sim_of_user_i = list(temp_dict.keys())
        sim_of_user_i.sort(key=lambda x: temp_dict[x], reverse=True)
        n_closest_users[i] = n_closest_users[i].union(set(sim_of_user_i[:num_sim_user_topk]))

        # 전체 사용자에 대한 유사도 저장 
        n_closest_value[i] = temp_dict


    num_reco_users = int(get_input().strip())  # 추천할 유저 총 개수

    for i in range(num_reco_users):
        target_user = int(get_input().strip())  # 추천 대상 유저 T
        target_user -= 1  # convert to zero index

        # 평가되지 않은 모든 item에 대한 user T의 평가를 계산함
        unrated = set(range(num_items)) - set(users[target_user].keys())
        ratings = dict()

        for k in unrated:  # 평가 안된 영화 k 에 대한 rating
            total = average_rating[target_user]
            # total = 0
            # (1) k 식 계산
            value_of_k = 0
            sigma_val = 0
            for f in n_closest_users[target_user]:
                # 가까운 사용자라도 해당 영화를 본 사람만 rating 계산이 가능함
                if k in users[f]:
                    sim_val = n_closest_value[target_user][f]
                    value_of_k += abs(sim_val)
                    sigma_val += (sim_val * (users[f][k] - average_rating[f]))
            if value_of_k != 0:
                value_of_k = 1 / value_of_k
                ratings[k] = total + value_of_k * sigma_val

        unrated_movies = list(ratings.keys())
        unrated_movies.sort(key=lambda x: ratings[x], reverse=True)
        print(' '.join(map(str, unrated_movies[:min(len(unrated), num_item_rec_topk)])))

def cosine_similiarty(user_x: dict, user_y: dict):
    x_set = set(user_x.keys())
    y_set = set(user_y.keys())

    # x와 y 둘 다 rating한 item 목록
    inter_set = x_set.intersection(y_set)
    uni_set = x_set.union(y_set)
    sim = 0.0
    r_xy = 0.0
    r_x = 0.0
    r_y = 0.0

    for k in uni_set:
        if k in inter_set:
            r_xy += user_x[k] * user_y[k]
        if k in x_set:
            r_x += (user_x[k]) ** 2
        if k in y_set:
            r_y += (user_y[k]) ** 2

    try:
        sim = r_xy / (math.sqrt(r_x) * math.sqrt(r_y))
    except:
        return 0
    else:
        return sim


solution()
