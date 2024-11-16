from controller import Robot 
TIME_STEP = 64 
MAX_SPEED = 6.28 
robot = Robot() 
prox_sensor = [] 
sensor_names = ["ps0", "ps1", "ps2", "ps3", "ps4", "ps5", "ps6", "ps7"] 
for name in sensor_names: 
    sensor = robot.getDevice(name) 
    sensor.enable(TIME_STEP) 
    prox_sensor.append(sensor) 
left_motor = robot.getDevice("left wheel motor") 
right_motor = robot.getDevice("right wheel motor") 
left_motor.setPosition(float('inf')) 
right_motor.setPosition(float('inf')) 
left_motor.setVelocity(0.0) 
right_motor.setVelocity(0.0) 
FRONT_THRESHOLD = 150.0 
SIDE_THRESHOLD = 80.0 
TURN_THRESHOLD = 100.0 
while robot.step(TIME_STEP) != -1: 
    front = prox_sensor[0].getValue() 
    front_right = prox_sensor[1].getValue() 
    front_left = prox_sensor[6].getValue() 
    left_side = prox_sensor[7].getValue() 
    left_speed = 0.5 * MAX_SPEED 
    right_speed = 0.5 * MAX_SPEED 
    if front > FRONT_THRESHOLD or front_left > FRONT_THRESHOLD: 
        left_speed = 0.5 * MAX_SPEED 
        right_speed = -0.2 * MAX_SPEED 
    elif left_side < SIDE_THRESHOLD: 
        left_speed = 0.3 * MAX_SPEED 
        right_speed = 0.5 * MAX_SPEED 
    elif front_right > TURN_THRESHOLD: 
        left_speed = -0.2 * MAX_SPEED 
        right_speed = 0.5 * MAX_SPEED 
    else: 
        left_speed = 0.5 * MAX_SPEED 
        right_speed = 0.5 * MAX_SPEED 
    left_motor.setVelocity(left_speed) 
    right_motor.setVelocity(right_speed)
