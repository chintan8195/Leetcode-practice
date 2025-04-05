'''
 station A = [San Jose, Sunnyvale]
 station B = [Mountain View, Cupertino]
 station C = [San Mateo, San Francisco]
 origin = Mountain View, destination = San Mateo, distance = BC
 origin = San Jose, destination = San Mateo, distance = ABC
 origin = Mountain View, destination = Cupertino, distance = BC/AB
 
'''

def minimum_trainstops(stationA, stationB, stationC, origin, destination):
    return 