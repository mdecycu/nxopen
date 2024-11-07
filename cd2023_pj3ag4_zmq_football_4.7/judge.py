# pip install pyzmq cbor keyboard
# for 4.7.0 rev4
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import keyboard
import random

client = RemoteAPIClient('localhost', 23000)

print('Program started')
sim = client.getObject('sim')
sim.startSimulation()
print('Simulation started')

def avoid(x,y):
    #bubbleRob = sim.getObject('/brickRob')
    #bubbleRob2 = sim.getObject('/brickRob2')
    #b1=sim.getObjectPosition(bubbleRob,-1)
    #b2=sim.getObjectPosition(bubbleRob2,-1)
    
    #while (((b1[0]<x+0.5) and (b1[0]>x-0.5)) and ((b1[1]<y+0.5) and (b1[1]>y-0.5)))or(((b2[0]<x+0.5) and (b2[0]>x-0.5)) and ((b2[1]<y+0.5) and (b2[1]>y-0.5))):
    #x=random.uniform(-1,1)
    #y=random.uniform(-1,1)
       # print(x)
       # print(y)
    position2= [x, y, 2]
    ball = sim.createPureShape(1, options, size, 1, None)
    sim.setObjectPosition(ball, -1, position2)
    
size = [0.1, 0.1, 0.1]
position = [0, 0, 2]
options = 8
def existball():
    try:
        Sphere= sim.getObject('/Sphere')
    except Exception as e:
        #print("Failed to get object: ", e)
        return 1
    return 0

if existball()==1:    
    ball = sim.createPureShape(1, options, size, 1, None)
    sim.setObjectPosition(ball, -1, position)
    ball = sim.getObject('/Sphere')
    sim.setObjectSpecialProperty(ball, sim.objectspecialproperty_detectable)

while True:

    ball = sim.getObject('/Sphere')
    ball_position =sim.getObjectPosition(ball,-1)
    if ball_position[1]<-1.865 or ball_position[1]>1.865:
        #sim.removeObject(ball)
        sim.setObjectAlias(ball, 'ball')
        ball2=sim.getObject('/ball')
        sim.removeObject(ball2)
        avoid(random.uniform(-1,1),random.uniform(-1,1))
        #avoid(0,2)
        ball = sim.getObject('/Sphere')
        sim.setObjectSpecialProperty(ball, sim.objectspecialproperty_detectable)
 




