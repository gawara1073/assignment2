#!/bin/bash
#SPDX-FileCopyrightText: 2025 Ryota Sugawara
#SPDX-License-Identifier: BSD-3-Clause

# スクリプトの開始を表示
echo "Starting ROS2 package test..."

# ワークスペースのセットアップ
echo "Sourcing ROS2 environment..."
source /opt/ros/<your_ros2_distro>/setup.bash  # <your_ros2_distro> を galactic や humble に変更

echo "Sourcing workspace..."
source ~/assignment2/ros2_ws/install/setup.bash

# ワークスペースのビルド
echo "Building workspace..."
colcon build
if [ $? -ne 0 ]; then
    echo "Build failed. Exiting."
    exit 1
fi

# パブリッシャーノードをバックグラウンドで起動
echo "Starting battery_publisher node..."
ros2 run my_package battery_publisher &
PUBLISHER_PID=$!

# リスナーノードを起動
echo "Starting battery_listener node..."
ros2 run my_package battery_listener &
LISTENER_PID=$!

# 5秒間待機
echo "Waiting for 5 seconds to observe node output..."
sleep 5

# ノードの停止
echo "Stopping nodes..."
kill $PUBLISHER_PID
kill $LISTENER_PID

# スクリプトの終了を表示
echo "Test completed."
