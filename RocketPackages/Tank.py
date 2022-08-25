import time

class Tank:
    def __init__(self):
        self.emptying = False
        self.weight = 10
        self.liter = 12
        self.propeller = "Propellant 1"
        self.flow_rate = 0.5  # L/s

    def update(self, time_step):
        if self.emptying:
            self.empty(time_step)

    def empty(self, time_step):
        if self.liter > 0:
            possible_liter = self.liter - (self.flow_rate / time_step)
            if possible_liter > 0:
                self.liter = possible_liter
            else:
                self.emptying = True
                self.liter = 0
