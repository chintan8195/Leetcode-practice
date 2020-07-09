def getLastMoment(self, n: int, left: List[int], right: List[int]):
    if not left:
        return len(right)
    if not right:
        return len(left)
    units = 0
    for val in left:
        units = max(units,val)
    for val in right:
        units = max(units,n-val)
    return units
    
