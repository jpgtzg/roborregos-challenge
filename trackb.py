from systems.chassis import Chassis
from systems.infrareds import Infrareds
from actions.line_follower import LineFollower
from lib.actions.action_scheduler import ActionScheduler

# WORKING :) 
def init_line_action(chassis_system: Chassis, infrared : Infrareds):

    line_follower = LineFollower(chassis_system, infrared)
    
    ActionScheduler().schedule_action(line_follower)