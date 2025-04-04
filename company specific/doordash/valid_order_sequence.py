"""
Given a set list of pickups and deliveries for order, figure out if the given list is valid or not. A delivery cannot happen for an order before pickup.

Examples below:

[P1, P2, D1, D2]==>valid
[P1, D1, P2, D2]==>valid
[P1, D2, D1, P2]==>invalid
[P1, D2]==>invalid
[P1, P2]==>invalid
[P1, D1, D1]==>invalid
[]==>valid
[P1, P1, D1]==>invalid
[P1, P1, D1, D1]==>invalid
[P1, D1, P1]==>invalid
[P1, D1, P1, D1]==>invalid
Follow up: Find longest valid subarray

Ex 1: orders = ['P1', 'P1', 'D1'], return ['P1', 'D1']
Ex 2: orders = ['P1', 'P1', 'D1', 'D1'], return ['P1', 'D1']
"""