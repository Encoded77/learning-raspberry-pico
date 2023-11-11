from machine import Pin
from time import sleep_ms

greenLED = Pin(10, Pin.OUT)
yellowLED = Pin(11, Pin.OUT)
redLED = Pin(12, Pin.OUT)

def chain_leds():
  greenLED.toggle()
  sleep_ms(100)
  yellowLED.toggle()
  sleep_ms(100)
  redLED.toggle()
  sleep_ms(100)

while True:
  chain_leds()
