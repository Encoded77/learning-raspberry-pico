from machine import Pin
from time import sleep_ms

BUTTON_PIN = Pin(18, mode=Pin.IN, pull=Pin.PULL_UP)
onboard_led = Pin(25, Pin.OUT)

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

def set_irq(pin: Pin):
  pin.irq(trigger=Pin.IRQ_FALLING, handler=interruption_handler)

set_irq(BUTTON_PIN)

while True:
  if should_flash:
    print('flashing')
    flash_leds()
  else:
    sleep_ms(100)
