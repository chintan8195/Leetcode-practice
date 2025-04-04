"""
Maximize Delivery Pay
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