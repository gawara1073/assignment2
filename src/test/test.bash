#!/bin/bash
#SPDX-FileCopyrightText: 2025 Ryota Sugawara
#SPDX-License-Identifier: BSD-3-Clause

# スクリプトをエラーで停止する
set -e

echo "=== Setting up ROS2 workspace ==="
source install/setup.bash

echo "=== Starting battery_publisher node ==="
# バックグラウンドでノードを起動
ros2 run my_package battery_publisher &
PUBLISHER_PID=$!

# 少し待機してからデータを確認
sleep 5

echo "=== Subscribing to /battery_status topic ==="
# トピックのデータを1回だけ受け取る
ros2 topic echo /battery_status --once

# ノードを停止する
echo "=== Stopping battery_publisher node ==="
kill $PUBLISHER_PID

echo "=== Test completed ==="

