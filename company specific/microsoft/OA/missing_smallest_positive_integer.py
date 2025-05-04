def smallest_missing_positive(A, B):
    mandatory = set()
    possible = set()
    
    for a, b in zip(A, B):
        if a == b:
            mandatory.add(a)
        possible.add(a)
        possible.add(b)
    
    # The answer is either:
    # 1. The smallest positive not in 'possible' (if no mandatory numbers force inclusion)
    # 2. The smallest positive not in 'mandatory' (but must check if it's avoidable in C)
    
    # First, find the smallest positive missing from 'possible' (trivial upper bound)
    missing = 1
    while missing in possible:
        missing += 1
    
        # Now, check if we can construct a C where 'missing' is missing
        # If 'missing' is not in 'mandatory', then we can avoid it
        if missing not in mandatory:
            return missing
    
    # Otherwise, find the next smallest positive not in 'possible'
    missing += 1
    while missing in possible:
        missing += 1
    return missing

A = [3, 2, 1, 6, 5]
B = [4, 2, 1, 3, 3]

print(smallest_missing_positive(A,B))