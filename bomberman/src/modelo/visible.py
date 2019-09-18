class Visible():
    def __init__(self):
        self.pos = []

    def __get_pos_x(self):
        return self.pos[0]
    
    def __get_pos_y(self):
        return self.pos[1]
    
    def __set_pos_x(self, pos_x):
        self.pos[0] = pos_x

    def __set_pos_y(self, pos_y):
        self.pos[1] = pos_y