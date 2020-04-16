import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        head_pos = self.get_head()
        next_move_pos = [head_pos[0]+Snake.dx[self.direction], head_pos[1]+Snake.dy[self.direction]]
        f_cells = []
        if next_move_pos[0] == -1:
            next_move_pos[0] = consts.table_size-1
        elif next_move_pos[1] == -1:
            next_move_pos[1] = consts.table_size-1
        elif next_move_pos[0] == consts.table_size:
            next_move_pos[0] = 0
        elif next_move_pos[1] == consts.table_size:
            next_move_pos[1] = 0

        for i in self.game.snakes:
            for j in i.cells:
                f_cells.append(j)

        if (tuple(next_move_pos) in f_cells) or (next_move_pos in consts.block_cells):
            self.game.kill(self)
        elif (tuple(next_move_pos) in self.game.fruits):
            self.cells.append(tuple(next_move_pos))
            self.game.get_cell(self.get_head()).set_color(self.color)
        else:
            self.game.get_cell(self.cells.pop(0)).set_color(consts.back_color)
            self.cells.append(tuple(next_move_pos))
            self.game.get_cell(self.get_head()).set_color(self.color)


    def handle(self, keys):
        rev = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        for i in keys:
            if i in self.keys.keys():
                if rev[self.keys[i]] != self.direction:
                    self.direction = self.keys[i]
                    break

        