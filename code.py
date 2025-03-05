"""
Created by Annwyn M. 
Created on Mar 4/2025
This makes an RGB LED light up and blink with different colours using the different LED bulbs
"""
import board 
import time 
import digitalio

R_LED.value = digitalio.DigitalInOut(board.GP11) 
G_LED.value = digitalio.DigitalInOut(board.GP12) 
B_LED.value = digitalio.DigitalInOut(board.GP13) 

R_LED.direction = digitalio.Direction.OUTPUT
G_LED.direction = digitalio.Direction.OUTPUT
B_LED.direction = digitalio.Direction.OUTPUT

blink_time = 1 
while True: 
  R_LED.value = False
  G_LED.value = False
  B_LED.value = False

  #red is turned on
  R_LED.value = True
  time.sleep(blink_time) 

  #green is turned on
  R_LED.value = False #turn off the red to put green on, repeat with other colours 
  G_LED.value = True 
  time.sleep(blink_time) 

  #blue is turned on 
  G_LED.value = False
  B_LED.value = True 
  time.sleep(blink_time) 

  #red and green on at the same time to create yellow
  B_LED.value = False 
  R_LED.value = True
  G_LED.value = True
  time.sleep(blink_time) 

  #green and blue on at the same time to create cyan 
  R_LED.value = False
  G_LED.value = True
  B_LED.value = True
  time.sleep(blink_time) 

  #red and green on at the same time to create magenta
  G_LED.value = False
  B_LED.value = True 
  R_LED.value = True
  time.sleep(blink_time)

  #all colours on to create white
  B_LED.value = True
  R_LED.value = True
  G_LED.value = True
  time.sleep(blink_time)

  #all colous are off
  G_LED.value = False  
  B_LED.value = False 
  R_LED.value = False 
  time.sleep(blink_time) 
  




