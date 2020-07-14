from Model.Solver import Solver
from kivy.clock import Clock



class SudokuController:
    def __init__(self, gui):
        self.solver = Solver()
        self.gui = gui
        self.gui.controller = self

    def resetModell(self):
        self.solver.resetAll()

        self.gui.updateSpots(self.solver.spots)
        self.solver.stopSlowSolve = True

    def spotPressed(self, spot):
        if self.solver.solving:
            return

        row = spot.row
        col = spot.col

        print("row", row, "col", col)



        self.solver.plusSpotVal(row, col)
        self.gui.updateSpots(self.solver.spots)

    def startSlowSolve(self):
        if not self.solver.is_solveable():
            print("Not solveable")
            return

        self.gui.slowSolveButt.disabled = True

        self.solver.stopSlowSolve = False

        print("Starting Slowsolve")
        Clock.schedule_interval(self.slowSolveInterval, 0.1)



    def slowSolveInterval(self, dt):
        if self.solver.stopSlowSolve or self.solver.solved:
            self.gui.slowSolveButt.disabled = False
            return False

        self.solver.slowSolve()
        self.gui.updateSpots(self.solver.spots)

    def startFastSolve(self):
        self.solver.fastSolve()
        self.gui.updateSpots(self.solver.spots)
        self.gui.slowSolveButt.disabled = False




