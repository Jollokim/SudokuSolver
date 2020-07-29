from model.solver import Solver
from kivy.clock import Clock



class Controller:
    def __init__(self, gui):
        self.solver = Solver()
        self.gui = gui
        self.gui.controller = self

    def reset_modell(self):
        self.solver.reset_all()

        self.gui.update_spots(self.solver.spots)
        self.solver.stop_slow_solve = True

    def spot_pressed(self, spot):
        if self.solver.solving:
            return

        row = spot.row
        col = spot.col

        print("row", row, "col", col)



        self.solver.plus_spot_val(row, col)
        self.gui.update_spots(self.solver.spots)

    def start_slow_solve(self):
        if not self.solver.is_solveable():
            print("Not solveable")
            return

        self.gui.slow_solve_button.disabled = True

        self.solver.stop_slow_solve = False

        print("Starting Slowsolve")
        Clock.schedule_interval(self.slow_solve_interval, 0.1)



    def slow_solve_interval(self, dt):
        if self.solver.stop_slow_solve or self.solver.solved:
            self.gui.slow_solve_button.disabled = False
            return False

        self.solver.slow_solve()
        self.gui.update_spots(self.solver.spots)

    def start_fast_solve(self):
        self.solver.fast_solve()
        self.gui.update_spots(self.solver.spots)
        self.gui.slow_solve_button.disabled = False




