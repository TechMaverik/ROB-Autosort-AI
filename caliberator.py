from motion_planner import MotionPlanner
import time

planner = MotionPlanner()


def pick_and_raise():
    speed = 0.008
    planner.move_robot("LEFT", speed, 180)
    planner.move_robot("RIGHT", speed, 210)
    planner.move_robot("RIGHT", speed, 90)
    planner.move_robot("LEFT", speed, 90)


def move_base():
    speed = 0.001
    planner.move_robot("MID", speed, 0 * 5)
    planner.move_robot("MID", speed, -90 * 5)
    time.sleep(1)
    planner.move_robot("MID", speed, 90 * 5)
    time.sleep(1)
    planner.move_robot("MID", speed, 20 * 5)


move_base()
pick_and_raise()
