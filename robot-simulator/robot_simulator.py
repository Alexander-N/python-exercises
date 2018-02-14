from itertools import cycle

NORTH, EAST, SOUTH, WEST = range(4)

class Robot(object):
    def __init__(self, bearing=NORTH, coord_x=0, coord_y=0):
        # if bearing is not in range(4):
            # raise ValueError("Bearing is strange.")
        self.bearing = bearing
        self.coord_x = coord_x
        self.coord_y = coord_y

    @property
    def coordinates(self):
        return (self.coord_x, self.coord_y)

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        if self.bearing == NORTH:
            self.coord_y += 1
        if self.bearing == SOUTH:
            self.coord_y -= 1
        if self.bearing == EAST:
            self.coord_x += 1
        if self.bearing == WEST:
            self.coord_x -= 1
            
    def simulate(self, directions):
        for step in directions:
            if step == "L":
                self.turn_left()
            elif step == "R":
                self.turn_right()
            elif step == "A":
                self.advance()
            else:
                raise ValueError(str(step) + " is a bad direction.")

