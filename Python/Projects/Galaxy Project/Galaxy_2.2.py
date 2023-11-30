from turtle import Shape, Turtle, mainloop, Vec2D as Vec

G = 8

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    
    def init(self):
        for p in self.planets:
            p.init()
    
    def start(self):
        for i in range(10000):
            self.t += self.dt
            for p in self.planets:
                p.step()

class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape=shape)
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
        self.v = self.v + 0.5*dt*self.a
    
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
    s = Turtle()
    s.reset()
    s.getscreen().tracer(0, 0)
    s.ht()
    s.pu()
    s.fd(6)
    s.lt(90)
    s.begin_poly()
    s.circle(6, 180)
    s.end_poly()
    m1 = s.get_poly()
    s.begin_poly()
    s.circle(6, 180)
    s.end_poly()
    m2 = s.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1, "orange")
    planetshape.addcomponent(m2, "blue")
    s.getscreen().register_shape("planet", planetshape)
    s.getscreen().tracer(1, 0)

    gs = GravSys()
    sun = Star(1000000, Vec(0, 0), Vec(0, -2.5), gs, "circle")
    sun.color("yellow")
    sun.shapesize(1.8)
    sun.pu()

    # Earth
    earth = Star(12500, Vec(210, 0), Vec(0, -1950), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)

    # Moon
    moon = Star(1, Vec(220, 0), Vec(0, -2950), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(0.5)

    # Additional Planets
    mars = Star(10000, Vec(-150, 0), Vec(0, -2100), gs, "planet")
    mars.pencolor("red")
    mars.shapesize(0.7)

    jupiter = Star(500000, Vec(350, 0), Vec(0, -1400), gs, "planet")
    jupiter.pencolor("orange")
    jupiter.shapesize(1.2)

    # Jupiter's moons
    io = Star(1, Vec(360, 0), Vec(0, -1500), gs, "planet")
    io.pencolor("gray")
    io.shapesize(0.3)

    europa = Star(1, Vec(370, 0), Vec(0, -1600), gs, "planet")
    europa.pencolor("gray")
    europa.shapesize(0.3)

    ganymede = Star(1, Vec(380, 0), Vec(0, -1700), gs, "planet")
    ganymede.pencolor("gray")
    ganymede.shapesize(0.3)

    callisto = Star(1, Vec(390, 0), Vec(0, -1800), gs, "planet")
    callisto.pencolor("gray")
    callisto.shapesize(0.3)

    # Saturn's moons
    titan = Star(1, Vec(450, 0), Vec(0, -2300), gs, "planet")
    titan.pencolor("gray")
    titan.shapesize(0.3)

    rhea = Star(1, Vec(460, 0), Vec(0, -2400), gs, "planet")
    rhea.pencolor("gray")
    rhea.shapesize(0.3)

    iapetus = Star(1, Vec(470, 0), Vec(0, -2500), gs, "planet")
    iapetus.pencolor("gray")
    iapetus.shapesize(0.3)

    # Add more planets and moons as desired

    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
