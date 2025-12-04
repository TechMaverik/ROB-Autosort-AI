import cv2
import numpy as np
import servo_operations
from motion_planner import MotionPlanner


cube_coordinates_image = []
cube_color_image = []
planner = MotionPlanner()


def pick_and_raise():
    speed = 0.01
    servo_operations.set_angle(90)
    planner.move_robot("LEFT", speed, 240)
    servo_operations.set_angle(20)
    planner.move_robot("LEFT", speed, 90)
    # servo_operations.set_angle(90)


def drop():
    servo_operations.set_angle(90)


def find_centroid(mask):
    M = cv2.moments(mask)
    if M["m00"] > 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        return (cx, cy)
    return None


def identify_cubes():
    color_ranges = {
        "Yellow": ([20, 100, 100], [30, 255, 255], [0, 255, 255]),
        # "Green": ([40, 70, 70], [80, 255, 255], [0, 255, 0]),
        "Red": ([170, 70, 70], [180, 255, 255], [0, 0, 255]),
        # "Blue": ([90, 70, 70], [130, 255, 255], [255, 0, 0]),
    }
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera not found")
        exit()
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Failed to capture image")
        exit()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    for color, (lower, upper, bgr) in color_ranges.items():
        lower = np.array(lower)
        upper = np.array(upper)

        mask = cv2.inRange(hsv, lower, upper)
        center = find_centroid(mask)
        cube_coordinates_image.append(center)
        cube_color_image.append(color)

        if center is not None:
            cv2.circle(frame, center, 8, bgr, -1)
            cv2.putText(
                frame,
                f"{color}: {center}",
                (center[0] + 10, center[1]),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                bgr,
                2,
            )
    cv2.imwrite("identified_blocks.jpg", frame)
    color_cube_map = dict(zip(cube_color_image, cube_coordinates_image))
    return color_cube_map


def check_position(coordinate, color):
    print("DEBUG--->", coordinate)
    x = 100
    x2 = 300
    x3 = 400
    x4 = 630
    speed = 0.009
    try:
        if color == "Green":
            if coordinate is not None:
                if coordinate[0] < x:
                    planner.move_robot("MID", speed, 0 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -40 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)

                    return "p1"
                elif x <= coordinate[0] < x2:
                    planner.move_robot("MID", speed, 10 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -40 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p2"
                elif x2 <= coordinate[0] < x3:  # Center
                    planner.move_robot("MID", speed, 20 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -40 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p3"
                elif x3 <= coordinate[0] < x4:
                    planner.move_robot("MID", speed, 30 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -40 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p4"
                elif coordinate[0] > x4:
                    planner.move_robot("MID", speed, 40 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -40 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p5"
                else:
                    return "Outside Camera Range"

        if color == "Yellow":
            if coordinate is not None:
                if coordinate[0] < x:
                    planner.move_robot("MID", speed, 0 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -60 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)

                    return "p1"
                elif x <= coordinate[0] < x2:
                    planner.move_robot("MID", speed, 10 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -60 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p2"
                elif x2 <= coordinate[0] < x3:  # Center
                    planner.move_robot("MID", speed, 20 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -40 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p3"
                elif x3 <= coordinate[0] < x4:
                    planner.move_robot("MID", speed, 30 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -60 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p4"
                elif coordinate[0] > x4:
                    planner.move_robot("MID", speed, 40 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, -60 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p5"
                else:
                    return "Outside Camera Range"

        if color == "Red":
            if coordinate is not None:
                if coordinate[0] < x:
                    planner.move_robot("MID", speed, 0 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, 90 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)

                    return "p1"
                elif x <= coordinate[0] < x2:
                    planner.move_robot("MID", speed, 10 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, 90 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p2"
                elif x2 <= coordinate[0] < x3:  # Center
                    planner.move_robot("MID", speed, 20 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, 90 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p3"
                elif x3 <= coordinate[0] < x4:
                    planner.move_robot("MID", speed, 30 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, 90 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p4"
                elif coordinate[0] > x4:
                    planner.move_robot("MID", speed, 40 * 5)
                    pick_and_raise()
                    planner.move_robot("MID", speed, 90 * 5)
                    drop()
                    planner.move_robot("MID", speed, 20 * 5)
                    return "p5"
                else:
                    return "Outside Camera Range"
    except:
        pass


while True:
    color_cube_map = identify_cubes()
    for color in color_cube_map:
        print(color_cube_map[color])
        robot_arm_map = check_position(color_cube_map[color], color)
        print(robot_arm_map)
        cube_coordinates_image.clear()
        cube_color_image.clear()
