from machine import Pin, ADC
from time import sleep_ms

led = Pin(25, Pin.OUT)

lightSensor = ADC(26)

while True:
  print('Sensor value:', lightSensor.read_u16())
  sleep_ms(200)
