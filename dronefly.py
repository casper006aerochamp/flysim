#!/usr/bin/env python

#importing time module
import time
#importing flytbase API
from flyt_python import api

#creating instance of drone navigation from api
drone = api.navigation(timeout=10000)

# waiting to initialize
time.sleep(5)

#taking off to the specified altitude
print ('Commencing Takeoff')
drone.take_off(5.0)
print ('Target Altitude Reached')

time.sleep(1)

print('Commencing Mission')

#logic to follow square pattern of side length 6.5 m | commands will be executed synchronously

drone.position_set(6.5, 0, 0, relative=True) # +x to move 6.5 m in forward direction | relative to the current position
print('Reached Waypoint 1')

drone.position_set(0, 6.5, 0, relative=True) # +y to move 6.5 m in right direction | relative to the current position
print('Reached Waypoint 2')

drone.position_set(-6.5, 0, 0, relative=True) # -x to move 6.5 m in backwards direction | relative to the current position
print('Reached Waypoint 3')

drone.position_set(0, -6.5, 0, relative=True) # -y to move 6.5 m in left direction | relative to the current position
print('Reached Final Waypoint')

#landing on the initial point asynchronously
print('Drone Landing')
drone.land(async=False)
print('Drone landed Successfully')
print('Mission Accomplished')
# shutting down drone
drone.disconnect()
