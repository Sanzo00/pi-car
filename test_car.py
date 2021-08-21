# -*- coding: utf-8 -*-
'''
Time:   2021/8/20 14:40
Author: Sanzo
Github: github.com/Sanzo00
Email:  arrangeman@163.com
'''

from move import Move
from distance import Distance
from auto import Auto
import RPi.GPIO as GPIO
import time
import collections

ENA = 20
ENB = 21
IN = [5, 6, 13, 19]
ECHO = 14
TRIG = 15

move = Move(ENA, ENB, IN)
distance = Distance(TRIG, ECHO)
auto = Auto(move, distance)

def test_move():
  try:
    # GPIO.cleanup()
    move.forward()
    # move.back()
    # move.left()
    # move.left45()
    # move.left90()
    # move.right()
    # move.right45()
    # move.right90()
    while True:
      time.sleep(2)
  except KeyboardInterrupt:
    print("中断程序!")
    GPIO.cleanup()

def test_speed():
  try:
    move.forward()
    while True:
      time.sleep(2)
      move.speed('medium')
      time.sleep(2)
      move.speed('fast')
      time.sleep(2)
      move.speed('low')
  except KeyboardInterrupt:
    print("中断程序!")
    GPIO.cleanup()


def test_distance():
  while True:
    time.sleep(1)
    print(distance.dis())

def test_auto():
  auto.go()

def test_queue():
  d = collections.deque(maxlen=5)
  for i in range(7):
    d.append(i)
  print(d)
  print(sum(d) / len(d))

def test_backoff():
  old = move.speed_type
  move.speed('medium')
  move.back()
  move.speed(old)
  time.sleep(0.35)
  move.right45()
  move.forward()

def test_time():
  for i in range(5):
    time.sleep(1)
    print(time.time())

# test_move()
# test_speed()
# test_distance()
# test_auto()
# test_queue()
# test_backoff()
# test_time()
