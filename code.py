"""
Created by Annwyn M. 
Created on Mar 4/2025
This makes an RGB LED light up and blink with different colours 
"""
import board 
import time 
import digitalio

R_LED = digitalio.DigitalInOut(board.GP11) 
G_LED = digitalio.DigitalInOut(board.GP12) 
B_LED = digitalio.DigitalInOut(board.GP13) 

blink_time = 1 
while True: 
  R_LED = False
  G_LED = False
  B_LED = False

  
  R_LED.value = True
  time.sleep(blink_time) 
  
  R_LED.value = False
  G_LED.value = True 
  time.sleep(blink_time) 
  
  G_LED.value = False
  B_LED.value = True 
  time.sleep(blink_time) 
  
  B_LED.value = False
  R_LED.value = True
  G_LED.value = True
  time.sleep(blink_time) 
  
  R_LED.value = False
  G_LED.value = True
  B_LED.value = True
  time.sleep(blink_time) 
  
  G_LED.value = False
  B_LED.value = True 
  R_LED.value = True
  time.sleep(blink_time)
  
  B_LED.value = True
  R_LED.value = True
  G_LED.value = True
  time.sleep(blink_time)

blink_time += 1 
  




