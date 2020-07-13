import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

import math

defaultcolor1 = (0, 1, 255, 1)
defaultcolor2 = (1, 1, 1, 1)

class Gui(GridLayout):
    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)

        self.cols = 1

        self.sudoku_board = GridLayout()

        self.sudoku_board.cols = 9
        self.sudoku_board.rows = 9

        self.spots = []


        for row in range(9):
            self.spots.append([])
            for col in range(9):
                spot = Button(text=str(""))

                spot.row = row
                spot.col = col

                # spot.defaultColor = (120, 1, 1, 1)

                if math.floor(row/3) != 1:
                    if math.floor(col/3) != 1:
                        spot.defaultColor = defaultcolor1
                    else:
                        spot.defaultColor = defaultcolor2
                else:
                    if math.floor(col / 3) == 1:
                        spot.defaultColor = defaultcolor1
                    else:
                        spot.defaultColor = defaultcolor2



                spot.background_color = spot.defaultColor
                spot.border = (1, 1, 1, 1)
                spot.bind(on_press=self.spotPressed)

                self.sudoku_board.add_widget(spot)

                self.spots[row].append(spot)

        self.add_widget(self.sudoku_board)

        self.buttons = GridLayout(size_hint_y=0.1)

        self.buttons.cols = 3

        self.resetButton = Button(text="Reset")
        self.resetButton.background_color = (0, 255, 0, 1)
        self.resetButton.border = (1, 1, 1, 1)
        self.resetButton.bind(on_press=self.resetBoard)

        self.slowSolveButt = Button(text="Slow Solve")
        self.slowSolveButt.background_color = (255, 0, 0, 1)
        self.slowSolveButt.border = (1, 1, 1, 1)
        self.slowSolveButt.bind(on_press=self.slowSolve)

        self.fastSolveButt = Button(text="Fast Solve")
        self.fastSolveButt.background_color = (0, 0, 255, 1)
        self.fastSolveButt.border = (1, 1, 1, 1)
        self.fastSolveButt.bind(on_press=self.fastSolve)

        self.buttons.add_widget(self.resetButton)
        self.buttons.add_widget(self.slowSolveButt)
        self.buttons.add_widget(self.fastSolveButt)

        self.add_widget(self.buttons)

    def updateSpots(self, spot_list):

        for row in range(9):
            for col in range(9):
                model_spot = spot_list[row][col]

                self.spots[row][col].text = str(model_spot.num)

                if not model_spot.legalNumber:
                    self.spots[row][col].background_color = (255, 1, 1, 1)
                else:
                    self.spots[row][col].background_color = self.spots[row][col].defaultColor



    def slowSolve(self, instance):
        print("SlowSolve pressed")
        self.controller.startSlowSolve()

    def fastSolve(self, instance):
        print("FastSolve")
        self.controller.startFastSolve()

    def spotPressed(self, instance):
        self.controller.spotPressed(instance)

    def resetBoard(self, instance):
        self.controller.resetModell()



