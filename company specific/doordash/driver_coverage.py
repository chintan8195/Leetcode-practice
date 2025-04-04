"""
Note this question is essentially https://leetcode.com/problems/count-sub-islands/description/

At DoorDash, we need to make sure that drivers are available at popular locations to deliver food. There are certain location clusters in a city that need drivers, and a driver can only cover certain location clusters. A location cluster is considered “covered” if the driver can deliver for the entire location cluster. How many location clusters are covered?

Provided:
driver_available_locations = {
{1,1,1,0,0},
{0,1,1,1,1},
{0,0,0,0,0],
{1,0,0,1,0],
{1,1,0,1,1}
}
drivers_needed_at = {
{1,1,1,0,0},
{0,0,1,1,1},
{0,1,0,0,0},
{1,0,1,1,0},
{0,1,0,1,0}
}

Return: Int indicating number of location cluster covered
3
"""