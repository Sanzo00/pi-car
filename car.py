# -*- coding: utf-8 -*-
'''
Time:   2021/8/19 18:40
Author: Sanzo
Github: github.com/Sanzo00
Email:  arrangeman@163.com
'''

from move import Move
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

move = Move(ENA, ENB, IN)

def get_time():
  return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

async def connect_and_move():
  url = "ws://localhost:9527" // your server address, which run server.py
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
        move.left()
      elif action == 'right':
        move.right()
      elif action == 'stop':
        move.stop()
      
asyncio.get_event_loop().run_until_complete(connect_and_move())