# -*- coding: utf-8 -*-
'''
Time:   2021/8/21 14:20
Author: Sanzo
Github: github.com/Sanzo00
Email:  arrangeman@163.com
'''

from move import Move
from distance import Distance
from auto import Auto
import RPi.GPIO as GPIO
import time
import json
import asyncio
import logging
import os
import websockets

ENA = 20
ENB = 21
IN = [5, 6, 13, 19]
ECHO = 14
TRIG = 15

move = Move(ENA, ENB, IN)
distance = Distance(TRIG, ECHO)
auto = Auto(move, distance)

def get_time():
  return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

async def connect_and_move():
  url = "ws://localhost:9527" # your server address, which run server.py
  async with websockets.connect(url) as websocket:
    # connect to server
    msg = {"device": "car", "type": "connect"}
    await websocket.send(json.dumps(msg))

    # receive msg from server
    while True:
      msg = await websocket.recv()
      msg = json.loads(msg)
      print("{0} receive from server: {1}".format(get_time(), msg))
      action = msg["action"]
      if action == 'back':
        move.back()
      elif action == 'forward':
        move.forward()
      elif action == 'left':
        old = move.speed_type
        move.speed('medium')
        move.left90()
        move.speed(old)
      elif action == 'left45':
        old = move.speed_type
        move.speed('medium')
        move.left45()
        move.speed(old)
      elif action == 'right':
        old = move.speed_type
        move.speed('medium')
        move.right90()
        move.speed(old)
      elif action == 'right45':
        old = move.speed_type
        move.speed('medium')
        move.right45()
        move.speed(old)
      elif action == 'stop':
        move.stop()
      elif action in ('slow', 'medium', 'fast'):
        move.speed(action)
      elif action == 'distance':
        msg = {"device": "car", "type": "config", "data": distance.dis()}
        print("send to server:", msg)
        await websocket.send(json.dumps(msg))
      elif action == 'auto':
        pass
        # auto.go()
      
asyncio.get_event_loop().run_until_complete(connect_and_move())