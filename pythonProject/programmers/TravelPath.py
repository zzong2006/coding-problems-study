results = []


def recur(ans, tickets, box):
    if len(box) == len(tickets):
        results.append(ans[:])
        return

    for i in range(len(tickets)):
        if i not in box and tickets[i][0] == ans[-1]:
            box.add(i)
            ans.append(tickets[i][1])
            recur(ans, tickets, box)
            ans.pop()
            box.remove(i)


def solution(tickets):
    answer = ["ICN"]
    ticket_box = set()

    for i in range(len(tickets)):
        # use ticket
        if tickets[i][0] == "ICN" and i not in ticket_box:
            ticket_box.add(i)
            answer.append(tickets[i][1])
            recur(answer, tickets, ticket_box)
            answer.pop()
            ticket_box.remove(i)

    print(sorted(results))


    return results


print(solution(	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
