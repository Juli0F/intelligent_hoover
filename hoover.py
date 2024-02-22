import time
class Hoover(object):
    def __init__(self, pos_x, pos_y, radio=1):
        self.pos_x = radio
        self.pos_y = pos_y
        self.symbol = "_7_"
        self.color = ""
        self.amount_trash = 0
        self.radio = radio
        self.moving_right = True

    def left_move(self):
        self.pos_y -= self.radio

    def right_move(self):
        self.pos_y += self.radio

    def up_move(self):
        self.pos_x -= self.radio

    def down_move(self):
        self.pos_x += self.radio

    def search_and_move(self, quadrant):
        original_pos_x, original_pos_y = self.pos_x, self.pos_y
        print(f"x = {self.pos_x}, y = {self.pos_y}")
        if self.moving_right:
            if self.pos_y < quadrant.size_y - self.radio:
                self.right_move()
            else:
                self.down_move()
                self.moving_right = False
        else:
            if self.pos_y > 0:
                self.left_move()
            else:
                self.down_move()
                self.moving_right = True

        has_trash_left = quadrant.check_trash(self.pos_x, self.pos_y - self.radio)
        has_trash_right = quadrant.check_trash(self.pos_x, self.pos_y + self.radio)
        has_trash_up = quadrant.check_trash(self.pos_x - self.radio, self.pos_y)
        has_trash_down = quadrant.check_trash(self.pos_x + self.radio, self.pos_y)

        if has_trash_left:
            self.left_move()
            quadrant.show_square(self)

        elif has_trash_right:
            self.right_move()
            quadrant.show_square(self)

        elif has_trash_up:
            self.up_move()
            quadrant.show_square(self)

        elif has_trash_down:
            self.down_move()
            quadrant.show_square(self)

        if has_trash_left or has_trash_right or has_trash_up or has_trash_down:
            print(f"Basura a la izquierda: {has_trash_left}, derecha: {has_trash_right}, up: {has_trash_up}, down: {has_trash_down}")
            quadrant.clean_square(self.pos_y, self.pos_x)
            time.sleep(1)
            self.amount_trash += 1
            self.pos_x, self.pos_y = original_pos_x, original_pos_y
            print(f"Basura recolectada: {self.amount_trash}")
            print(f"posicion: {self.pos_x}, {self.pos_y}")


