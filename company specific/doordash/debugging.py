"""
Order Assignment
I was given a piece of code which put a bunch of dashers in a map, then randomly picked a dasher and then adjusted the map so that there were no "gaps" in the map and the next pick could be made correctly. There were a couple of major bugs in the code (map wasn't initialized, the map size was not being taken into account after removing the picked dasher), which I was able to figure out and fix. I was allowed to run the code multiple times to zero in on the issues. I am now realizing that maybe one of the fixes I could have suggested was using a List instead of a Map since the indexing/adjustment would have been easier with a list.

Load Balancer
Load balancer round robin (there are around 3 bugs, one is the round robin implementation is wrong, and the test case has a bug). Followup is implementing consistent hashing.
"""