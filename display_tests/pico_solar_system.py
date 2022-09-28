import time
import random
import st7789

# Set the display resolution, in most cases you can flip these for portrait mode
# WIDTH, HEIGHT = 240, 135    # Pico Display
WIDTH, HEIGHT = 240, 240  # Pico Display 2.0

display = st7789.ST7789(WIDTH, HEIGHT, rotate180=False)

display.set_backlight(1.0)


class Ball:
    def __init__(self, x, y, r, pen):
        self.x = x
        self.y = y
        self.r = r
        self.pen = pen


# initialise shapes
balls = []
#SUN
r = 200
balls.append(
    Ball(
        -170,
        HEIGHT/2,
        r,
        display.create_pen(219, 178, 43),
    )
)

#MERCURY
r = 6
balls.append(
    Ball(
        40,
        HEIGHT/2,
        r,
        display.create_pen(175, 175, 175),
    )
)

#VENUS
r = 10
balls.append(
    Ball(
        60,
        HEIGHT/2,
        r,
        display.create_pen(206, 117, 0),
    )
)

#EARTH
r = 10
balls.append(
    Ball(
        85,
        HEIGHT/2,
        r,
        display.create_pen(0, 0, 255),
    )
)

#MARS
r = 8
balls.append(
    Ball(
        108,
        HEIGHT/2,
        r,
        display.create_pen(200, 0, 0),
    )
)

#JUPITER
r = 20
balls.append(
    Ball(
        141,
        HEIGHT/2,
        r,
        display.create_pen(252, 147, 10),
    )
)

#SATURN
r = 15
balls.append(
    Ball(
        181,
        HEIGHT/2,
        r,
        display.create_pen(160, 138, 109),
    )
)

#URANUS
r = 10
balls.append(
    Ball(
        211,
        HEIGHT/2,
        r,
        display.create_pen(26, 173, 237),
    )
)

#NEPTUNE
r = 10
balls.append(
    Ball(
        236,
        HEIGHT/2,
        r,
        display.create_pen(26, 89, 237),
    )
)



display.set_pen(0, 0, 0)
display.clear()

for ball in balls:
    display.set_pen(ball.pen)
    display.circle(int(ball.x), int(ball.y), int(ball.r))

display.update()
