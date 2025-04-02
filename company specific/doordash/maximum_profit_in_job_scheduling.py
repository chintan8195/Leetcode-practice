"""

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.


Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
"""

import bisect
from typing import List


def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    # Combine and sort jobs based on their end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        
        # Create a list of end times to use in binary search
        ends = [job[1] for job in jobs]
        
        # Initialize dp array where dp[i] is max profit up to i-th job (using 1-indexed dp for convenience)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]
            # Find the last job that ends on or before the start of the current job using binary search
            index = bisect.bisect(ends, s) - 1
            # If index is valid, add the profit from dp[index+1] (convert to dp index), otherwise just current profit.
            if index != -1:
                include_profit = p + dp[index + 1]
            else:
                include_profit = p
            # dp[i] is the max of not taking the current job or taking it.
            dp[i] = max(dp[i - 1], include_profit)
        
        return dp[n]
 