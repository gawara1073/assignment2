# ROS2 Battery Package

このリポジトリは、バッテリーの状態をシミュレートし、パブリッシャーとサブスクライバのモデルを使用してバッテリー情報をモニタリングするROS2パッケージです。

## 動作環境
･ ROS2:ubuntu20.04
･ Python:3.8以上

## インストール手法
`git clone https://github.com/gawara1073/assignment2.git`

## 使用方法
以下のコマンドを起動します。
`ros2 run my_package battery_publisher`

その後、別の端末で以下のコマンドを実行します。
`ros2 run my_package battery_listener` 

## 出力例
パブリッシャ―

