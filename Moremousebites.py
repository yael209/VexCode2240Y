#-----------------------------#
#
#
#       Module:     Mousebites.py
# 
#       Arthor:     Dipsa
# 
#       Created: 9/7/2024, 7:18:02 PM
#      
#       Description: AutoRunSequence
# 
# 
# --------------------------------#
# 
# Library Imports
from vex import *

#Brain should be defined by default

brain = Brain()
player = Controller()

if brain.sdcard.is_inserted(): # load up pizazz from the SD Card
    brain.screen.draw_image_from_file('PR.png',0,0)

# def display_message():
#     brain.screen.clear_screen()           # Clear the screen first
#     brain.screen.set_cursor(1, 1)         # Set the cursor to the top left
#     brain.screen.print("""He is dressed in a robe dipped in blood, 
#                        and his name is the Word of God.""") # Display the message

# Call the function to display the message
# display_message()

trackwidth = 12.25 # Farted's measurements
wheelbase = 10 # inches
wheeldiam = 2.75 # inches 
gearatio = 4/3
wheelcirc = wheeldiam * math.pi # inches/turns
robotcirc = wheelbase * math.pi # inches if brain.sdcard.is_inserted():# load up pizazz from the SD Card

# region brain ports
change = False
change = False
lefttop = Motor(Ports.PORT1,GearSetting.RATIO_6_1,True)
leftmid = Motor(Ports.PORT3,GearSetting.RATIO_6_1,True)
leftbak = Motor(Ports.PORT2,GearSetting.RATIO_6_1,True)
rigttop = Motor(Ports.PORT18,GearSetting.RATIO_6_1,False)
rigtmid = Motor(Ports.PORT4,GearSetting.RATIO_6_1,False)
rigtbak = Motor(Ports.PORT6,GearSetting.RATIO_6_1,False)
lefty = MotorGroup(leftbak,leftmid,lefttop) # all left movement motors
right = MotorGroup(rigtbak,rigtmid,rigttop) # all right movement motors
dtmots = MotorGroup(lefty,right) # all drivetrain motors in a single variable
house = Motor(Ports.PORT16,GearSetting.RATIO_18_1,True) #front intake motor. Control button L1
conveyor = Motor(Ports.PORT11,GearSetting.RATIO_6_1) #conveyor motor. Control button L1
lift = Motor(Ports.PORT10,GearSetting.RATIO_6_1,False) #lift motor. Contol button B for up / Down for down
arm = DigitalOut(brain.three_wire_port.a)  #Extend the piston arm. Control button Y
claw = DigitalOut(brain.three_wire_port.b) #Retrack the claw piston. Control button R1
houselift = DigitalOut(brain.three_wire_port.c) #Lift intake piston. Control button R2
Monkeypaw = DigitalOut(brain.three_wire_port.d) #Monkey Paw Button Up
Robotpull = DigitalOut(brain.three_wire_port.e) #Moves the robot up

def hold(button,lastState=0):
    """Halt thread until current state changes.

    Args:
        button (Button or Boolean): conditional to check
        lastState (Boolean): last state of same conditional
    """
    if compD == 1:
        lastState = button.pressing()
        while button.pressing() == lastState: wait(5) # wait for button change
    else:
        if button == lastState: return True # wait for state change
        else: return False

# region Base movement

def baseCont():
    lefty.spin(FORWARD) # Moves the left and right motors
    right.spin(FORWARD)
    while True: #allows the axis to move the robots
            lefty.set_velocity(player.axis3.position()+player.axis1.position(),PERCENT) 
            right.set_velocity(player.axis3.position()-player.axis1.position(),PERCENT)
            wait(5)







#endregion
#region Front intake

def mousego():
    house.spin(FORWARD) #Defines mousego as the motor moving

def mouseback():
      house.spin(REVERSE) #Defines mouseback as the motor moving in reverse


def mousestop(): #Defines mousestop as the motor being stopped and not moving
    house.stop()
    
def mouse():
      global Bites
Bites = player.buttonL2 
Bites.pressed(mousego) #Keybinds the action of pressing L2 to mousego
Bites.released(mousestop) #Keybinds the action of releasing L2 to mousestop

Vic = player.buttonL1 
Vic.pressed(mouseback) #Keybinds the action of pressing L2 to mouseback
Vic.released(mousestop) #Keybinds the action of releasing L1 to mousestop






#end region
#region Intake piston lift

def houseup():
      houselift.set(True) #defines houseup as extending the piston

def housedown():
       houselift.set(False) #defines housedown as retracting the piston

def housemove():
      global cane
cane = player.buttonR2 
cane.pressed(houseup)#Keybinds the action to trigger the piston
cane.released(housedown)





#end region
# region conveyor belt 

def conveyorgo():
     conveyor.spin(FORWARD) #Defines conveyorgo as moving the belt forward

def conveyorback():
      conveyor.spin(REVERSE) #Defines conveyor back as moving the belt backwards

def conveyorstop():
    conveyor.stop() #Defines conveyor stop as stopping the motor

def conveyorbelt():
        global peterpan
peterpan = player.buttonL2 
wendy = player.buttonL1 
wendy.pressed(conveyorback) #Keybinds pressing L1 to move the conveyor in reverse 
wendy.released(conveyorstop)
peterpan.pressed(conveyorgo) #Keybinds pressing L2 to move the conveyor forward
peterpan.released(conveyorstop)




#end region
#region Front and Conveyor

def Fullintake():
        global fullhouse
fullhouse = player.buttonL2 
fullhouse.pressed(mousego)(conveyorgo) #Keybinds pressing L2 to move both conveyor and intake at the same time
fullhouse.released(mousestop)(conveyorstop)













#end region
#region UppyPiston

def Buttonpair():
     player.buttonLeft.pressing()
     player.buttonUp.pressing()

def RobotLift():
    while True:
        while not Buttonpair:
            wait(5,MSEC)
        Robotpull.set(True)
        while Buttonpair():
            wait(5,MSEC)
        while not Buttonpair():
            wait(5,MSEC)
        Robotpull.set(False)
        while Buttonpair():
            wait(5,MSEC)






#region Conveyor lift

def liftdown():
    lift.spin(FORWARD) #Defines liftdown as moving the lift motor forward

def liftup():
    lift.spin(REVERSE) #Defines liftup as moving the lift motor in reverse

def liftdont():
    lift.stop() #Defines liftdont as the lift not moving

pinkman = player.buttonB 
pinkman.pressed(liftdown) #Keybinds the button to move lift down
pinkman.released(liftdont)

jesse = player.buttonDown 
jesse.pressed(liftup) #Keybinds the button to move the lift up
jesse.released(liftdont)






#end region
#region Claw Piston 

def Clawout():
      claw.set(True) #defines houseup as extending the piston

def Clawin():
       claw.set(False) #defines housedown as retracting the piston

def Clawmove():
      global cane
casa = player.buttonR1 
casa.pressed(Clawout)#Keybinds the action to trigger the piston
casa.released(Clawin)






#end region
#region arm extending piston

def extenderUp(): 
        arm.set(False) #Extends the piston
    
def extenderdown():
        arm.set(True) #Retrackts the piston

def extender():
      global extend
extend = player.buttonY #Keybinds the button to move the piston 
extend.pressed(extenderdown)
extend.released(extenderUp)









#end region
#region Mokey Paw

def Monkeyclaw():
    # wait(75,SECONDS)
    while True:
        while not player.buttonUp.pressing():
         wait(5,MSEC)
         Monkeypaw.set(False)
        while player.buttonUp.pressing():
            wait(5,MSEC)
        while not player.buttonUp.pressing():
            wait(5,MSEC)
            Monkeypaw.set(True)
        while player.buttonUp.pressing():
            wait(5,MSEC)


#end region







#region driver events


driver = Event()
def autoF(): # Threads the autonomous code, compliant with competitive requirements
    global compD
    compD = 1
    active = Thread(auton)
    while comp.is_enabled() and comp.is_autonomous(): wait(10) # waits until auton period ends
    active.stop()
def drivF(): # Threads driver period, compliant with competitive requirements
    global compD
    dtmots.set_stopping(COAST)
    compD = 1
    active = Thread(driver.broadcast)
    while comp.is_enabled() and comp.is_driver_control(): wait(10) # waits until driver period ends
    active.stop()

comp = Competition(drivF,autoF)







#end region
#region driver inputs

driver = Event()
#Made to do the function of movement 
driver(baseCont)
driver(mousego)
driver(mouseback)
driver(liftup)
driver(liftdown)
driver(conveyorgo)  
driver(liftdont)
driver(liftdont)
driver(conveyorstop)
driver(conveyorstop)
driver(mousestop)
driver(mousestop)
driver(liftdont)
driver(liftdont)
driver(conveyorstop)
driver(conveyorstop)
driver(mousestop)
driver(mousestop)
driver(Clawmove)
driver(Monkeyclaw)
driver(RobotLift)
driver(Buttonpair)

#end region 
#region Autonomous movement

def auton():    
    
    lefty.spin_for(FORWARD,5,TURNS)
    right.spin_for(FORWARD,5,TURNS)
    
    lefty.stop()
    right.stop()

   


#endregion

    
    
    
#motor speeds


lefty.set_velocity(100,PERCENT)
right.set_velocity(100,PERCENT)
house.set_velocity(100,PERCENT)
conveyor.set_velocity(100,PERCENT)
lift.set_velocity(100,PERCENT) 
