#  RigidBody_Xbox.py
#  
#  Copyright 2015 Rouglunge <https://www.youtube.com/channel/UCbhB_eggdTYjn4oey7wK-Gg>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


# The comments on this script have be written in a way that new scripters can understand
# This script allows an object with 'Rigid Body' physics to be controlled with an Xbox 360 Controller


## -Start- ##
# This checks what OS the scipt is running on;
# The function 'onWindows' will return positive if the script is running on Windows OS
os = 'Windows'

from sys import platform

if platform != "win32":
 os = 'Linux'

def onWindows():

 return os == 'Windows'

## -End- ##


import bge
import GameLogic

# This number will be used to lower the output value of the Xbox Controller 
reduction = 400000

# This is the lowest value the Xbox Controller can output and still trigger an event 
axisTh = 0.03 


## -Start- ##
##These two variables call Blender game logic

# 'cont' is the Controller logic brick that uses this script 
cont = GameLogic.getCurrentController() 

# 'obj' references objects in the current Scene - This allows selected objects to be manipulated by the script - 
obj = bge.logic.getCurrentScene().objects

## -End- ##


# These two are the Sensor logic bricks connected to the python Controller 
# Example - sensor1 = cont.sensors["SensorName"] - 
aXis = cont.sensors["Axis"]
bUtt = cont.sensors["Butt"]


## -Start- ##
##These variables are the axises and buttons on the Xbox Controller
# 'onW' is the Windows OS test
# The test is done with - button_or_axis = Windows_Value if onW else (=) Linux_Value -
# This test is need because the values for the buttons and axises are different on Windows and Linux
onW = onWindows()

# These are the numerical values associated with the axises on the Xbox Controller 
# Called with - SensorName.axisValues[axisnumber] - 
# A joystick sensor logic brick (with the 'Axis' Event Type; 'All Events' selected; and 'True Pulse' enabled) must be connected to the Python Controller logic brick to call these axises 


# left and right on the left thumb stick = 0 on Linux and Windows;
lar_lts = 0
# up and down on the left thumb stick = 1 on Linux and Windows;
uad_lts = 1
# left trigger = 2 on Linux, but = 4 on Windows;
lt = 4 if onW else 2
# left and right on the right thumb stick = 3 on Linux, but = 2 on Windows;
lar_rts = 2 if onW else 3
# up and down on the right thumb stick = 4 on Linux, but = 3 on Windows;
uad_rts = 3 if onW else 4
# right trigger = 5 on Linux and Windows
rt = 5


# These are the numerical values associated with the buttons on the Xbox Controller 
# Called with - SensorName.getButtonStatus(buttonnumber) - 
# A joystick sensor logic brick (with the 'Button' Event Type; 'All Events' selected; and 'Tap' enabled) must be connected to the Python Controller logic brick to call these buttons 

# a button = 0 on Linux, but = 10 on Windows;
a_but = 10 if onW else 0
# b button = 1 on Linux, but = 11 on Windows;
b_but = 11 if onW else 1
# x button = 2 on Linux, but = 12 on Windows;
x_but = 12 if onW else 2
# y button = 3 on Linux, but = 13 on Windows;
y_but = 13 if onW else 3
# left bumper = 4 on Linux, but = 8 on Windows;
l_bump = 8 if onW else 4
# right bumper = 5 on Linux, but = 9 on Windows;
r_bump = 9 if onW else 5
# back button = 6 on Linux, but = 5 on Windows;
bk_but = 5 if onW else 6
# start button = 7 on Linux, but = 4 on Windows;
st_but = 4 if onW else 7
# Xbox button = 8 on Linux, but = 14 on Windows;
xb_but = 14 if onW else 8
# left thumb stick pressed = 9 on Linux, but = 6 on Windows;
lts_pr = 6 if onW else 9
# right thumb stick pressed = 10 on Linux, but = 7 on Windows;
rts_pr = 7 if onW else 10
# left dpad button = 11 on Linux, but = 2 on Windows;
l_dp = 2 if onW else 11
# right dpad button = 12 on Linux, but = 3 on Windows;
r_dp = 3 if onW else 12
# up dpad button = 13 on Linux, but = 0 on Windows;
u_dp = 0 if onW else 13
# down dpad button = 14 on Linux, but = 1 on Windows
d_dp = 1 if onW else 14

lLR = aXis.axisValues[lar_lts] / reduction
lUD = aXis.axisValues[uad_lts] / reduction
rLR = aXis.axisValues[lar_rts] / reduction
rUD = aXis.axisValues[uad_rts] / reduction
lTrig = aXis.axisValues[lt] / reduction
rTrig = aXis.axisValues[rt] / reduction
aBut = bUtt.getButtonStatus(a_but)
bBut = bUtt.getButtonStatus(b_but)
xBut = bUtt.getButtonStatus(x_but)
yBut = bUtt.getButtonStatus(y_but)
lBump = bUtt.getButtonStatus(l_bump)
rBump = bUtt.getButtonStatus(r_bump)
bkBut = bUtt.getButtonStatus(bk_but)
stBut = bUtt.getButtonStatus(st_but)
xbBut = bUtt.getButtonStatus(xb_but)
ltsBut = bUtt.getButtonStatus(lts_pr)
rtsBut = bUtt.getButtonStatus(rts_pr)
ldPad = bUtt.getButtonStatus(l_dp)
rdPad = bUtt.getButtonStatus(r_dp)
udPad = bUtt.getButtonStatus(u_dp)
ddPad = bUtt.getButtonStatus(d_dp)

## -End- ##

# This is the object that is going to be manipulated 
# Using the 'obj' variable, the object 'Player' is called 
playObj = obj['Player']


# These are the directions the character will move or face in 
# Example - [x axis, y axis, z axis] - #
# 'motion' is the direction and speed the character will move at. The x and y axises have been set to the output from the left thumb stick 
# 'facing' is the direction and speed the character will rotate at. The z axis has been set to the output from the right thumb stick 
# 'jump' is the amount the character will jump  
motion = [lUD, lLR, 0.0]
facing = [0.0, 0.0, -rLR]
jump = [0.0, 0.0, 0.1]

# This function is activated if there is no input from the controller 
# It is used to stop the character from moving when the controller is not in use
# Only the axises and buttons in use need to be checked
# Axises are checked with - abs(axisnumber) < axisTh -
# Buttons are checked with - buttonnumber == False -
def cutOff():
    
 if (abs(lLR) < axisTh 
     and abs(lUD) < axisTh 
     and abs(rLR) < axisTh 
     and abs(rUD) < axisTh
     and aBut == False):
         
  return True


  
# This funtion allows the character to move
# If the output value from the left thumb stick is greater than the axis threshold, the character will move 
# abs(axisnumber) is used because the thumb sticks have a negative and positive state, depending on the direction they are pushed 
# How it works - character.applyMovement([x axis, y axis, z axis], local(True) or global(False) movement) - 
# Example - playObj.applyMovement(motion, True) - 
def movement():
    
 if abs(lLR) > axisTh or abs(lUD) > axisTh:
  playObj.applyMovement(motion, True)
  
  
# This function allows the character to rotate 
# If the output value from the right thumb stick is greater than the axis threshold, the character will rotate 
# How it works - character.applyRotation([x axis, y axis, z axis], local(True) or global(False) rotation) - 
# Example - playObj.applyRotation(facing, True) - 
def rotation():
    
 if abs(rLR) > axisTh:
  playObj.applyRotation(facing, True)
  
  
# This function allows the character to jump 
# If the a button is positive (pressed down) the character will jump 
def jumping():
    
 if aBut:
   playObj.applyMovement(jump, False)
  
  
# This is the main function, it calls all the other function in the script 
# The first thing that is checked, is if there is any input from the controller;
# If there is not, the other function will not be run 
def main():
    
 if cutOff():
  return
    
 else:
  movement()
  rotation()
  jumping()


# This runs the main function 
main()
