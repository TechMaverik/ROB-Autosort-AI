from motion_planner import MotionPlanner
import time

planner = MotionPlanner()


def pick_and_raise():
    speed = 0.01
    planner.move_robot("LEFT", speed, 240)
    # planner.move_robot("RIGHT", speed, 210) #raise
    # planner.move_robot("RIGHT", speed, 90)  #raise
    planner.move_robot("LEFT", speed, 90)


def move_base():
    speed = 0.01
    planner.move_robot("MID", speed, 0 * 5)
    planner.move_robot("MID", speed, -90 * 5)
    time.sleep(1)
    planner.move_robot("MID", speed, 90 * 5)
    time.sleep(1)
    planner.move_robot("MID", speed, 10 * 5)


def motor_test():
    move_base()
    pick_and_raise()


def picksim():
    speed = 0.009
    # for angle in range(-50, 90, 10):
    for angle in range(0, 40, 10):
        planner.move_robot("MID", speed, angle * 5)
        pick_and_raise()
    planner.move_robot("MID", speed, 20 * 5)


picksim()
