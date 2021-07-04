import pyautogui as pag

x_click_left = 600
x_click_right = 1280

x_color_left = 550
x_color_right = 1340

y_pos = (270, 460, 640, 830)


def drag_from_to(sx, sy, fx, fy, drag_duration=0.0, _button="left"):
    pag.mouseDown(sx, sy, button=_button)
    pag.moveTo(fx, fy, drag_duration)
    pag.mouseUp()


class WireSolver:

    def __init__(self):
        self._left_color_pos = [
            (x_color_left, y_pos[0]),
            (x_color_left, y_pos[1]),
            (x_color_left, y_pos[2]),
            (x_color_left, y_pos[3])
        ]

        self._left_click_pos = [
            (x_click_left, y_pos[0]),
            (x_click_left, y_pos[1]),
            (x_click_left, y_pos[2]),
            (x_click_left, y_pos[3])
        ]

        self._right_color_pos = [
            (x_color_right, y_pos[0]),
            (x_color_right, y_pos[1]),
            (x_color_right, y_pos[2]),
            (x_color_right, y_pos[3])
        ]

        self._right_click_pos = [
            (x_click_right, y_pos[0]),
            (x_click_right, y_pos[1]),
            (x_click_right, y_pos[2]),
            (x_click_right, y_pos[3])
        ]

    def solve_wires(self):
        try:
            shot = pag.screenshot()
            colors_left = [shot.getpixel(i) for i in self._left_color_pos]
            colors_right = [shot.getpixel(i) for i in self._right_color_pos]

            for i in range(len(colors_left)):
                print(f"{colors_left[i]}  \t\t{colors_right[i]}")

            for i in range(len(colors_left)):
                sx, sy = self._left_click_pos[i]
                fx, fy = self._right_click_pos[colors_right.index(colors_left[i])]
                drag_from_to(sx, sy, fx, fy)

        except Exception as e:
            print(f"Error: {e}")


def main():
    # sc = Shortcut(solve_wires, lambda: None, combination={Key.shift_l, Key.space})
    # sc.start()
    pass


if __name__ == '__main__':
    main()
