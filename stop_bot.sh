#!/bin/bash

ps -ef | grep 'python3 bot.py' | grep -v grep | awk '{print $2}'| sudo xargs kill -9;

echo "Completed stop"