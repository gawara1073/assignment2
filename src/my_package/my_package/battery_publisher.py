#SPDX-FileCopyrightText: 2025 Ryota Sugawara
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class BatteryPublisher(Node):
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(String, 'battery_status', 10)
        self.timer = self.create_timer(2.0, self.publish_battery_status)  # 2秒ごとに実行
        self.get_logger().info('Battery Publisher Node started.')

    def publish_battery_status(self):
        # ランダムにバッテリー残量を生成（例：10%から100%）
        battery_level = random.randint(10, 100)
        # 消費量もランダムに生成（例：1%から10%）
        consumption_rate = random.randint(1, 10)
        msg = String()
        msg.data = f'Battery Level: {battery_level}%, Consumption Rate: {consumption_rate}%/hour'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Node stopped cleanly')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

