import math as m
import time

from Messages import *
from RocketPackages import Engine, Tank


class Rocket:
    def __init__(self):
        self.start_flight = False
        self.height = 3000  # mm
        self.radius = 16  # mm
        self.weight = 30  # kg

        self.pos_x = 0
        self.pos_y = 0

        # Rocket Components
        self.engine = Engine.Engine()
        self.tank = Tank.Tank()

    def ignition(self):
        print(f"{Info.INFO_0004.value}")
        self.start_flight = True
        self.engine.start()
        self.tank.emptying = True

    def update(self, time_step):
        pre_loop_time = time.time()
        while self.start_flight:
            if (time.time() - pre_loop_time) > time_step:
                # Update Engine thrust
                self.engine.update(time_step)
                self.tank.update(time_step)
                # Update Commands

                # Update Sensors

                pre_loop_time = time.time()
