from kivy.app import App
from kivy.config import Config


from Controller.SudokuController import SudokuController
from View.gui import Gui



class MyApp(App):
    title = "Sudoku Solver"
    icon = "sudoku.png"

    def build(self):
        Config.set('graphics', 'width', '700')
        Config.set('graphics', 'height', '700')



        gui = Gui()



        global controller
        controller = SudokuController(gui)


        return gui


if __name__ == '__main__':
    MyApp().run()

# solver = Solver.Solver()
#
# run = True
#
# while run:
