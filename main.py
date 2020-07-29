from kivy.app import App
from kivy.config import Config

from controller import Controller
from view.gui import Gui



class MyApp(App):
    title = "Sudoku Solver"
    icon = "sudoku.png"

    def build(self):
        Config.set('graphics', 'width', '700')
        Config.set('graphics', 'height', '700')



        gui = Gui()



        global controller
        controller = Controller(gui)


        return gui


if __name__ == '__main__':
    MyApp().run()
