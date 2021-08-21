# -*- coding: utf-8 -*-
'''
Time:   2021/8/21 14:20
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
      # users.add(websocket)
      # print("users size: {0}".format(len(users))) # bug!!!
      await control_event(websocket, data)

async def car_event(websocket, data):
  global car
  # print("id(car): ", id(car))
  if data["type"] == "connect":
    car = websocket
  elif data["type"] == "config" and users is not None: # send distance to contorl
    for user in users:
      try:
        await user.send(json.dumps(data))
      except websockets.exceptions.ConnectionClosedError:
        pass
    users.clear()

async def control_event(websocket, data):
  global car
  msg = {"device": "server"}
  if data["type"] == "connect":
    msg["type"] = "connect"
    msg["state"] = 0 if car is None else 1
    await websocket.send(json.dumps(msg))
    print(get_time(), "server send to control: {0}".format(msg))

  # foward back stop left left45 right right45
  # slow fast distance auto
  elif (data["type"] == "move" or data["type"] == "config") and car is not None:
    if data["action"] == "distance":
      users.add(websocket)
    msg["action"] = data["action"]
    try:
      await car.send(json.dumps(msg))
      print(get_time(), "server send to car: {0}".format(msg))
    except websockets.exceptions.ConnectionClosedError:
      car = None

start_server = websockets.serve(watchDog, "0.0.0.0", 9527)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
