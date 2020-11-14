class Obj:
    def __init__(self, coord, type):
        self.start = coord  # x, y
        if type == 'b':  # 보
            self.end = (coord[0] + 1, coord[1])
        else:  # 기둥
            self.end = (coord[0], coord[1] + 1)
        self.type = type


def solution(n, build_frame):
    # 기둥이 보의 한쪽 끝 부분 위에 있는지?
    def on_bo(x, y):
        for bo in bos:
            if bo.start == (x, y) or bo.end == (x, y):
                return True
        return False

    # 다른 기둥 위에 있는지?
    def other_gi_dung(x, y):
        for g in gi_dungs:
            if g.end == (x, y):
                return True
        return False

    # 보가 한쪽 끝 부분이 기둥 위에 있는지?
    def on_gi_dung(x, y):
        for gi in gi_dungs:
            if gi.end == (x, y) or gi.end == (x + 1, y):
                return True
        return False

    # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는지?
    def bo_connected(x, y):
        for i in range(len(bos)):
            for j in range(len(bos)):
                if i != j and (bos[i].start == (x, y) and bos[j].end == (x + 1, y)) or (
                        bos[i].end == (x, y) and bos[j].start == (x + 1, y)):
                    return True
        return False

    answer = []
    bos = []
    gi_dungs = []
    # x, y 형식
    for a, b, c, d in build_frame:
        if d == 0:  # 삭제
            if c == 0:  # 기둥
                # pop 후 기구가 정상인지 모두 확인, 아니면 취소
                # 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.
                for idx, gi in enumerate(gi_dungs):
                    if gi.start == (a, b):
                        temp = gi_dungs.pop(idx)
                        break
            else:  # 보
                for idx, bo in enumerate(bos):
                    if bo.start == (a, b):
                        temp = bos.pop(idx)
                        break
            # 모든 기둥은 정상인가?
            sanity = True
            for gi in gi_dungs:
                if gi.start[1] == 0 or on_bo(*gi.start) or other_gi_dung(*gi.start):
                    continue
                else:
                    sanity = False
                    break
            if not sanity:
                if temp.type == 'g':
                    gi_dungs.append(temp)
                else:
                    bos.append(temp)
                continue
            # 모든 보는 정상인가?
            for bo in bos:
                if on_gi_dung(*bo.start) or bo_connected(*bo.start):
                    continue
                else:
                    sanity = False
                    break
            if not sanity:
                if temp.type == 'g':
                    gi_dungs.append(temp)
                else:
                    bos.append(temp)
                continue
        else:  # 설치
            # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
            if c == 0:  # 기둥
                if b == 0 or on_bo(a, b) or other_gi_dung(a, b):
                    gi_dungs.append(Obj((a, b), 'g'))
            else:  # 보
                # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
                if on_gi_dung(a, b) or bo_connected(a, b):
                    bos.append(Obj((a, b), 'b'))
    for o in gi_dungs:
        answer.append([o.start[0], o.start[1], 0])
    for o in bos:
        answer.append([o.start[0], o.start[1], 1])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer