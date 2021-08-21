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

# test_move()
test_speed()
# test_distance()
# test_auto()

