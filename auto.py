# -*- coding: utf-8 -*-
'''
Time:   2021/8/20 16:04
Author: Sanzo
Github: github.com/Sanzo00
Email:  arrangeman@163.com
'''

from move import Move
from distance import Distance
import time
import collections

class Auto():
  def __init__(self, move, distance):
    self.distance = distance
    self.move = move
    self.off = False
    self.pre = (0, 0) # time, distance

  def stop(self):
    self.off = True

  def backoff(self):
    old = self.move.speed_type
    self.move.speed('medium')
    self.move.back()
    self.move.speed(old)
    time.sleep(0.30)
    # self.move.left45()
    self.move.right45()
    self.move.forward()

  def go(self):
    self.move.speed("slow")
    self.move.forward()
    while True:
      if self.off is True: # exit the thread
        self.move.stop()
        break

      dis = float(self.distance.dis()[:-3])
      if time.time() - self.pre[0] > 1.5: # 2s
        self.pre = (time.time(), dis)
        
      if dis <= 30.0 or (time.time() - self.pre[0] > 1.0 and abs(dis - self.pre[1]) < 2):
        self.backoff()