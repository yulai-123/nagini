#!/bin/bash

# 获取当前时间作为日志文件名
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="logs/bot_$TIMESTAMP.log"

echo "Starting bot..."
ps -ef | grep 'python3 bot.py' | grep -v grep | awk '{print $2}'| sudo xargs kill -9;
# 在后台运行机器人并将输出重定向到日志文件
nohup python3 bot.py >> "$LOG_FILE" 2>&1 &

echo "Started successfully"