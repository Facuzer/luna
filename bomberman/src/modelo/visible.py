class Visible():
    def __init__(self, pos):
        self.__set_pos(pos)

    def __get_pos_x(self):
        return self.pos[0]
    
    def __get_pos_y(self):
        return self.pos[1]
    
    def __set_pos_x(self, pos_x):
        self.pos[0] = pos_x

    def __set_pos_y(self, pos_y):
        self.pos[1] = pos_y
    
    def __set_pos(self, pos):
        self.pos = pos