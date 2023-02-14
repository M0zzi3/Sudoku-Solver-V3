class Sudoku:
    def __init__(self):

        # define plane matrix
        self.plane = []
        for y in range(9):
            x_row = []
            for x in range(9):
                x_row.append([])
            self.plane.append(x_row)

        self.show_plane()

    def show_plane(self):
        for x_row in self.plane:
            for place in x_row:
                print(f' {place}',end='')
            print('')

