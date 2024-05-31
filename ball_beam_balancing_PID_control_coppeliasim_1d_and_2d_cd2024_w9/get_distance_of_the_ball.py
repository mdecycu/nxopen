# pip install pyzmq cbor keyboard
# zmqRemoteApi_IPv6 為將 zmq 通訊協定修改為 IPv4 與 IPv6 相容
from zmqRemoteApi_IPv6 import RemoteAPIClient
import keyboard

# 利用 zmqRemoteAPI 以 23000 對場景伺服器進行連線
client = RemoteAPIClient('localhost', 23000)

print('Program started')
sim = client.getObject('sim')

# Get the handle of the proximity sensor and the ball
laser_handle = sim.getObject('/laser')
# Set the ball object in the property common tab to be detectable
ball_handle = sim.getObject('/ball')

sim.startSimulation()
print('Simulation started')

# Function to get the distance between the laser and the ball
def getDistance():
    result, distance, _, _, _ = sim.readProximitySensor(laser_handle, ball_handle)
    if result == 1:
        return round(distance, 4)
    else:
        return None

while True:
    if keyboard.is_pressed('q'):
        # Stop simulation
        sim.stopSimulation()
        break
    # Get and print the distance between the laser and the ball
    distance = getDistance()
    if distance is not None:
        print('Distance:', distance)
    else:
        print('No object detected')

# 終止模擬
#sim.stopSimulation()
