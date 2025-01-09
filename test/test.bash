#!/bin/bash
#SPDX-FileCopyrightText: 2025 Ryota Sugawara
#SPDX-License-Identifier: BSD-3-Clause

# ワークスペースのセットアップ
echo "Setting up ROS 2 workspace..."
source ~/assignment2/ros2_ws/install/setup.bash

# ノードの実行
echo "Starting the battery_publisher node..."
ros2 run my_package battery_publisher &
NODE_PID=$!  # バックグラウンドプロセスのPIDを記録

# トピックのエコー
echo "Echoing the /battery_status topic..."
ros2 topic echo /battery_status &

# テストを一定時間実行 (例: 10秒)
echo "Running the test for 10 seconds..."
sleep 10

# ノードとエコーを停止
echo "Stopping the battery_publisher node and topic echo..."
kill $NODE_PID
kill %1  # トピックエコーを停止

echo "Test completed."
