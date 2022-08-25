import sys
import time

import time as t
from threading import Thread

import Messages
from Messages import *
from Rocket import *


class Simulation:
    def __init__(self):
        self.run = False
        self.time_simulation = 0
        self.time_start_loop = 0
        self.second_timer = 0
        self.time_step = 1
        self.real_time_clock = 0
        self.simulation_acceleration = 1

        self.rocket = Rocket()

        self.time_thread = Thread(target=self.start, args=())
        self.rocket_thread = Thread(target=self.rocket.update, args=(self.time_step,))
        self.info_thread = Thread(target=self.print_info, args=())

        self.start_threads()

    def start(self):
        print(f"{Info.INFO_0001.value}")
        self.run = True
        self.time_start_loop = t.time()

        self.rocket.ignition()

        while self.run:
            self.real_time_clock_update()
            # print(f"{Info.INFO_0003.value} : {int(self.time_simulation)}s")

        print(f"{Info.INFO_0002.value}")

    def real_time_clock_update(self):
        if t.time() - self.time_start_loop > self.time_step * self.simulation_acceleration:
            self.time_simulation += self.time_step
            self.time_start_loop = t.time()

    def start_threads(self):
        self.time_thread.start()
        self.rocket_thread.start()
        self.info_thread.start()

    def print_info(self):
        seconds = 0
        info_step = 1
        pre_loop_time = t.time()
        while self.run:
            if (t.time() - pre_loop_time) > info_step:
                print(f"Time : {int(seconds * 100) / 100} s")
                print(f"{Messages.Info.INFO_0005.value} {int(self.rocket.engine.thrust_power)} kN")
                print(f"{Messages.Info.INFO_0006.value} {self.rocket.tank.liter}")
                seconds += info_step
                if self.rocket.engine.thrust_power > 300:
                    self.rocket.start_flight = False
                    break
                pre_loop_time = t.time()
