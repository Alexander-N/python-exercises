import string
import random
import datetime

class Robot(object):
    letters = string.ascii_uppercase    # [A, B, C, ... Z ]
    digits = string.digits              # [ 0, ...9]
    pattern = {"alpha": 2, "digits": 3} 

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = self.genName()

    def genName(self):
        random.seed(datetime.datetime.now().timestamp())
        name = ""

        for i in list(range(0, Robot.pattern["alpha"])): 
            name += self.letters[int(random.random()*26)]

        for i in list(range(0, Robot.pattern["digits"])):
            name += self.digits[int(random.random()*10)]
        
        print ('name', name)
        return name
