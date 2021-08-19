# -*- coding: utf-8 -*-
'''
Time:   2021/8/19 18:40
Author: Sanzo
Github: github.com/Sanzo00
Email:  arrangeman@163.com
'''

import json
import websockets
import asyncio
import logging
import os
import time

# cur_dir = os.path.abspath(__file__).rsplit("/", 1)[0]
# log_path = os.path.join(cur_dir, "server.log")
# logging.basicConfig(filename=log_path)
# logging.info("server send to control: {0}".format(msg))

users = set()
car = None

def get_time():
  return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

async def watchDog(websocket, path):
  global users
  async for message in websocket:
    data = json.loads(message)
    print(get_time(), "server receive:", message)
    if 'type' not in data:
      print(get_time(), "unsupported event, please set type!")
    elif data["device"] == "car":
      await car_event(websocket, data)
    elif data["device"] == "control":
      users.add(websocket)
      # print("users size: {0}".format(len(users))) # bug!!!
      await control_event(websocket, data)

async def car_event(websocket, data):
  global car
  # print("id(car): ", id(car))
  if data["type"] == "connect":
    car = websocket

async def control_event(websocket, data):
  msg = {"device": "server"}
  if data["type"] == "connect":
    msg["state"] = 0 if car is None else 1
    await websocket.send(json.dumps(msg))
    print(get_time(), "server send to control: {0}".format(msg))

  elif data["type"] == "move" and car is not None:
    msg["action"] = data["action"]
    await car.send(json.dumps(msg))
    print(get_time(), "server send to car: {0}".format(msg))

start_server = websockets.serve(watchDog, "0.0.0.0", 9527)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
