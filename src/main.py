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
IntakeF = Motor(Ports.PORT16,GearSetting.RATIO_18_1,True) #front intake motor. Control button L1
conveyor = Motor(Ports.PORT11,GearSetting.RATIO_6_1) #conveyor motor. Control button L1
lift = Motor(Ports.PORT10,GearSetting.RATIO_6_1,False) #lift motor. Contol button B for up / Down for down
arm = DigitalOut(brain.three_wire_port.a)  #Extend the piston arm. Control button Y
claw = DigitalOut(brain.three_wire_port.b) #Retrack the claw piston. Control button R1
IntakeLift = DigitalOut(brain.three_wire_port.c) #Lift intake piston. Control button R2
HooksM = DigitalOut(brain.three_wire_port.d) #Monkey Paw Button Up
Robotpull = DigitalOut(brain.three_wire_port.e) #Moves the robot up
Ringdetect = Optical(Ports.PORT20)
autonOpt = Distance(Ports.PORT15)
inertial_sensor = Inertial(Ports.PORT9) 

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
Blueloop = False
Redloop = False

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

def IntakeIn():
    IntakeF.spin(FORWARD) #Defines IntakeIn as the motor moving

def IntakeOut():
      IntakeF.spin(REVERSE) #Defines IntakeOut as the motor moving in reverse


def IntakeStop(): #Defines mousestop as the motor being stopped and not moving
        global IntakeStop
        IntakeF.stop()
    
def InatakeMove():
      global IntakeP
IntakeP = player.buttonL2 
IntakeP.pressed(IntakeIn) #Keybinds the action of pressing L2 to IntakeP
IntakeP.released(IntakeStop) #Keybinds the action of releasing L2 to IntakeStop

Vic = player.buttonL1 
Vic.pressed(IntakeOut) #Keybinds the action of pressing L2 to IntakeOut
Vic.released(IntakeStop) #Keybinds the action of releasing L1 to IntakeStop






#end region
#region Intake piston lift

def IntakeUp():
      IntakeLift.set(True) #defines IntakeUp as extending the piston

def IntakeDown():
       IntakeLift.set(False) #defines IntakeDown as retracting the piston

def Intakemove():
      global cane
cane = player.buttonR2 
cane.pressed(IntakeUp)#Keybinds the action to trigger the piston
cane.released(IntakeDown)





#end region
# region conveyor belt 

def conveyorgo():
     conveyor.spin(FORWARD) #Defines conveyorgo as moving the belt forward

def conveyorback():
      conveyor.spin(REVERSE) #Defines conveyor back as moving the belt backwards

def conveyorstop():
    global conveyorstop
    conveyor.stop() #Defines conveyor stop as stopping the motor

def conveyorbelt():
        global ConveyorP
ConveyorP = player.buttonL2 
ConveyorW = player.buttonL1 
ConveyorW.pressed(conveyorback) #Keybinds pressing L1 to move the conveyor in reverse 
ConveyorW.released(conveyorstop)
ConveyorP.pressed(conveyorgo) #Keybinds pressing L2 to move the conveyor forward
ConveyorP.released(conveyorstop)




#end region
#region Front and Conveyor

def Fullintake():
        global IntCov
IntCov = player.buttonL2 
IntCov.pressed(IntakeIn)(conveyorgo) #Keybinds pressing L2 to move both conveyor and intake at the same time
IntCov.released(IntakeStop)(conveyorstop)













#end region
#region UppyPiston

def RobotLift():
    while True:
        while not player.buttonLeft.pressing():
            wait(5,MSEC)
        Robotpull.set(True)
        while player.buttonLeft.pressing():
            wait(5,MSEC)
        while not player.buttonLeft.pressing():
            wait(5,MSEC)
        Robotpull.set(False)
        while player.buttonLeft.pressing():
            wait(5,MSEC)






#region Conveyor lift

def liftdown():
    lift.spin(FORWARD) #Defines liftdown as moving the lift motor forward

def liftup():
    lift.spin(REVERSE) #Defines liftup as moving the lift motor in reverse

def liftdont():
    global liftdont
    lift.stop() #Defines liftdont as the lift not moving

LiftP = player.buttonB 
LiftP.pressed(liftdown) #Keybinds the button to move lift down
LiftP.released(liftdont)

LiftJ = player.buttonDown 
LiftJ.pressed(liftup) #Keybinds the button to move the lift up
LiftJ.released(liftdont)






#end region
#region Claw Piston 

def Clawout():
      claw.set(True) #defines clawout as extending the piston

def Clawin():
       claw.set(False) #defines clawin as retracting the piston

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

def Hooks():
    # wait(75,SECONDS)
    while True:
        while not player.buttonUp.pressing():
         wait(5,MSEC)
         HooksM.set(False)
        while player.buttonUp.pressing():
            wait(5,MSEC)
        while not player.buttonUp.pressing():
            wait(5,MSEC)
            HooksM.set(True)
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
driver(IntakeIn)
driver(IntakeOut)
driver(liftup)
driver(liftdown)
driver(conveyorgo)  
driver(liftdont)
driver(conveyorstop)
driver(IntakeStop)
driver(Clawmove)
driver(Hooks)
driver(RobotLift)


#end region 
#region Autonomous movement
def disToMot(dis):
    return (dis / wheelcirc) * gearatio # if wrong change second operator to '*'
color = Ringdetect.color()
if color == Color.BLUE:
    Blueloop = True
    # Add any actions to perform when blue is detected
    # Check for red color
elif color == Color.RED:
    Redloop = True
    # Add any actions to perform when red is detected

    # Optionally handle other colors or no color
else:
    wait(1,MSEC)
 
def degToDis(deg):
    return (deg / 360) * robotcirc # makes a turn from degrees to inches
def calcArc(degs=0,dis=float(0)):
    val = 2*math.pi*dis*(degs/360)
    return disToMot(val)
def veldec(motor):
    retval = motor.velocity(PERCENT)    # save OG motor velocity
    if motor.count() > 3:               # check if we need to slow down whole base
        motor.set_velocity(motor.velocity()/3)          # change velocity to 1/3 its original value
    else: motor.set_velocity(motor.velocity() * 0.80)   # reduce velocity by 20%
    return retval           # return OG velocity, used if necessary
def autonDetect():
    if not autonOpt.installed(): return ""  # if sensor is disconnected, return empty
    if autonOpt.is_near_object():           # check if theres an object covering the sensor
        ret = "defen"                       # return to run offensive side auton
    else:
        ret = "offen"                       # return to run defesive side auton
    return ret                              # return our variable
def move(dis):
    dir = dis / abs(dis)            
    lefty.set_velocity(70 * dir,PERCENT)         # get direction, -1 for backwards or 1 for forwards
    right.set_velocity(70 * dir,PERCENT)   # set current velocity to a stable, precise velocity. multiplied by dir
    right.spin_for(FORWARD,disToMot(dis),TURNS,wait=False)
    lefty.spin_for(FORWARD,disToMot(dis),TURNS,wait=True) # spins motors using its encoders as reference
    wait(10)
def tmove(time):
    dir = time / abs(time)
    lefty.set_velocity(80 * dir,PERCENT)         # get direction, -1 for backwards or 1 for forwards
    right.set_velocity(80 * dir,PERCENT)   # set current velocity to a stable, precise velocity. multiplied by dir
    lefty.spin(FORWARD)
    right.spin(FORWARD)
    wait(abs(time),SECONDS)
    right.stop()
    lefty.stop()
def rtmove(time):
    dir = time / abs(time)
    lefty.set_velocity(80 * dir,PERCENT)         # get direction, -1 for backwards or 1 for forwards
    right.set_velocity(80 * dir,PERCENT)   # set current velocity to a stable, precise velocity. multiplied by dir
    lefty.spin(REVERSE)
    right.spin(REVERSE)
    wait(abs(time),SECONDS)
    right.stop()
    lefty.stop()
def turn(theta):
    dir = theta / abs(theta)                # get direction of turn
    dtmots.set_velocity(60 * dir,PERCENT)   # set velocity to a stable vel. dir determines direction
    amnt = degToDis(theta)                  # convert degrees to distance. x2 for radius
    turn = disToMot(amnt)                   # convert distance to motor turns
    right.spin_for(REVERSE,turn,TURNS,wait=False)
    lefty.spin_for(FORWARD,turn,TURNS,wait=True) # spins motors using its encoders as reference
def pturn(theta):
    dir = theta / abs(theta)
    dtmots.set_velocity(60,PERCENT)   # set velocity to a stable vel. dir determines direction
    amnt = degToDis(theta)*2                # convert degrees to distance
    turn = disToMot(amnt)                   # convert distrance to motor turns
    if dir > 0:
        right.spin_for(FORWARD,turn,TURNS,wait=True)   # start motors
    else:
        lefty.spin_for(FORWARD,turn,TURNS,wait=True)   # start motors
def rpturn(theta):
    dir = theta / abs(theta)
    dtmots.set_velocity(60,PERCENT)   # set velocity to a stable vel. dir determines direction
    amnt = degToDis(theta)*2                # convert degrees to distance
    turn = disToMot(amnt)                   # convert distrance to motor turns
    if dir > 0:
        right.spin_for(FORWARD,turn,TURNS,wait=True)   # start motors
    else:
        lefty.spin_for(FORWARD,turn,TURNS,wait=True)   # start motors
def aturn(theta=90,pivdis=float(5)):
    vel = 55
    dtmots.set_velocity(vel,PERCENT)
    if theta < 0:
        turnR = abs(calcArc(theta,pivdis+trackwidth))
        turnL = abs(calcArc(theta,pivdis))
        veL = vel * (turnL/turnR)
        veR = vel
    else:
        turnL = abs(calcArc(theta,pivdis+trackwidth))
        turnR = abs(calcArc(theta,pivdis))
        veL = vel
        veR = vel * (turnR/turnL)
    right.spin_for(FORWARD,turnR,TURNS,veR,PERCENT,False)
    lefty.spin_for(FORWARD,turnL,TURNS,veL,PERCENT,True)
    wait(5)
def raturn(theta=90,pivdis=float(5)):
    vel = 55
    dtmots.set_velocity(vel,PERCENT)
    if theta < 0:
        turnR = abs(calcArc(theta,pivdis+trackwidth))
        turnL = abs(calcArc(theta,pivdis))
        veL = vel * (turnL/turnR)
        veR = vel
    else:
        turnL = abs(calcArc(theta,pivdis+trackwidth))
        turnR = abs(calcArc(theta,pivdis))
        veL = vel
        veR = vel * (turnR/turnL)
    right.spin_for(REVERSE,turnR,TURNS,veR,PERCENT,False)
    lefty.spin_for(REVERSE,turnL,TURNS,veL,PERCENT,True)
    wait(5)
def auton():
    check = autonDetect()       # check which autonomous should be ran
    dtmots.set_stopping(COAST)  # set stopping to hold, should make everything more precise
    if check == "offen": # offensive side auton
        move(5)



    elif check == "defen":  # defensive side auton
    
        move(20)        


        
    else:                   # no auton; only used in emergencies
        dtmots.set_stopping(COAST)
        lefty.set_stopping(COAST)
        right.set_stopping(COAST)
        lift.spin(REVERSE)
        claw.set(True)
        move(-20)
        lift.stop()
        claw.set(False)
        conveyor.spin_for(FORWARD,4,TURNS,wait=False)
        turn(-90)
        move(-7)
        claw.set(True)
        wait(50,MSEC)
        move(6)
        wait(0.7,SECONDS)
        turn(150)
        wait(0.6,SECONDS)
        move(-31)
        claw.set(True)
        move(5)

        
        
        


    

        
   


#endregion

    
    
    
#motor speeds


lefty.set_velocity(100,PERCENT)
right.set_velocity(100,PERCENT)
IntakeF.set_velocity(100,PERCENT)
conveyor.set_velocity(100,PERCENT)
lift.set_velocity(100,PERCENT) 

# Main loop
if Blueloop:
    while True: 
        color = Ringdetect.color()
        if color == Color.RED:
            conveyor.spin_for(REVERSE,1,TURNS)
        else:
            wait(1,MSEC) 
if Redloop:
    while True: 
        color = Ringdetect.color()
        if color == Color.BLUE:
            conveyor.spin_for(REVERSE,1,TURNS)
        else:
            wait(1,MSEC)
        
    
             

        

