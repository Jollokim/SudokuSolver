from model.spot import Spot
import math


class Solver:
    def __init__(self):
        self.spots = []
        self.row = 0
        self.col = 0
        self.solved = False
        self.tracked_back = False
        self.stop_slow_solve = False
        self.solving = False

        for row in range(9):
            self.spots.append([])

            for col in range(9):
                self.spots[row].append(Spot())


    def update_model(self):
        for row in range(9):
            for col in range(9):

                if self.spots[row][col].unchangeable:
                    self.spots[row][col].legal_number = self.check_number_legal(self.spots[row][col].num, row, col)
                    continue

                self.spots[row][col].possible_nums.clear()

                # finds numbers that could fit in a pos
                for num in range(1, 10):
                    if self.check_number_legal(num, row, col):
                        self.spots[row][col].possible_nums.append(num)


    def check_number_legal(self, num, row, col):
        if num == "":
            return True

        squareRow = math.floor(row / 3) * 3
        squareCol = math.floor(col / 3) * 3

        # check square
        for sqRow in range(squareRow, squareRow + 3):
            for sqCol in range(squareCol, squareCol + 3):

                if sqRow == row and sqCol == col:
                    pass
                elif num == self.spots[sqRow][sqCol].num:
                    return False

        for i in range(9):
            # test row
            if i == col:
                pass
            elif num == self.spots[row][i].num:
                return False
            # test col
            if i == row:
                pass
            elif num == self.spots[i][col].num:
                return False

        # if it fits 
        return True


    def plus_spot_val(self, row, col):
        self.spots[row][col].pluss_one()

        self.spots[row][col].legal_number = self.check_number_legal(self.spots[row][col].num, row, col)

        self.update_model()


    def reset_all(self):
        print("Modell reset!")

        for row in range(9):
            for col in range(9):
                self.spots[row][col] = Spot()

        self.row = 0
        self.col = 0
        self.solved = False
        self.tracked_back = False
        self.solving = False

    def is_solveable(self):
        for row in self.spots:
            for spot in row:
                if not spot.legal_number:
                    return False
        return True

    def track_forth_spot(self):
        self.col += 1
        if self.col > 8:
            self.row +=1
            self.col = 0

        self.tracked_back = False

        if self.row > 8:
            self.solved = True

    def track_back_spot(self):
        self.col -= 1

        if self.col < 0:
            self.row -= 1
            self.col = 8

        self.tracked_back = True

    def fast_solve(self):
        if self.is_solveable():


            while not self.solved:
                self.slow_solve()


    def slow_solve(self):
        self.solving = True

        try:
            while self.spots[self.row][self.col].unchangeable:
                if self.tracked_back:
                    print("backtracking")
                    self.track_back_spot()
                else:
                    print("forth tracking")
                    self.track_forth_spot()
        except IndexError:
            self.solved = True
            return
        except:
            print("SOmething went wrong in testing unchangeable")



        print("row:", str(self.row), "col:", str(self.col))

        possible_nums = self.spots[self.row][self.col].possible_nums
        possible_counter = self.spots[self.row][self.col].possible_counter

        if self.tracked_back:
            possible_counter += 1
            if possible_counter >= len(possible_nums):
                print("nothing fits")
                self.spots[self.row][self.col].possible_counter = 0
                self.spots[self.row][self.col].num = ""
                self.track_back_spot()
                return

        number_to_test = possible_nums[possible_counter]

        print(possible_nums)
        print(number_to_test)

        while not self.check_number_legal(number_to_test, self.row, self.col):
            possible_counter += 1

            try:
                number_to_test = possible_nums[possible_counter]
                print(number_to_test)
            except:
                # none fit
                print("nothing fits back tracking")
                self.spots[self.row][self.col].possible_counter = 0
                self.spots[self.row][self.col].num = ""
                self.track_back_spot()
                return


        # number fits
        print("number fits")
        self.spots[self.row][self.col].possible_counter = possible_counter
        self.spots[self.row][self.col].num = number_to_test

        self.track_forth_spot()














