# -*- coding: utf-8 -*-
'''
Time:   2021/8/19 18:40
Author: Sanzo
Github: github.com/Sanzo00
Email:  arrangeman@163.com
'''

import RPi.GPIO as GPIO
import time

class Move:
  
  def __init__(self, ENA, ENB, INs):
    self.IN = INs
    self.ENA = ENA
    self.ENB = ENB
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.ENA, GPIO.OUT)
    GPIO.setup(self.ENB, GPIO.OUT)
    for i in self.IN:
      GPIO.setup(i, GPIO.OUT)

    self.speed_type = 'slow'
    self.pwm_left = GPIO.PWM(self.ENA, 100)
    self.pwm_right = GPIO.PWM(self.ENB, 100)
    self.pwm_left.start(40)
    self.pwm_right.start(40)
    self.stop()
    # print("init is done!")

  def __del__(self):
    self.pwm_left.stop()
    self.pwm_right.stop()
    GPIO.cleanup()
  
  def speed(self, speed_type):
    if speed_type == 'slow':
      self.speed_type = 'slow'
      self.pwm_left.ChangeDutyCycle(40)
      self.pwm_right.ChangeDutyCycle(40)
    elif speed_type == 'medium':
      self.speed_type = 'medium'
      self.pwm_left.ChangeDutyCycle(78)
      self.pwm_right.ChangeDutyCycle(78)
    elif speed_type == 'fast':
      self.speed_type = 'fast'
      self.pwm_left.ChangeDutyCycle(100)
      self.pwm_right.ChangeDutyCycle(100)

  def right(self):
    # print("right")
    GPIO.output(self.IN[0], GPIO.LOW)
    GPIO.output(self.IN[1], GPIO.HIGH)
    GPIO.output(self.ENA, GPIO.HIGH)

    GPIO.output(self.IN[2], GPIO.LOW)
    GPIO.output(self.IN[3], GPIO.HIGH)
    GPIO.output(self.ENB, GPIO.HIGH)

  def right45(self):
    self.right()
    time.sleep(0.13)
    self.stop()

  def right90(self):
    self.right()
    time.sleep(0.5)
    self.stop()

  def left(self):
    # print("left")
    GPIO.output(self.IN[0], GPIO.HIGH)
    GPIO.output(self.IN[1], GPIO.LOW)
    GPIO.output(self.ENA, GPIO.HIGH)

    GPIO.output(self.IN[2], GPIO.HIGH)
    GPIO.output(self.IN[3], GPIO.LOW)
    GPIO.output(self.ENB, GPIO.HIGH)

  def left45(self):
    self.left()
    time.sleep(0.13)
    self.stop()

  def left90(self):
    self.left()
    time.sleep(0.48)
    self.stop()

  def back(self):
    # print("back")
    GPIO.output(self.IN[0], GPIO.HIGH)
    GPIO.output(self.IN[1], GPIO.LOW)
    GPIO.output(self.ENA, GPIO.HIGH)

    GPIO.output(self.IN[2], GPIO.LOW)
    GPIO.output(self.IN[3], GPIO.HIGH)
    GPIO.output(self.ENB, GPIO.HIGH)

  def forward(self):
    # print("forward")
    GPIO.output(self.IN[0], GPIO.LOW)
    GPIO.output(self.IN[1], GPIO.HIGH)
    GPIO.output(self.ENA, GPIO.HIGH)

    GPIO.output(self.IN[2], GPIO.HIGH)
    GPIO.output(self.IN[3], GPIO.LOW)
    GPIO.output(self.ENB, GPIO.HIGH)

  def stop(self):
    # print("stop")
    GPIO.output(self.IN[0], GPIO.LOW)
    GPIO.output(self.IN[1], GPIO.LOW)
    GPIO.output(self.ENA, GPIO.HIGH)

    GPIO.output(self.IN[2], GPIO.LOW)
    GPIO.output(self.IN[3], GPIO.LOW)
    GPIO.output(self.ENB, GPIO.HIGH)