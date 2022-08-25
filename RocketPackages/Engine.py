import time


class Engine:
    def __init__(self):
        self.weight = 0.3  # kg
        self.thrust_power_command = 0  # kN
        self.thrust_power = 0  # kN
        self.thrust_acceleration = 50  # kN
        self.max_thrust_power = 300  # kN

        self.ignite = False

    def start(self):
        self.ignite = True
        self.change_thrust_power(300)

    def stop(self):
        self.change_thrust_power(0)
        self.ignite = False

    def change_thrust_power(self, thrust_power):
        if thrust_power > self.max_thrust_power:
            self.thrust_power_command = self.max_thrust_power
        else:
            self.thrust_power_command = thrust_power

    def engine_force_acceleration(self, time_step):
        if self.thrust_power < self.max_thrust_power and self.thrust_power < self.thrust_power_command:
            self.thrust_power += self.thrust_acceleration / time_step
            # print(f"1 : {self.thrust_power}")
        elif self.thrust_power >= self.max_thrust_power:
            self.thrust_power = self.max_thrust_power
            # print(f"2 : {self.thrust_power}")

    def update(self, time_step):
        if self.ignite:
            self.engine_force_acceleration(time_step)
        else:
            self.thrust_power = 0
