#!/usr/bin/env bash

ps -ef | grep python3 autologin.py | grep -v grep

if [ $? -ne 0 ]
then
  echo "start process..."
  cd /home/bjtu/;nohup python3 autologin.py
else
  echo "running..."
fi