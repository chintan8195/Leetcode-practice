'''
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]


JFK-> MUC->LHR->SFO->SJC

JFK-> SFO,ATL
SFO -> ATL
ATL  -> JFK
ATL->SFO 

JFK -> ATL -> JFK -> SFO -> ATL -> SFO
'''
import collections
def reconstruct_iternary(tickets):
    iternary = collections.defaultdict(list)
    
    for ticket in tickets:
        iternary[ticket[0]].append(ticket[1])
    
    for keys in iternary:
        iternary[keys].sort(reverse=True)

    stack = ["JFK"]
    result = []
    while stack:
        while iternary[stack[-1]]:
            stack.append(iternary[stack[-1]].pop())
        else:
            result.append(stack.pop())
    return result[::-1]


def test():
    assert reconstruct_iternary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])==["JFK", "MUC", "LHR", "SFO", "SJC"], "Should return iternary"
    assert reconstruct_iternary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])==["JFK","ATL","JFK","SFO","ATL","SFO"], "Should return iternary"
    assert reconstruct_iternary([["JFK","SFO"]])== ["JFK","SFO"], "Should return base case"

test()