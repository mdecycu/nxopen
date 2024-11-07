# pip install pyzmq cbor keyboard
# for 4.7.0 rev4
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import keyboard
import random
import math

client = RemoteAPIClient('localhost', 23000)

print('Program started')
sim = client.getObject('sim')
#sim.startSimulation()
print('Simulation started')


def setBubbleRobVelocity(leftWheelVelocity1, rightWheelVelocity1,leftWheelVelocity2, rightWheelVelocity2):
    leftMotor1 = sim.getObject('/b_player2/joint_lf')
    rightMotor1 = sim.getObject('/b_player2/joint_rf')
    leftMotor2 = sim.getObject('/b_player2/joint_lb')
    rightMotor2 = sim.getObject('/b_player2/joint_rb')
    sim.setJointTargetVelocity(leftMotor1, leftWheelVelocity1)
    sim.setJointTargetVelocity(rightMotor1, rightWheelVelocity1)
    sim.setJointTargetVelocity(leftMotor2, leftWheelVelocity2)
    sim.setJointTargetVelocity(rightMotor2, rightWheelVelocity2)
    #輸入四個變數分別給四個軸速度
    
def setBubbleRobangel(a):
    brickRob= sim.getObject('/b_player2')
    angel = [-90*math.pi/180, a*math.pi/180, 0*math.pi/180]
    leftMotor = sim.getObject('/b_player2/joint_lf')
    rightMotor = sim.getObject('/b_player2/joint_rf')
    sim.setObjectOrientation(leftMotor, brickRob, angel)
    sim.setObjectOrientation(rightMotor, brickRob, angel)
    #輸入一個變數改變前輪方向
  
while True:
    if keyboard.is_pressed('w'):
        setBubbleRobVelocity(8, 8, 8, 8)
        if keyboard.is_pressed('a'):
            setBubbleRobangel(-40)
        elif keyboard.is_pressed('d'):
            setBubbleRobangel(40)
        else:
            setBubbleRobangel(0)
    elif keyboard.is_pressed('s'):
        setBubbleRobVelocity(-8, -8, -8, -8)
        if keyboard.is_pressed('a'):
            setBubbleRobangel(-40)
        elif keyboard.is_pressed('d'):
            setBubbleRobangel(40)
        else:
            setBubbleRobangel(0)
    elif keyboard.is_pressed('a'):
        setBubbleRobVelocity(-8, 8, -8, 8)
    elif keyboard.is_pressed('d'):
        setBubbleRobVelocity(8, -8, 8, -8)
    elif keyboard.is_pressed('q'):
        # stop simulation
        sim.stopSimulation()
    else:
        setBubbleRobVelocity(0, 0, 0, 0)
        setBubbleRobangel(0)




