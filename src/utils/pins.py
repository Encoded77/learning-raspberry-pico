from machine import Pin

ALL_PINS_ADDR = list(range(1, 28))

def reset_pins(pins_addr = ALL_PINS_ADDR):
  for pin_n in pins_addr:
    pin = Pin(pin_n, Pin.OUT)
    pin.value(0)

reset_pins()
