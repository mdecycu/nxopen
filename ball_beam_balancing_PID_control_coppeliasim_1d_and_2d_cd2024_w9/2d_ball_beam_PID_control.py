# pip install pyzmq cbor keyboard
# zmqRemoteApi_IPv6 為將 zmq 通訊協定修改為 IPv4 與 IPv6 相容
from zmqRemoteApi_IPv6 import RemoteAPIClient
import keyboard

# 利用 zmqRemoteAPI 以 23000 對場景伺服器進行連線
client = RemoteAPIClient('localhost', 23000)

print('Program started')
sim = client.getObject('sim')

# Get the handles of the ball, motorx, and motory objects
ball_handle = sim.getObject('/ball')
motorx_handle = sim.getObject('/motorx')
motory_handle = sim.getObject('/motory')

# PID control constants for x and y coordinates
kp_x = 1.0  # Proportional gain for x
ki_x = 0.1  # Integral gain for x
kd_x = 0.5  # Derivative gain for x

kp_y = 1.0  # Proportional gain for y
ki_y = 0.1  # Integral gain for y
kd_y = 0.5  # Derivative gain for y

# Initialize error and integral terms for x and y coordinates
error_sum_x = 0.0
last_error_x = 0.0

error_sum_y = 0.0
last_error_y = 0.0

sim.startSimulation()
print('Simulation started')

# Function to get the ball's x and y coordinates
def getBallCoordinates():
    pos = sim.getObjectPosition(ball_handle, -1)
    x = pos[0]
    y = pos[1]
    return x, y

def controlMotor(target_x, target_y, dt):
    global error_sum_x, last_error_x, error_sum_y, last_error_y

    # Get the current ball coordinates
    current_x, current_y = getBallCoordinates()
    print("Target: (", target_x, ",", target_y, "), Current: (", current_x, ",", current_y, ")")

    # Calculate errors for x and y coordinates
    error_x = target_x - current_x
    error_y = target_y - current_y

    # Update error sums for x and y coordinates
    error_sum_x += error_x
    error_sum_y += error_y

    # Calculate derivatives for x and y coordinates
    derivative_x = (error_x - last_error_x) / dt
    derivative_y = (error_y - last_error_y) / dt

    # Calculate control signals for x and y coordinates
    control_signal_x = kp_x * error_x + ki_x * error_sum_x + kd_x * derivative_x
    control_signal_y = kp_y * error_y + ki_y * error_sum_y + kd_y * derivative_y

    # Set the rotational angles of motorx and motory
    sim.setJointTargetPosition(motorx_handle, control_signal_x)
    sim.setJointTargetPosition(motory_handle, control_signal_y)

    # Update the last errors for x and y coordinates
    last_error_x = error_x
    last_error_y = error_y

while True:
    if keyboard.is_pressed('q'):
        # Stop simulation
        sim.stopSimulation()
        break

    # Control the motors to set the ball to the desired coordinates
    controlMotor(0.3, 0.3, 0.05)  # Adjust the time step (dt) and target coordinates as needed

# 終止模擬
#sim.stopSimulation()
