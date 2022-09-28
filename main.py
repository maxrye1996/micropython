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

STATUS_LED = machine.Pin(25, machine.Pin.OUT)
YELLOW_LED = machine.Pin(3, machine.Pin.OUT)
GREEN_LED = machine.Pin(4, machine.Pin.OUT)
BLUE_LED = machine.Pin(7, machine.Pin.OUT)
RED_LED = machine.Pin(0, machine.Pin.OUT)

def turn_of_leds():
    # check all leds 
    RED_LED.value(0)
    YELLOW_LED.value(0)
    GREEN_LED.value(0)
    BLUE_LED.value(0)

def test_leds():
    # check all leds 
    RED_LED.value(1)
    time.sleep(1)
    RED_LED.value(1)
    YELLOW_LED.value(1)
    time.sleep(1)
    YELLOW_LED.value(0)
    GREEN_LED.value(1)
    time.sleep(1)
    GREEN_LED.value(0)
    BLUE_LED.value(1)
    time.sleep(1)
    BLUE_LED.value(0)

test_leds()
while True:
  # show the program has started 
  STATUS_LED.value(1)
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
    # print('Temperature: %3.1f C' %t)
    # print('Humidity: %3.1f %%' %h)

    turn_of_leds()
    if t < 18:
        # cold boi
        BLUE_LED.value(1)
    elif t >= 18 and t <= 20:
        YELLOW_LED.value(1)
    elif t > 20 and t <= 24:
        # perfect
        GREEN_LED.value(1)
    elif t > 24:
        # hot boi
        RED_LED.value(1)
  except OSError as e:
    print('Sensor Reading Failed')
    print(e)

