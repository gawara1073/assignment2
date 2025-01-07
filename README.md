# ROS2 Battery Package

このパッケージは、ROS2上で動作するバッテリーモニタリングシステムです。

## 動作環境
･ ROS2:ubuntu20.04  　
･ Python:3.8以上

## インストール手法
`git clone https://github.com/gawara1073/assignment2.git`

## 使用方法
以下のコマンドを実行します。  
`ros2 run my_package battery_publisher`  

その後、別の端末で以下のコマンドを実行します。  
`ros2 topic echo /battery_status` 

## 出力例
-充電中: `Battery Level: 53.74%, Status: Charging`  
-充電してない: `Battery Level: 54.46%, Status: Discharging`
## ライセンス
このプロジェクトは、3条項BSDライセンスの下、再頒布および使用が許可されています。

## 作成者
菅原 玲太  
e-mail:sugawararyota0813@icloud.com
