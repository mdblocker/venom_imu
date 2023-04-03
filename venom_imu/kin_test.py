# KINEMATIC CONFIGURATION FILE
# Set up PWM channels, and define servo locations. 
##################################################
from adafruit_servokit import ServoKit
import adafruit_pca9685
import board
import busio
import time
#--------------------------------------

i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

# PWM setup
kit0 = ServoKit(channels=16, address=0x40, frequency=50)
kit1 = ServoKit(channels=16, address=0x41, frequency=50)

# SERVO VARIABLES/
# Hips
servo_1h = kit0.servo[0]
servo_2h = kit0.servo[4]
servo_3h = kit0.servo[12]
servo_4h = kit1.servo[0]
servo_5h = kit1.servo[8]
servo_6h = kit1.servo[12]
# Knees
servo_1k = kit0.servo[1]
servo_2k = kit0.servo[5]
servo_3k = kit0.servo[13]
servo_4k = kit1.servo[1]
servo_5k = kit1.servo[9]
servo_6k = kit1.servo[13]
# Ankles
servo_1a = kit0.servo[2]
servo_2a = kit0.servo[6]
servo_3a = kit0.servo[14]
servo_4a = kit1.servo[2]
servo_5a = kit1.servo[10]
servo_6a = kit1.servo[14]

# Other 
# head in up/down direction (yes movement)
servo_no = kit0.servo[11]
servo_yes = kit1.servo[4]

# Leg Definitions
def L1(hip_angle, knee_angle, ankle_angle):
    # Right Back leg (1)
    servo_1h.angle = hip_angle
    servo_1k.angle = knee_angle
    servo_1a.angle = ankle_angle

def L2(hip_angle, knee_angle, ankle_angle):
    # Right Middle leg (2)
    servo_2h.angle = hip_angle
    servo_2k.angle = knee_angle
    servo_2a.angle = ankle_angle

def L3(hip_angle, knee_angle, ankle_angle):
    # Right Front leg (3)
    servo_3h.angle = hip_angle
    servo_3k.angle = knee_angle
    servo_3a.angle = ankle_angle

def L4(hip_angle, knee_angle, ankle_angle):
    # Left Front leg (4)
    servo_4h.angle = 180-hip_angle
    servo_4k.angle = 180-knee_angle
    servo_4a.angle = 180-ankle_angle

def L5(hip_angle, knee_angle, ankle_angle):
    # Left Middle leg (5)
    servo_5h.angle = 180-hip_angle
    servo_5k.angle = 180-knee_angle
    servo_5a.angle = 180-ankle_angle

def L6(hip_angle, knee_angle, ankle_angle):
    # Left Back leg (6)
    servo_6h.angle = 180-hip_angle
    servo_6k.angle = 180-knee_angle
    servo_6a.angle = 180-ankle_angle

# others

def goozle_noangle(neck_angle):
    servo_no.angle = neck_angle

def goozle_yesangle(neck_angle):
    servo_yes.angle = neck_angle


goozle_noangle(0)
time.sleep(1)
goozle_noangle(90)
time.sleep(1)
goozle_noangle(180)
time.sleep(1)

goozle_yesangle(0)
time.sleep(1)
goozle_yesangle(90)
time.sleep(1)
goozle_yesangle(180)
time.sleep(1)
