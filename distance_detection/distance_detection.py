from hcsr04 import HCSR04
from time import sleep
import machine
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P8
from pimoroni import Buzzer

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P8)

WIDTH, HEIGHT = display.get_bounds()
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)

STATUS_LED = machine.Pin(25, machine.Pin.OUT)
RED_LED = machine.Pin(2, machine.Pin.OUT)
GREEN_LED = machine.Pin(6, machine.Pin.OUT)
BUZZER = Buzzer(5)

# BUZZER.set_tone(4970)
# BUZZER.set_tone(-1)
# STATUS_LED.value(1)
# RED_LED.value(1)
# GREEN_LED.value(1)

sensor = HCSR04(trigger_pin=4, echo_pin=0)

while True:
    STATUS_LED.value(1)
    distance = sensor.distance_cm()
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(WHITE)
    display.text(f"Distance: {distance}cm", 10, 10, 240, 4)
    display.update()
    
    if distance < 10:
        GREEN_LED.value(0)
        RED_LED.value(1)
        BUZZER.set_tone(4970)
    else:
        RED_LED.value(0)
        GREEN_LED.value(1)
        BUZZER.set_tone(-1)

    sleep(0.01)