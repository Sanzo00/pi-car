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

ENA = 20
ENB = 21
IN = [5, 6, 13, 19]

move = Move(ENA, ENB, IN)

try:
  # move.forward()
  # move.back()
  # move.left()
  # GPIO.cleanup()
  move.right()
  while True:
    time.sleep(5)
except KeyboardInterrupt:
  print("中断程序!")
  GPIO.cleanup()