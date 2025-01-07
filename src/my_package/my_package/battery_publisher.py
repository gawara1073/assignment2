#SPDX-FileCopyrightText: 2025 Ryota Sugawara
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil  # バッテリー情報を取得するためのライブラリ
import random  # 消費量を擬似的に生成するためのライブラリ

class BatteryPublisher(Node):
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(String, 'battery_stats', 10)
        self.timer = self.create_timer(1.0, self.publish_battery_stats)

    def publish_battery_stats(self):
        battery = psutil.sensors_battery()  # バッテリー情報を取得
        if battery:
            charge = battery.percent  # 現在のバッテリー充電量（%）
            consumption = random.uniform(0.5, 1.5)  # 擬似的な消費量（例: ワット単位）
            msg = String()
            msg.data = f'Battery: {charge}% | Consumption: {consumption:.2f}W'
            self.publisher_.publish(msg)
            self.get_logger().info(f'Publishing: {msg.data}')
        else:
            self.get_logger().warn('Battery information not available.')

def main():
    rclpy.init()
    node = BatteryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

