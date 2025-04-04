"""
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

 

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0

"""


"""
You're a dasher, and you want to try planning out your schedule. You can view a list of deliveries along with their associated start time, end time, and dollar amount for completing the order. Assuming dashers can only deliver one order at a time, determine the maximum amount of money you can make from the given deliveries.

The inputs are as follows:

int start_time: when you plan to start your schedule
int end_time: when you plan to end your schedule
int d_starts[n]: the start times of each delivery[i]
int d_ends[n]: the end times of each delivery[i]
int d_pays[n]: the pay for each delivery[i]
The output should be an integer representing the maximum amount of money you can make by forming a schedule with the given deliveries.
  Constraints

end_time >= start_time
d_ends[i] >= d_starts[i]
d_pays[i] > 0
len(d_starts) == len(d_ends) == len(d_pays)
  Example 1

start_time = 0
end_time = 10
d_starts = [2, 3, 5, 7]
d_ends = [6, 5, 10, 11]
d_pays = [5, 2, 4, 1]
Expected output: 6
 

Followup 1: Return the jobs as well which will give max profit

Followup 2: If the dasher is allowed to handle up to N orders at the same time, what will be the max profit?
"""

"""
Similar to Leetcode 1235. Use DP to solve. Remove/ignore jobs that don't lie entirely within [start_time, end_time]

Followup 1: In the DP array, instead of just storing max profit for a given index, also store which intervals led to that max profit. This will be either be [currInterval, nextAvailableInterval], or [nextImmediateInterval] -- since these are the 2 choices we made in the DP solution.

After you have finished with the DP, you end up with something like the following DP array:

0: [20, [0,3]] --> index 0 has max profit of 20, and used profits from indices 0,3 in to get there
1: ...
2: ...
3: [10, [4]] --> index 3 has max profit of 10, and used interval 4 to get it
4: [10, [4]] --> index 4 used itself to get max profit of 4
...
You can follow through the indices and collect which values were used. If the current index is in the list of intervals used, add it to the solution. Continue checking for the remaining index in the list.

0: [0,3] --> add 0 to jobs since index == 0. go to index 3
3: [4] --> 3 is missing from intervals, so don't add it. go to index 4
4: [4] --> add 4 to jobs since index == 4. No other items used, so terminate

jobs = [0,4]
This is O(n) operation. You can also do this during the DP itself rather than getting the selected jobs at the end.

Followup 2: Run the scheduler once -> remove the jobs that yield max profit -> run the scheduler a second time with the remaining jobs -> remove the jobs -> ... -> repeat until we get k overlaps
"""