# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import OrderedDict, defaultdict
from itertools import combinations, product


class Tr:
    def __init__(self, name=None):
        self.table_name = name
        self.table = defaultdict(Tr)
        self.total_num = defaultdict(int)
        self.end = False

    def insert(self, psn, key_list):
        curr = self
        for k in key_list:
            attr, value = k, psn[k]
            if curr.table_name is None:
                curr.table_name = attr
            curr.total_num[value] += 1
            curr = curr.table[value]
        curr.end = True


def solution():
    def get_support_value(q, curr: Tr, key_list, idx, matched, total):
        t = 0
        if key_list[idx] not in q:
            for k in curr.table.keys():
                t += get_support_value(q, curr.table[k], key_list, idx + 1, matched, total)
        else:
            if q[key_list[idx]] in curr.table:
                if matched + 1 == total:
                    t += curr.total_num[q[key_list[idx]]]
                else:
                    t += get_support_value(q, curr.table[q[key_list[idx]]], key_list, idx + 1, matched + 1, total)
        return t

    answer = []
    get_input = sys.stdin.readline
    attribute = int(get_input().strip())
    threshold = float(get_input().strip())
    num_of_rows = int(get_input().strip())
    trie = Tr()
    attr_table = defaultdict(set)

    for t in range(num_of_rows):
        infos = get_input().strip().split(',')
        person = OrderedDict()
        for info in infos:
            attr, value = info.split('=')
            person[attr] = value
            attr_table[attr].add(value)
        if t == 0:
            attr_list = sorted(person.keys())
        trie.insert(person, attr_list)

    for attr_comb in combinations(attr_table.keys(), attribute):
        iterables = [attr_table[c] for c in attr_comb]
        for value_comb in product(*iterables):
            query = dict()
            for k in range(len(value_comb)):
                query[attr_comb[k]] = value_comb[k]
            print(query)
            # sv = get_support_value(query, trie, attr_list, 0, 0, attribute)
            # if sv >= threshold * num_of_rows:
            #     answer.append(query)

    for res in answer:
        print(','.join(['{}={}'.format(k, res[k]) for k in res.keys()]))

    return None


solution()
