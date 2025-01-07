#SPDX-FileCopyrightText: 2025 Ryota Sugawara
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BatteryListener(Node):
    def __init__(self):
        super().__init__('battery_listener')
        self.subscription = self.create_subscription(
            String,
            'battery_stats',  # トピック名
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main():
    rclpy.init()
    node = BatteryListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

