def asteroidCollision(asteroids):
    result = []
    if asteroids is None or len(asteroids)==0:
        return result
    for asteroid in asteroids:
        if asteroid > 0: 
            result.append(asteroid)
        else:
            while result and result[-1]>0 and result[-1]<abs(asteroid):
                result.pop()
            if not result or result[-1] < 0:
                result.append(asteroid)
            elif result[-1] == -asteroid:
                result.pop()
    return result