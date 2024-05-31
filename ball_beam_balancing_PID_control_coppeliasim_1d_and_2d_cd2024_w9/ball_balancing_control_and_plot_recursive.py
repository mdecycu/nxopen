# 導入必要的模組
import matplotlib.pyplot as plt
from zmqRemoteApi_IPv6 import RemoteAPIClient
import keyboard
import os
import random

# 設定模擬參數
simulation_count = 0
max_simulations = 10  # 最大模擬次數
kp_range = (0.5, 2.0)  # 比例增益調整範圍
ki_range = (0.01, 0.2)  # 積分增益調整範圍
kd_range = (0.1, 1.0)  # 微分增益調整範圍

# 利用 zmqRemoteAPI 以 23000 對場景伺服器進行連線
client = RemoteAPIClient('localhost', 23000)
sim = client.getObject('sim')

# 取得物件的控制代碼
ball_handle = sim.getObject('/ball')
motorx_handle = sim.getObject('/motorx')
motory_handle = sim.getObject('/motory')

# 函數用於取得球的 x 和 y 座標
def getBallCoordinates():
    pos = sim.getObjectPosition(ball_handle, -1)
    x = pos[0]
    y = pos[1]
    return x, y

# 函數用於控制馬達
def controlMotor(target_x, target_y, dt, kp_x, ki_x, kd_x, kp_y, ki_y, kd_y):
    global error_sum_x, last_error_x, error_sum_y, last_error_y

    # 取得目前的球座標
    current_x, current_y = getBallCoordinates()

    # 計算 x 和 y 座標的誤差
    error_x = target_x - current_x
    error_y = target_y - current_y

    # 更新 x 和 y 座標的誤差總和
    error_sum_x += error_x
    error_sum_y += error_y

    # 計算 x 和 y 座標的微分
    derivative_x = (error_x - last_error_x) / dt
    derivative_y = (error_y - last_error_y) / dt

    # 計算 x 和 y 座標的控制訊號
    control_signal_x = kp_x * error_x + ki_x * error_sum_x + kd_x * derivative_x
    control_signal_y = kp_y * error_y + ki_y * error_sum_y + kd_y * derivative_y

    # 設定 motorx 和 motory 的旋轉角度
    sim.setJointTargetPosition(motorx_handle, control_signal_x)
    sim.setJointTargetPosition(motory_handle, control_signal_y)

    # 更新 x 和 y 座標的最後誤差
    last_error_x = error_x
    last_error_y = error_y

# 函數用於執行一次模擬
def run_simulation(kp_x, ki_x, kd_x, kp_y, ki_y, kd_y):
    global simulation_count, x_coordinates, y_coordinates

    # 重置誤差累積和最後誤差
    global error_sum_x, last_error_x, error_sum_y, last_error_y
    error_sum_x = 0.0
    last_error_x = 0.0
    error_sum_y = 0.0
    last_error_y = 0.0

    # 清空座標列表
    x_coordinates = []
    y_coordinates = []

    sim.startSimulation()

    while True:
        if keyboard.is_pressed('q'):
            sim.stopSimulation()
            return

        # 取得目前的球座標
        current_x, current_y = getBallCoordinates()

        # 檢查球是否超出平台範圍
        if abs(current_x) > 1.2 or abs(current_y) > 1.2:
            sim.stopSimulation()
            break

        # 控制馬達
        controlMotor(0.3, 0.3, 0.05, kp_x, ki_x, kd_x, kp_y, ki_y, kd_y)

        # 儲存目前的 x 和 y 座標
        x_coordinates.append(current_x)
        y_coordinates.append(current_y)

    # 繪製模擬結果
    plt.plot(x_coordinates, label='X Coordinate')
    plt.plot(y_coordinates, label='Y Coordinate')
    plt.xlabel('Time')
    plt.ylabel('Coordinate')
    plt.title('Ball Position on Balancing Platform')
    plt.legend()

    # 儲存圖形為 PNG 檔案
    filename = f"simulation_{simulation_count}.png"
    plt.savefig(filename)
    plt.clf()  # 清除圖形

    simulation_count += 1

# 主迴圈
while simulation_count < max_simulations:
    # 在一定範圍內隨機調整 PID 參數
    kp_x = random.uniform(*kp_range)
    ki_x = random.uniform(*ki_range)
    kd_x = random.uniform(*kd_range)
    kp_y = random.uniform(*kp_range)
    ki_y = random.uniform(*ki_range)
    kd_y = random.uniform(*kd_range)

    # 執行模擬
    run_simulation(kp_x, ki_x, kd_x, kp_y, ki_y, kd_y)