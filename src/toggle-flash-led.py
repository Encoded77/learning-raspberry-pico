from machine import Pin
from time import sleep_ms

toggle_pin = Pin(18, mode=Pin.IN, pull=Pin.PULL_UP)

leds = [Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(12, Pin.OUT)]

def flash_leds():
  for led in leds:
    led.toggle()
    sleep_ms(100)

def reset_leds(pins_addr = leds):
  for pin_n in pins_addr:
    pin = Pin(pin_n, Pin.OUT)
    pin.value(0)

should_flash = True

def interruption_handler(pin: Pin):
  global should_flash

  should_flash = not should_flash
  reset_leds()

toggle_pin.irq(trigger=Pin.IRQ_FALLING, handler=interruption_handler)

while True:
  if should_flash:
    flash_leds()
  else:
    sleep_ms(100)
