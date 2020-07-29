class Spot:
    def __init__(self):
        self.num = ""
        self.possible_nums = []
        for num in range(1,10):
            self.possible_nums.append(num)

        self.possible_counter = 0
        self.unchangeable = False
        self.legal_number = True

    def pluss_one(self):
        try:
            number = int(self.num)
        except:
            self.num = 1
            self.unchangeable = True
            return

        self.unchangeable = True
        number += 1

        if number > 9:
            number = ""

        self.num = number

        if self.num == "":
            self.unchangeable = False


    def __str__(self):
        if self.num == "":
            return "empty"
        return str(self.num)