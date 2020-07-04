from random import random

'''
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
'''


class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array =[]
        self.map = {}
         

    def insert(self, val: int):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        self.map[val]= len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.map:
            last, i = self.array[-1], self.map[val]
            self.array[i], self.map[last] = last, i
            self.array.pop()
            self.map.pop(val,0)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return self.array[random.randint(0,len(self.array)-1)]