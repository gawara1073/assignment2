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
- パブリッシャ―
[INFO] [1736242235.630722281] [battery_publisher]: Publishing: Battery: 68.46% | Consumption: 0.80W
[INFO] [1736242236.572843578] [battery_publisher]: Publishing: Battery: 68.46% | Consumption: 0.64W
[INFO] [1736242237.572486751] [battery_publisher]: Publishing: Battery: 68.46% | Consumption: 1.20W

- リスナー
  [INFO] [1736242372.401926013] [battery_listener]: Received: Battery: 68.46% | Consumption: 0.77W
[INFO] [1736242373.379820669] [battery_listener]: Received: Battery: 68.46% | Consumption: 1.46W\
[INFO] [1736242374.380403723] [battery_listener]: Received: Battery: 68.46% | Consumption: 0.73W

## ライセンス
このプロジェクトは、3条項BSDライセンスの下、再頒布および使用が許可されています。

## 作成者
菅原 玲太
e-mail:sugawararyota0813@icloud.com
