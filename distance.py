# -*- coding: utf-8 -*-
'''
Time:   2021/8/20 11:55
Author: Sanzo
Github: github.com/Sanzo00
Email:  arrangeman@163.com
'''

import RPi.GPIO as GPIO
import time

class Distance:
  
  def __init__(self, TRIG, ECHO):
    self.TRIG = TRIG
    self.ECHO = ECHO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.TRIG, GPIO.OUT)
    GPIO.setup(self.ECHO, GPIO.IN)

  def __del__(self):
    GPIO.cleanup()

  def dis(self):
    GPIO.output(self.TRIG, GPIO.HIGH)
    time.sleep(0.00001) # 10us
    GPIO.output(self.TRIG, GPIO.LOW)

    while GPIO.input(self.ECHO) == GPIO.LOW:
      pass
    start_time = time.time()

    while GPIO.input(self.ECHO) == GPIO.HIGH:
      pass
    end_time = time.time()

    # GPIO.cleanup()
    GPIO.output(self.TRIG, GPIO.LOW)
    ret = (end_time - start_time) * 34000 / 2
    return f"{ret:.1f} cm"