from square import Square


class Quadrant(object):
    def __init__(self, size_x=0, size_y=0):
        self.size_x = size_x
        self.size_y = size_y
        self.squares = [[Square(x, y) for x in range(size_x)] for y in range(size_y)]

    def add_trash(self, trash):
        if 0 <= trash.pos_x < self.size_x and 0 <= trash.pos_y < self.size_y:
            self.squares[trash.pos_y][trash.pos_x].trash = trash
        else:
            print("Posicion incorrecta")

    def show_square(self, hoover):
        for i in range(self.size_x):
            for j in range(self.size_y):
                square = self.squares[j][i]
                if (i, j) == (hoover.pos_x, hoover.pos_y):
                    print(hoover.symbol, end=" ")
                elif square.trash is not None:
                    print(square.trash.symbol, end=" ")
                else:
                    print(square.symbol, end=" ")
            print("")

    def check_trash(self, x, y):
        if 0 <= x < self.size_x and 0 <= y < self.size_y:
            return self.squares[y][x].trash is not None
        else:
            return False

    def clean_square(self, x, y):
        print(f"Posicion de basura:{x},{y} ")
        self.squares[x][y].trash = None
