class Visible():
    def __init__(self, pos):
        self._set_pos(pos)

    def _get_pos_x(self):
        return self.pos[0]
    
    def _get_pos_y(self):
        return self.pos[1]
    
    def _set_pos_x(self, pos_x):
        self.pos[0] = pos_x

    def _set_pos_y(self, pos_y):
        self.pos[1] = pos_y
    
    def _set_pos(self, pos):
        self.pos = pos