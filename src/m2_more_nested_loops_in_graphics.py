"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Cleo Barmes.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------

    left_point = rectangle.get_upper_left_corner()
    right_point = rectangle.get_lower_right_corner()

    original_lx = left_point.x
    original_ly = left_point.y
    original_rx = right_point.x
    original_ry = right_point.y

    length = abs(original_rx - original_lx)
    height = abs(original_ry - original_ly)

    original_lx = original_lx - (n / 2 * length)
    original_rx = original_rx - (n / 2 * length)

    lx = original_lx
    ly = original_ly
    rx = original_rx
    ry = original_ry

    for k in range(n):
        for j in range((n - k)):
            lx = lx + (length / 2)
            rx = rx + (length / 2)
        for h in range(k + 1):
            left = rg.Point(lx, ly)
            right = rg.Point(rx, ry)
            brick = rg.Rectangle(left, right)
            brick.attach_to(window)
            window.render()
            lx = lx + length
            rx = rx + length
        ly = ly - height
        ry = ry - height
        lx = original_lx
        rx = original_rx
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
