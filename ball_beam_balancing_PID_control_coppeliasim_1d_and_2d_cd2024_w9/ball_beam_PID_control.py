# pip install pyzmq cbor keyboard
# zmqRemoteApi_IPv6 為將 zmq 通訊協定修改為 IPv4 與 IPv6 相容
from zmqRemoteApi_IPv6 import RemoteAPIClient
import keyboard
import time

#time.sleep(15)

# 利用 zmqRemoteAPI 以 23000 對場景伺服器進行連線
client = RemoteAPIClient('localhost', 23000)

print('Program started')
sim = client.getObject('sim')

# Get the handle of the proximity sensor and the ball
laser_handle = sim.getObject('/laser')
# Set the ball object in the property common tab to be detectable
ball_handle = sim.getObject('/ball')
motor_handle = sim.getObject('/motor')
# motor rotation angle plus to make ball move to the right
# motor rotation angle minus to make ball move to the left

# PID control constants
kp = 1.0  # Proportional gain
ki = 0.1  # Integral gain
kd = 0.5  # Derivative gain

# Initialize error and integral term
error_sum = 0.0
last_error = 0.0

sim.startSimulation()
print('Simulation started')

# Function to get the distance between the laser and the ball
def getDistance():
    result, distance, _, _, _ = sim.readProximitySensor(laser_handle, ball_handle)
    if result == 1:
        return round(distance, 4)
    else:
        return None

def controlMotor(target_distance, dt):
    global error_sum, last_error

    # Get the current distance
    distance = getDistance()
    print(target_distance, distance)

    if distance is not None:
        # Calculate the error term
        error = target_distance - distance
        print(error)
        # Update the error sum
        error_sum += error

        # Calculate the derivative term
        derivative = (error - last_error) / dt

        # Calculate the control signal
        control_signal = kp * error + ki * error_sum + kd * derivative

        # Set the motor rotation angle
        sim.setJointTargetPosition(motor_handle, control_signal)

        # Update the last error
        last_error = error

while True:
    if keyboard.is_pressed('q'):
        # Stop simulation
        sim.stopSimulation()
        break

    # Control the motor to maintain a desired distance
    controlMotor(0.9, 0.05)  # Adjust the time step (dt) as needed

# 終止模擬
#sim.stopSimulation()
