"""
The chef processes the eligible orders one at a time and deletes the orderId processed from the array. In a given array of orders, an eligible orderId is the orderId that is greater than its immediate left neighbor and Immediate right neighbor. For the first element in the array, it is eligible if it is greater than its right neighbor; for the last element it should only be greater than its left neighbor. If there are more than 1 eligible orderid then chef processes the order with smaller orderid. Return sequence of processing the order.

Eg.

Initial OrderIds = [3,1,5,4,2]

In first iteration 3 and 5 both eligible so take 3 Order processed: 3 After processing the order 3 array would look like remaining orders would be [1,5,4,2]

After 2nd iteration In second iteration only 5 is eligible so Order processed: 5 Array would [1,4,2]

After 3rd iteration Only 4 is eligible Order processed:4 Array would be[1,2]

After 4th iteration Only eligible item is 2 Order processed:2 Array would be [1]

Finally array would be [1] Order processed: 1

So ans 3,5,4,2,1

Interviwer was looking for O(n) solution.
"""