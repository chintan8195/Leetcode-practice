'''Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
'''

def twoCitySchedCost(costs):
    costs.sort(key = lambda x:x[0]-x[1])
    min_cost = 0
    n= len(costs)//2
    for i in range(n):
        min_cost += costs[i][0]+costs[i+n][1]
    return min_cost

costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedCost(costs))