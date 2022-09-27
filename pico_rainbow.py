import utime
import st7789
from pimoroni import RGBLED

import time
import random
import st7789

# Set the display resolution, in most cases you can flip these for portrait mode
# WIDTH, HEIGHT = 240, 135    # Pico Display
WIDTH, HEIGHT = 240, 240  # Pico Display 2.0

display = st7789.ST7789(WIDTH, HEIGHT, rotate180=False)

display.set_backlight(0.1)


class Ball:
    def __init__(self, x, y, r, pen):
        self.x = x
        self.y = y
        self.r = r
        self.pen = pen


# initialise shapes
balls = []
#RED
r = 120
balls.append(
    Ball(
        WIDTH/2,
        240,
        r,
        display.create_pen(255, 0, 0),
    )
)

#ORANGE
r = 110
balls.append(
    Ball(
        WIDTH/2,
        240,
        r,
        display.create_pen(255, 236, 0),
    )
)

#YELLOW
r = 100
balls.append(
    Ball(
        WIDTH/2,
        240,
        r,
        display.create_pen(255, 255, 0),
    )
)

#Green
r = 90
balls.append(
    Ball(
        WIDTH/2,
        240,
        r,
        display.create_pen(0, 255, 0),
    )
)

#BLUE
r = 80
balls.append(
    Ball(
        WIDTH/2,
        240,
        r,
        display.create_pen(0, 0, 255),
    )
)

#INDIGO
r = 70
balls.append(
    Ball(
        WIDTH/2,
        240,
        r,
        display.create_pen(200, 0, 255),
    )
)


#inner circle
r = 60
balls.append(
    Ball(
        WIDTH/2,
        240,
        r,
        display.create_pen(0, 0, 0),
    )
)



display.set_pen(0, 0, 0)
display.clear()

for ball in balls:
    display.set_pen(ball.pen)
    display.circle(int(ball.x), int(ball.y), int(ball.r))

display.set_pen(255,255,255)
display.text("JAMES' RAINBOW!", 10, 10, 240, 4)  # Add some text
display.update()
