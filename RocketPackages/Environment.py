import math as m


class Environment:
    def __init__(self):
        self.subsonic = True
        self.transonic = False
        self.supersonic = False
        self.hypersonic = False

        self.gravity_force = 0  # kN
        self.gravitational_acceleration = 9.81  # m/s²

        self.drag_force = 0  # kN
        self.lift_force = 0  # kN

        self.cd = 10
        self.rho = 1.3  # kg/m3

    def update_gravity_force(self, weight):
        self.gravity_force = weight * self.gravitational_acceleration

    def update_aero_force(self, speed, reference_area):
        self.drag_force = self.cd * self.rho * speed ** 2 * reference_area / 2

    def update_rho_air(self, altitude):
        if altitude < 0:
            self.rho = 1.225

        elif altitude < 1000:
            self.rho = 1.225

        elif altitude < 2000:
            self.rho = 1.112

        elif altitude < 3000:
            self.rho = 1.007

        elif altitude < 4000:
            self.rho = 0.909

        elif altitude < 5000:
            self.rho = 0.819

        elif altitude < 6000:
            self.rho = 0.736

        elif altitude < 7000:
            self.rho = 0.660

        elif altitude < 8000:
            self.rho = 0.590

        elif altitude < 9000:
            self.rho = 0.525

        elif altitude < 10000:
            self.rho = 0.466

        else:
            self.rho = 0.413

    def update_sonic(self, speed):
        if speed <= 343:
            self.subsonic = True
            self.transonic = False
            self.supersonic = False
            self.hypersonic = False
        elif speed == 343:
            self.subsonic = False
            self.transonic = True
            self.supersonic = False
            self.hypersonic = False
        elif speed < 343 * 5:
            self.subsonic = False
            self.transonic = False
            self.supersonic = True
            self.hypersonic = False
        elif speed > 343 * 5:
            self.subsonic = False
            self.transonic = False
            self.supersonic = False
            self.hypersonic = True
