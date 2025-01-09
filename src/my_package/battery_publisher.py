#SPDX-FileCopyrightText: 2025 Ryota Sugawara
#SPDX-License-Identifier: BSD-3-Clause


import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil


class BatteryPublisher(Node):
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(String, 'battery_status', 10)
        self.timer = self.create_timer(1.0, self.publish_battery_status)
        self.get_logger().info("Battery Publisher Node has started.")

    def publish_battery_status(self):
        # psutilを使ってバッテリー情報を取得
        battery = psutil.sensors_battery()

        if battery is not None:
            # バッテリーレベルと消費率を取得
            battery_level = battery.percent  # バッテリー残量（％）
            is_charging = battery.power_plugged  # 充電中かどうか
            status = "Charging" if is_charging else "Discharging"
            msg = String()
            msg.data = f"Battery Level: {battery_level}%, Status: {status}"
            self.publisher_.publish(msg)
            self.get_logger().info(f"Publishing: {msg.data}")
        else:
            self.get_logger().error("Battery information is not available on this system.")


def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Node stopped manually.")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
