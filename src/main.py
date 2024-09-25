# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       yaelf                                                        #
# 	Created:      9/18/2024, 2:12:15 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import atexit
import bdb
import importlib

# Brain should be defined by default
brain=Brain()

     
vexcode_brain_precision = 0
vexcode_console_precision = 0
myVariable = 0
doctorcasa = 0

def onauton_autonomous_0():
    global myVariable, vexcode_brain_precision, vexcode_console_precision
    brain.screen.print("It's easier to assimilate, than explain.")

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )


# Down here will be the code to display