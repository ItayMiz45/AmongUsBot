import pyautogui as pag
import time


def drag_from_to(sx, sy, fx, fy, drag_duration=0.0, _button="left"):
    pag.mouseDown(sx, sy, button=_button)
    pag.moveTo(fx, fy, drag_duration)
    pag.mouseUp()


class SwipeCardSolver:

    def __init__(self):
        self._CARD_IN_WALLET_POS = (760, 825)
        self._sx = 545
        self._sy = 415
        self._fx = 1508
        self._fy = 420

    def solve_swipe_card(self):
        pag.click(*self._CARD_IN_WALLET_POS)
        time.sleep(0.45)
        drag_from_to(self._sx, self._sy, self._fx, self._fy, drag_duration=0.55)


def main():
    solver = SwipeCardSolver()
    solver.solve_swipe_card()


if __name__ == '__main__':
    main()
