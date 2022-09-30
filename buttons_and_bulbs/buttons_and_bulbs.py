
# 2 = YELLOW_LED
# 3 = RED_LED
# 4 = BLUE_LED
# 5 = GREEN_LED
# 6 = yeelow button
# 7 = red button
# 8 = blue button
# 9 = green button


# This example shows you a simple, non-interrupt way of reading Pico Explorer's buttons with a loop that checks to see if buttons are pressed.
import time
import machine
from pimoroni import Button

yellow_button = Button(6)
red_button = Button(7)
blue_button = Button(8)
green_button = Button(9)

STATUS_LED = machine.Pin(25, machine.Pin.OUT)
YELLOW_LED = machine.Pin(2, machine.Pin.OUT)
RED_LED = machine.Pin(3, machine.Pin.OUT)
BLUE_LED = machine.Pin(4, machine.Pin.OUT)
GREEN_LED = machine.Pin(5, machine.Pin.OUT)

def fresh_start():
    STATUS_LED.value(0)
    YELLOW_LED.value(0)
    RED_LED.value(0)
    BLUE_LED.value(0)
    GREEN_LED.value(0)
    check_leds()

def check_leds():
    YELLOW_LED.value(1)
    time.sleep(2)
    YELLOW_LED.value(0)
    RED_LED.value(1)
    time.sleep(2)
    RED_LED.value(0)
    BLUE_LED.value(1)
    time.sleep(2)
    BLUE_LED.value(0)
    GREEN_LED.value(1)
    time.sleep(2)
    GREEN_LED.value(0)


fresh_start()
while True:
    STATUS_LED.value(1)
    if yellow_button.read():
        """ yellow led """
        YELLOW_LED.toggle()
    elif red_button.read():
        """ red led """
        RED_LED.toggle()
    elif blue_button.read():
        """ blue led """
        BLUE_LED.toggle()
    elif green_button.read():
        """ green led """
        GREEN_LED.toggle()
    time.sleep(0.01)
