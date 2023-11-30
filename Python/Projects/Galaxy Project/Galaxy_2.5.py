from solid import *
from solid.extensions.legacy import *

G = 8

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
        self.delay = 3  # Delay between planet rotations in seconds
    
    def init(self):
        for p in self.planets:
            p.init()
    
    def start(self):
        for i, p in enumerate(self.planets):
            time.sleep(self.delay)
            self.t += self.dt
            p.step()
            while p.is_rotating():
                self.t += self.dt
                p.step()

class Star:
    def __init__(self, m, x, v, gravSys, color):
        self.m = m
        self.x = x
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.color = color
        self.rotating = True
    
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5 * dt * self.a
    
    def acc(self):
        a = vector(0, 0, 0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.x - self.x
                a += (G * planet.m / abs(v) ** 3) * v
        return a
    
    def step(self):
        dt = self.gravSys.dt
        self.x += dt * self.v
        self.a = self.acc()
        self.v += dt * self.a
    
    def is_rotating(self):
        return self.rotating

def create_planet(radius, distance, color):
    planet = sphere(radius=radius, segments=32)
    orbit = translate([distance, 0, 0])(planet)
    return color(color)(orbit)

def create_solar_system():
    gs = GravSys()
    sun = Star(1000000, vector(0, 0, 0), vector(0, -2.5, 0), gs, "Yellow")

    # Earth
    earth = Star(12500, vector(210, 0, 0), vector(0, -195, 0), gs, "Green")

    # Moon
    moon = Star(1, vector(220, 0, 0), vector(0, -295, 0), gs, "Blue")

    # Additional Planets
    mars = Star(10000, vector(-150, 0, 0), vector(0, -210, 0), gs, "Red")

    jupiter = Star(500000, vector(350, 0, 0), vector(0, -140, 0), gs, "Orange")

    # Create the OpenSCAD code
    code = ""

    # Sun
    code += create_planet(10, 0, sun.color)

    # Earth
    code += create_planet(2, 210, earth.color)

    # Moon
    code += create_planet(1, 220, moon.color)

    # Mars
    code += create_planet(3, -150, mars.color)

    # Jupiter
    code += create_planet(7, 350, jupiter.color)

    return code

# Generate the OpenSCAD code for the solar system
solar_system_code = create_solar_system()

# Save the OpenSCAD code to a file
with open("solar_system.scad", "w") as f:
    f.write(solar_system_code)
 
 