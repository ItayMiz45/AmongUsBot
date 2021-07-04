import pyautogui as pag
import time
from AmongUs.wires import WireSolver
from AmongUs.calibrate_distributor import CalibrateDistributorSolver
from AmongUs.swipe_card import SwipeCardSolver


WIRES_ID = 1
CALIBRATE_DISTRIBUTOR_ID = 2
SWIPE_CARD_ID = 3


# (
# 	( id, (pos, color), (pos, color) )
# )


missions_sig = (
    (WIRES_ID, ((700, 148), (16, 16, 19)), ((1170, 274), (21, 20, 24))),
    (CALIBRATE_DISTRIBUTOR_ID, ((559, 111), (203, 203, 203)), ((1391, 228), (66, 65, 66))),
    (SWIPE_CARD_ID, ((1300, 155), (22, 74, 57)), ((558, 280), (30, 31, 30)))
)


def get_mission():
    shot = pag.screenshot()

    for miss in missions_sig:
        curr_id = miss[0]

        print(f"ID: {curr_id}")
        is_good = True

        for pos_col in miss[1:]:
            print(f"Position: {pos_col[0]}, Color: {pos_col[1]}")
            if shot.getpixel(pos_col[0]) != pos_col[1]:
                is_good = False
                break

        if is_good:
            print(f"Is {curr_id}")
            return curr_id

        else:
            print(f"Not {curr_id}")

        print()


def main():
    wire_solver = WireSolver()
    calibrate_distributor_solver = CalibrateDistributorSolver()
    swipe_card_solver = SwipeCardSolver()

    while True:
        mission_id = None
        while mission_id is None:
            mission_id = get_mission()

            print(f"ID from get_mission(): {mission_id}")

            if mission_id == WIRES_ID:
                wire_solver.solve_wires()
            elif mission_id == CALIBRATE_DISTRIBUTOR_ID:
                calibrate_distributor_solver.solve_calibrate_distributor()
            elif mission_id == SWIPE_CARD_ID:
                swipe_card_solver.solve_swipe_card()
            else:
                continue

            # after a task was solved wait to not detect it again
            time.sleep(2)


if __name__ == '__main__':
    main()
