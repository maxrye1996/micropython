import time
import machine
import dht 
import random
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P8
 
sensor = dht.DHT11(machine.Pin(2))

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P8)

WIDTH, HEIGHT = display.get_bounds()
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)



while True:
  try:
    time.sleep(2)
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(WHITE)
    display.text(f"Temp: {t} C \nHum: {h} %", 10, 10, 240, 4)
    display.update()
    print('Temperature: %3.1f C' %t)
    print('Humidity: %3.1f %%' %h)
  except OSError as e:
    print('Sensor Reading Failed')