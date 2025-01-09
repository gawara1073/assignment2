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

    def publish_battery_status(self):
        # psutilを使ってバッテリー情報を取得
        battery = psutil.sensors_battery()  # batteryを定義
        if battery is None:  # バッテリー情報が取得できない場合
            print("バッテリー情報が取得できません。このシステムはバッテリー非対応の可能性があります。")
            return  # 処理を終了

        # バッテリーレベルと状態を取得
        battery_level = battery.percent  # バッテリー残量（％）
        is_charging = battery.power_plugged  # 充電中かどうか
        status = "Charging" if is_charging else "Discharging"
        msg = String()
        msg.data = f"Battery Level: {battery_level}%, Status: {status}"
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = BatteryPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

