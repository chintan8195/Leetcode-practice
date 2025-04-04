"""
# Part 1
# You are in charge of implementing the dasher payment model. The
first
# version of the payment model is naively based on how much time
dasher
# spends on each order. Given the sequence of accepted/fulfilled
order
# activities from a given dasher on a given day, calculate the
dasher
# pay based on the following payment rules
# 1. base pay rate: $0.3 per minute
# 2. multi order pay rate: # ongoing deliveries * base pay rate
#
(when dasher is delivering multiple orders at the same
time）
# Assumptions:
# 1. All order activities are from the same calendar day
# 2. Order activity sequence is valid. All orders are fulfilled
by end
# of day (no duplicates, no fulfillment without pickup, no pickup
#
without fulfillment, etc).
# Example:
# Input:
# 06:15: Dx accepted order A
# 06:18: Dx accepted order B
# 06:36: Dx fulfilled order A
# 06:45: Dx fulfilled order B
# Output: final pay: $14.4
# Explanation:
# 06:15 - 06:18 →> рау = 3 * 0.3 →> $0.9
# 06:18 - 06:36 →> pay = 2 orders * 0.3 * 18 →> $10.8
# 06:36 - 06:45 →> рау = 0.3 * 9 = $2.7


Part 2
# Our previous version of the payment model is flawed, such that it
# overcounts the time a given dasher spends between arrival and pick up
# for a given order (e.g. food packing, food paying, wait time, etc).
# The new payment model should still be able to give dasher credit when
# deliverying multiple orders at the same time, but the time spent at a
# given store should not be counted toward other orders.

# Assumptions from Part 1 apply.

# Example
# Input:
# 06:15: Dx accepted order A  
# 06:18: Dx accepted order B  
# 06:19: Dx arrived at pick up location for A  
# 06:22: Dx picked up order A  
# 06:30: Dx arrived at pick up location for B  
# 06:33: Dx picked up order B  
# 06:36: Dx fulfilled order A  
# 06:45: Dx fulfilled order B

# Output: final pay: $12.6

# Explanation:
# 06:15 - 06:18 -> pay = 3 * 0.3 = $0.9
# 06:18 - 06:19 -> pay = 2 orders * 0.3 = $0.6
# 06:19 - 06:22 -> pay = 3 * 0.3 = $0.9
# 06:22 - 06:30 -> pay = 2 orders * 0.3 * 8= $4.8
# 06:30 - 06:33 -> pay = $0.9
# 06:33 - 06:36 -> pay = 2 * 0.3 * 3 = $1.8
# 06:36 - 06:45 -> pay = 0.3 * 9 = $2.7


# Part 3
# To make sure we have enough dashers on the wheel during rush hours,
# doordash promotes peak hours that doubles the pay during certain
# windows. Given the peak hour windows (e.g. `[["06:20", "06:30"]]`)
# and the order activity sequence, calculate the new pay.

# Assumptions from Part 1 apply.

# Example
# Input:
# peak pay windows [[starts, ends]]: [["06:20", "06:30"]]
# 06:15: Dx accepted order A  
# 06:18: Dx accepted order B  
# 06:19: Dx arrived at pick up location for A  
# 06:22: Dx picked up order A  
# 06:30: Dx arrived at pick up location for B  
# 06:33: Dx picked up order B  
# 06:36: Dx fulfilled order A  
# 06:45: Dx fulfilled order B

# Output: final pay: $18.0

# Explanation:
# 06:15 - 06:18 -> pay = $0.9
# 06:18 - 06:19 -> pay = 2 orders * 0.3 = $0.6
# 06:19 - 06:20 -> pay = $0.3
# 06:20 - 06:22 -> **peak pay** = 0.6 * 2 = $1.2
# 06:22 - 06:30 -> **peak pay** = 2 orders * 0.6 * 8= $9.6
# 06:30 - 06:33 -> pay = $0.9
# 06:33 - 06:36 -> pay = 2 orders * 0.3 * 3 = $1.8
# 06:36 - 06:45 -> pay = 0.3 * 9 = $2.7
"""