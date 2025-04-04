"""
Find Available Deliveries
At DoorDash, many deliveries are scheduled well in advance. To improve our assignment rate, we want to enable dashers to claim these scheduled deliveries early. However, we noticed that certain dashers perform better, and want to reward them with a better selection. As a simple solution, we will introduce open windows for when deliveries will appear for a particular dasher. Below are the following requirements.

deliveries scheduled two days or further into the future should never be available
high tier dashers can see all of next day deliveries if the current time is 18:00 or later
all dashers can see all of next day deliveries if the current time is 19:00 or later
all dashers can see same day deliveries anytime
from datetime import datetime, timedelta

def get_available_deliveries(dasher, deliveries, current_time):
# TODO: implement.
return []

class Delivery(object):
def init(self, idx, pickup_time, store_id):
self.id = idx
self.pickup_time = pickup_time
self.store_id = store_id

class Dasher(object):
def init(self, idx, tier):
self.id = idx
self.tier = tier # 'low', 'high'

Sample test.
today = datetime(2021, 1, 15)
dasher = Dasher('dasher', 'low')
deliveries = [
Delivery('1', today + timedelta(hours=10), 'store_1'),
Delivery('2', today + timedelta(hours=30), 'store_1')
]
available_deliveries = get_available_deliveries(
dasher=dasher,
deliveries=deliveries,
current_time=today + timedelta(hours=18)
)
print([d.id for d in available_deliveries]) # Should include delivery 1.

"""