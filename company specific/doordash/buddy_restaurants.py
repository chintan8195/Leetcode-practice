"""
DoorDash obtains restaurant data from various sources which have varying quality. 
These sources often have duplicate merchants with minor typos in their names. 
The assignment is to create a list of unique restaurants across various sources ignoring the errors before onboarding them.
Definition: Similar restaurants
Two restaurants R1 and R2 are similar if we can swap a maximum of two letters (in different positions) of R1, so that it equals R2.
For example, source one may have a restaurant named "omega grill" while another source may have the same restaurant as "omgea grill".
For example, "biryani" and "briyani" are similar (swapping at positions 1 and 2). "biryani" is not similar to following, "biryeni" (no e to swap with), "briynai"(Needs 2 swap)
For a given restaurant name, find and return all the similar restaurant names in the list.
Implement the function below:
public List findSimilarRestaurants(String name, String[] list) {}
"""


"""
edge cases:

What about non matching cases
Same alphabets are supposed to be swapped?
"""


#Tests

from typing import List

from collections import Counter, defaultdict, deque

def findSimilarRestaurants(name, restaurant_list) -> List[str]:
    def are_similar(str1, str2):
   
        """
        Check if name1 and name2 are similar.
        Two names are similar if they are identical or if swapping exactly two letters in name1
        results in name2.
        """
        if len(str1) != len(str2):
            return False     

       # Find differing positions
        diff_positions = []
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff_positions.append(i)
                
        # More than 2 differences can't be similar
        if len(diff_positions) > 2 or len(diff_positions) == 1:
            return False
            
        # If no differences, they're same (not similar by definition)
        if len(diff_positions) == 0:
            return True
            
        # If exactly 2 differences, check if swapping works
        if len(diff_positions) == 2:
            i, j = diff_positions
            return str1[i] == str2[j] and str1[j] == str2[i]
            
        return False    
    
    result = []
    for candidate in restaurant_list:
        if are_similar(name, candidate):
            result.append(candidate)
    return result

input = "hotpot"
list = ["hottop", "hotopt", "hotpit", "httoop", "hptoot"]
print("Expected:")
print(["hottop", "hotopt", "hptoot"])
print("Got:")
print(findSimilarRestaurants(input, list))

input = "biryani"
list = ["biryani", "biryeni", "biriyani", "biriany", "briynai"]
print("Got:")
print(findSimilarRestaurants(input, list))
print("Expected:")
print(["biryani", "biriany"])

input = "omega grill"
list = ["omeag grill", "omeea grill", "omega gril", "omegla gril"]
print("Got:")
print(findSimilarRestaurants(input, list))
print("Expected:")
print(["omeag grill"])

"""
Given a restaurant name, find other restaurants in the list that are k-anagrams with each other. 
A name is a k-anagram with another name if both the conditions below are true:
- The names contain the same number of characters.
- The names can be turned into anagrams by changing at most k characters in the string
For example:
name = "grammar", k = 3, and list = ["anagram"], 
"grammar" is k-anagram with "anagram" since they contain the same number of characters and you can change 'r' to 'n' and 'm' to 'a'.
name = "omega grill", k = 2 and list = ["jmegra frill"], "omega grill" is k-anagram with "jmega frill" 
since they contain same number of characters and you can change 'o' to 'j' and 'g' to 'f'



def printfindKAnagrams(input, list, K) -> List[str]:
    result = []
    return result

input = "anagram"
list = ["grammar", "grammer", "anagram"]
K = 2
printfindKAnagrams(input, list, K)
print(["grammar", "anagram"])

input = "anagram"
list = ["grammar"]
K = 3
printfindKAnagrams(input, list, K)
print(["grammar"])

input = "anagram"
list = ["grammar"]
K = 1
printfindKAnagrams(input, list, K)
print([])

input = "omexyb grillg"
list = ["omgxca grille"]
K = 2
printfindKAnagrams(input, list, K)
print(["omgxca grille"])"
"""