NORTH, EAST, SOUTH, WEST = range(4)

class Robot(object):
    def __init__(self,bearing=NORTH,x=0,y=0):
        self.coordinates = (x,y)
        self.bearing = bearing
        self.grid_dict = {NORTH:(0,1),EAST:(1,0),SOUTH:(0,-1),WEST:(-1,0)}
        self.instruction_dict = {'L': self.turn_left, 'R': self.turn_right, 'A': self.advance}

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        x = self.coordinates[0] + self.grid_dict[self.bearing][0]
        y = self.coordinates[1] + self.grid_dict[self.bearing][1]
        self.coordinates = (x,y)

    def simulate(self, instructions):
        """ 
            Args:
                Instructions: string chain with L, A or R
        """
        for char in instructions:
            self.instruction_dict[char]()

