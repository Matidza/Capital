from turtle import Turtle, mainloop, Vec2D as Vec

G = 8

class GravSys:
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    
    def init(self):
        for p in self.planets:
            p.init()
    
    def start(self):
        for _ in range(10000):
            self.t += self.dt
            for p in self.planets:
                p.step()

class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        super().__init__(shape=shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        self.pendown()
    
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5 * dt * self.a
    
    def acc(self):
        a = Vec(0, 0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.pos() - self.pos()
                a += (G * planet.m / abs(v) ** 3) * v
        return a
    
    def step(self):
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt * self.v)
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt * self.a

def main():
    screen = Turtle().getscreen()
    screen.tracer(0, 0)
    
    planet_shapes = [
        ("orange", [(6, 180), (6, 180)]),  # Sun
        ("green", [(6, 180), (6, 180)]),   # Earth
        ("blue", [(6, 180), (6, 180)]),    # Moon
        ("red", [(6, 180), (6, 180)]),     # Mars
        ("orange", [(6, 180), (6, 180)]),  # Jupiter
        ("gray", [(6, 180), (6, 180)]),    # Jupiter's moons
        ("gray", [(6, 180), (6, 180)]),
        ("gray", [(6, 180), (6, 180)]),
        ("gray", [(6, 180), (6, 180)]),
        ("gray", [(6, 180), (6, 180)]),    # Saturn's moons
        ("gray", [(6, 180), (6, 180)]),
        ("gray", [(6, 180), (6, 180)])
    ]
    
    screen.register_shape("planet", planet_shapes)
    screen.tracer(1, 0)

    gs = GravSys()

    # Sun
    sun = Star(1000000, Vec(0, 0), Vec(0, -2.5), gs, "planet")
    sun.color("yellow")
    sun.shapesize(2.8)
    sun.penup()

    # Earth
    earth = Star(12500, Vec(210, 0), Vec(0, 195), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(1.0)

    # Moon
    moon = Star(1, Vec(220, 0), Vec(0, 295), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(0.8)

    # Additional Planets
    mars = Star(10000, Vec(-150, 0), Vec(0, -210), gs, "planet")
    mars.pencolor("red")
    mars.shapesize(0.7)

    jupiter = Star(500000, Vec(350, 0), Vec(0, 140), gs, "planet")
    jupiter.pencolor("orange")
    jupiter.shapesize(1.4)

    # Jupiter's moons
    io = Star(1, Vec(360, 0), Vec(0, 150), gs, "planet")
    io.pencolor("gray")
    io.shapesize(0.8)

    europa = Star(1, Vec(370, 0), Vec(0, 160), gs, "planet")
    europa.pencolor("gray")
    europa.shapesize(0.5)

    ganymede = Star(1, Vec(380, 0), Vec(0, 170), gs, "planet")
    ganymede.pencolor("gray")
    ganymede.shapesize(0.399)

    callisto = Star(1, Vec(390, 0), Vec(0, 180), gs, "planet")
    callisto.pencolor("gray")
    callisto.shapesize(0.3)

    # Saturn's moons
    titan = Star(1, Vec(450, 0), Vec(0, 230), gs, "planet")
    titan.pencolor("gray")
    titan.shapesize(0.3)

    rhea = Star(1, Vec(460, 0), Vec(0, 240), gs, "planet")
    rhea.pencolor("gray")
    rhea.shapesize(0.3)

    iapetus = Star(1, Vec(470, 0), Vec(0, 250), gs, "planet")
    iapetus.pencolor("gray")
    iapetus.shapesize(0.3)

    gs.init()
    gs.start()

if __name__ == "__main__":
    main()
    mainloop()
