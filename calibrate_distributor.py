import pyautogui as pag


class CalibrateDistributorSolver:

    def __init__(self):
        self._color_pos = [
            (1250, 230),
            (1250, 500),
            (1250, 765)
        ]

        self._button_pos = [
            (1230, 310),
            (1230, 580),
            (1230, 845)
        ]

    def solve_calibrate_distributor(self):
        # while loop for each position until we get the color, then click
        for i in range(len(self._color_pos)):
            # wait until not black
            while pag.screenshot().getpixel(self._color_pos[i]) == (0, 0, 0):
                pass
            print(f"{i}: found")
            pag.click(self._button_pos[i])


def main():
    pass


if __name__ == '__main__':
    main()