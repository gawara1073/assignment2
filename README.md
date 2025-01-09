# my_package

## 概要
`my_package`は、ROS2を使用してバッテリーの状態（充電量や充電中の状態）を取得し、トピックとして配信するサンプルパッケージです。

## インストール方法
以下の手順に従って`my_package`をセットアップしてください。

### 前提条件
- ROS2がインストールされていること
  - [ROS2公式インストールガイド](https://docs.ros.org/en/humble/Installation.html)を参照してください。
- Pythonライブラリ`psutil`がインストールされていること
  ```bash
  pip install psutil
  ```

### 手順

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/gawara1073/my_package.git
   ```

2. ワークスペースを構築します。
   ```bash
   cd my_package/src
   colcon build
   ```

3. 環境を設定します。
   ```bash
   source install/setup.bash
   ```

## 使用方法

1. パブリッシャーノードを起動します。
   ```bash
   ros2 run my_package battery_publisher
   ```

2. トピックの内容を確認します。
   別のターミナルで以下のコマンドを実行してください。
   ```bash
   ros2 topic echo /battery_status
   ```

   **出力例:**
   ```
   data: "Battery Level: 45%, Status: Charging"
   ```

## ライセンス
このプロジェクトは、3条項BSDライセンスの下、再頒布および使用が許可されています。


## 作成者
菅原玲太  
e-mail: sugawararyota0813@icloud.com
