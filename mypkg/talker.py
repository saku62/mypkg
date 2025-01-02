#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuta Sakusabe <s23c1062mq@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Float32, "cpu_usage", 10)

def cb():
    # 現在のCPU使用率を取得
    cpu_usage = psutil.cpu_percent(interval=None)  # interval=Noneで直近の平均を取得
    msg = Float32()
    msg.data = cpu_usage
    pub.publish(msg)
    print(f"CPU Usage: {msg.data}%")

def main():
    # 1秒ごとにCPU使用率を取得して送信
    node.create_timer(1.0, cb)
    rclpy.spin(node)
