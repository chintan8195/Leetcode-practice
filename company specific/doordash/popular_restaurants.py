"""
Given a list of restaurant IDs where each ID represents an order placed at that restaurant, find the k most ordered-from restaurants.

function findTopKRestaurants(orders: string[], k: number): string[];
Input:

orders: Array of restaurant IDs, where each occurrence represents one order
k: Number of top restaurants to return
Example:

// Order history
const orders = ['100', '100', '2', '2', '1', '10'];
const k = 2;

findTopKRestaurants(orders, k);  
// Returns: ['100', '2']
// Because:
// Restaurant '100' had 2 orders
// Restaurant '2' had 2 orders
// Restaurant '1' had 1 order
// Restaurant '10' had 1 order
"""