# ------------------------------ HEADER COMMENTS ------------------------------
# Program Name: Lugnuts Navigation
# Version: 1.0
# Author(s): Ephram Pope
# Description: This program controls the Lugnuts robot's movements using sensors and motors for mission tasks.
# Robot: Spike Prime Robot
# Competition/Task: FLL Mission Task 2025

# --------------------------- IMPORT STATEMENTS ------------------------------
from hub import port, motion_sensor
import runloop
import motor_pair
import math

# -------------------------- GLOBAL CONSTANTS ---------------------------------
# Robot Configuration
RIGHT_ATTACHMENT_MOTOR_PORT = port.A
LEFT_ATTACHMENT_MOTOR_PORT = port.B
RIGHT_DRIVE_MOTOR_PORT = port.C
LEFT_DRIVE_MOTOR_PORT = port.D

# Wheel and robot measurements
WHEEL_DIAMETER_CM = 5.6 # Diameter of the large wheel in centimeters
AXLE_TRACK_CM = 12.0    # Distance between the two wheels in centimeters

# Speed Settings
DEFAULT_SPEED = 600    # 60% of max speed for medium motors (600 degrees/sec)
TURN_SPEED = 400       # Speed during turns
RATE = 500             # rate of acceleration or deceleration

# --------------------------- INITIALIZATION ----------------------------------
# Pair the motors for coordinated movement
motor_pair.pair(motor_pair.PAIR_1, RIGHT_DRIVE_MOTOR_PORT, LEFT_DRIVE_MOTOR_PORT)

# ------------------------- HELPER FUNCTIONS ----------------------------------

async def move_forward(speed, distance):
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, distance, 0, velocity=speed, acceleration=RATE, deceleration=RATE)


async def left_pivot_turn(degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees,0, DEFAULT_SPEED, acceleration=RATE, deceleration=RATE)

async def right_pivot_turn(degrees):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degrees, DEFAULT_SPEED,0, acceleration=RATE, deceleration=RATE)


# ------------------------- MISSION-SPECIFIC LOGIC ----------------------------

async def mission_1():
    await move_forward(DEFAULT_SPEED,1539)
    await left_pivot_turn(400) 
    await move_forward(DEFAULT_SPEED,1018)

async def mission_2():
    """Mission 2: """
    await move_forward(DEFAULT_SPEED,200)
    await left_pivot_turn(100)
    await right_pivot_turn(100)
    await left_pivot_turn(100)
    await move_forward(DEFAULT_SPEED,2000)
    await right_pivot_turn(300)
    await move_forward(DEFAULT_SPEED,400)
    await move_forward(DEFAULT_SPEED,200)
    await left_pivot_turn(100)
    await right_pivot_turn(100)
    await left_pivot_turn(100)
    await move_forward(DEFAULT_SPEED,2000)
    await right_pivot_turn(300)
    await move_forward(DEFAULT_SPEED,400)
    await left_pivot_turn(300)
    await move_forward(DEFAULT_SPEED,9889)
    
async def mission_3():
    await move_forward(DEFAULT_SPEED,1000)
    await left_pivot_turn(300)
    await right_pivot_turn(300)    
    
# ------------------------- MAIN PROGRAM STRUCTURE ----------------------------

async def main():
    """Main program execution."""
    await mission_3()
    raise SystemExit

# ---------------------------- Start The Loop --------------------------------
runloop.run(main())
