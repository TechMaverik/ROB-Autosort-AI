import time
import RPi.GPIO as GPIO

class MotionPlanner:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        self.software_position_feedback = {"MID": 90, "LEFT": 90, "RIGHT": 90}

    def step_to_angle_converter(self, diff_angle):
        if diff_angle < 0:
            diff_angle = -diff_angle
        steps = int(abs(diff_angle) * 200 / 360)
        return steps

    def move_robot(self, motorname, step_delay, angle):
        try:

            if motorname == "MID":
                mid_current_angle = self.software_position_feedback["MID"]
                self.software_position_feedback["MID"] = angle
                diff_angle = mid_current_angle - angle
                if diff_angle > 0:
                    direction = False
                else:
                    direction = True
                steps = self.step_to_angle_converter(diff_angle)
                GPIO.output(
                    24,
                    (GPIO.HIGH if direction else GPIO.LOW),
                )
                response_payload = {
                    "Directions": direction,
                    "Steps": steps,
                    "Position": self.software_position_feedback,
                }
                print(response_payload)
                for _ in range(steps):
                    GPIO.output(25, GPIO.HIGH)
                    time.sleep(step_delay)
                    GPIO.output(25, GPIO.LOW)
                    time.sleep(step_delay)

            if motorname == "LEFT":
                mid_current_angle = self.software_position_feedback["LEFT"]
                self.software_position_feedback["LEFT"] = angle
                diff_angle = mid_current_angle - angle
                if diff_angle > 0:
                    direction = False
                else:
                    direction = True
                steps = self.step_to_angle_converter(diff_angle)
                GPIO.output(
                    17,
                    (GPIO.HIGH if direction else GPIO.LOW),
                )
                response_payload = {
                    "Directions": direction,
                    "Steps": steps,
                    "Position": self.software_position_feedback,
                }
                print(response_payload)
                for _ in range(steps):
                    GPIO.output(18, GPIO.HIGH)
                    time.sleep(step_delay)
                    GPIO.output(18, GPIO.LOW)
                    time.sleep(step_delay)

            if motorname == "RIGHT":
                mid_current_angle = self.software_position_feedback["RIGHT"]
                self.software_position_feedback["RIGHT"] = angle
                diff_angle = mid_current_angle - angle
                print(diff_angle)
                if diff_angle > 0:
                    direction = False
                else:
                    direction = True
                steps = self.step_to_angle_converter(diff_angle)
                GPIO.output(
                    22,
                    (GPIO.HIGH if direction else GPIO.LOW),
                )
                response_payload = {
                    "Directions": direction,
                    "Steps": steps,
                    "Position": self.software_position_feedback,
                }
                print(response_payload)
                for _ in range(steps):
                    GPIO.output(23, GPIO.HIGH)
                    time.sleep(step_delay)
                    GPIO.output(23, GPIO.LOW)
                    time.sleep(step_delay)

        except KeyboardInterrupt:
            print("Interrupted by user. Cleaning up GPIO.")

    GPIO.cleanup()


# Example usage for rotating MID motor by 90 degrees CW, then CCW, etc.
# planner = MotionPlanner()


# planner.move_robot("MID", 0.01, 50)
# planner.move_robot("MID", 0.01, 90)
# planner.move_robot("MID", 0.01, 150)
# planner.move_robot("MID", 0.01, 90)

# planner.move_robot("LEFT", 0.01, 50)
# planner.move_robot("LEFT", 0.01, 90)
# planner.move_robot("LEFT", 0.01, 150)
# planner.move_robot("LEFT", 0.01, 90)

# planner.move_robot("RIGHT", 0.01, 70)
# planner.move_robot("RIGHT", 0.01, 90)
# planner.move_robot("RIGHT", 0.01, 120)
# planner.move_robot("RIGHT", 0.01, 90)
