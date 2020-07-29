from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

import math



class Gui(GridLayout):

    # blue
    default_color_1 = (0, 1, 255, 1)
    # grey
    default_color_2 = (1, 1, 1, 1)

    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)

        self.cols = 1

        # board layout
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


                if math.floor(row / 3) != 1:
                    if math.floor(col / 3) != 1:
                        spot.defaultColor = Gui.default_color_1
                    else:
                        spot.defaultColor = Gui.default_color_2
                else:
                    if math.floor(col / 3) == 1:
                        spot.defaultColor = Gui.default_color_1
                    else:
                        spot.defaultColor = Gui.default_color_2



                spot.background_color = spot.defaultColor
                spot.border = (1, 1, 1, 1)
                spot.bind(on_press=self.spot_pressed)

                self.sudoku_board.add_widget(spot)

                self.spots[row].append(spot)

        self.add_widget(self.sudoku_board)

        self.buttons = GridLayout(size_hint_y=0.1)

        # buttons layout, resett, slowsolve, fastsolve
        self.buttons.cols = 3

        self.reset_button = Button(text="Reset")
        self.reset_button.background_color = (0, 255, 0, 1)
        self.reset_button.border = (1, 1, 1, 1)
        self.reset_button.bind(on_press=self.reset_board)

        self.slow_solve_button = Button(text="Slow Solve")
        self.slow_solve_button.background_color = (255, 0, 0, 1)
        self.slow_solve_button.border = (1, 1, 1, 1)
        self.slow_solve_button.bind(on_press=self.slow_solve)

        self.fast_solve_button = Button(text="Fast Solve")
        self.fast_solve_button.background_color = (0, 0, 255, 1)
        self.fast_solve_button.border = (1, 1, 1, 1)
        self.fast_solve_button.bind(on_press=self.fast_solve)

        self.buttons.add_widget(self.reset_button)
        self.buttons.add_widget(self.slow_solve_button)
        self.buttons.add_widget(self.fast_solve_button)

        self.add_widget(self.buttons)

    def update_spots(self, spot_list):

        for row in range(9):
            for col in range(9):
                model_spot = spot_list[row][col]

                self.spots[row][col].text = str(model_spot.num)

                # if number not legal in position change color
                if not model_spot.legal_number:
                    self.spots[row][col].background_color = (255, 1, 1, 1)
                else:
                    self.spots[row][col].background_color = self.spots[row][col].defaultColor



    def slow_solve(self, instance):
        print("SlowSolve pressed")
        self.controller.start_slow_solve()

    def fast_solve(self, instance):
        print("FastSolve")
        self.controller.start_fast_solve()

    def spot_pressed(self, instance):
        self.controller.spot_pressed(instance)

    def reset_board(self, instance):
        self.controller.reset_modell()



