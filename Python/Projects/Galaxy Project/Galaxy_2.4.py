from turtle import Shape, Turtle, mainloop, Vec3D as Vec
import time

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

class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape=shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        self.setz(0)
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        self.pendown()
        self.rotating = True
    
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5 * dt * self.a
    
    def acc(self):
        a = Vec(0, 0, 0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.pos() - self.pos()
                a += (G * planet.m / abs(v) ** 3) * v
        return a
    
    def step(self):
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt * self.v)
        self.setz(0)  # Reset z-coordinate to 0 for 2D representation
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt * self.a
    
    def is_rotating(self):
        return self.rotating

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
    sun = Star(1000000, Vec(0, 0, 0), Vec(0, -2.5, 0), gs, "circle")
    sun.color("yellow")
    sun.shapesize(1.8)
    sun.pu()

    # Earth
    earth = Star(12500, Vec(210, 0, 0), Vec(0, -195, 0), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)

    # Moon
    moon = Star(1, Vec(220, 0, 0), Vec(0, -295, 0), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(0.5)

    # Additional Planets
    mars = Star(10000, Vec(-150, 0, 0), Vec(0, -210, 0), gs, "planet")
    mars.pencolor("red")
    mars.shapesize(0.7)

    jupiter = Star(500000, Vec(350, 0, 0), Vec(0, -140, 0), gs, "planet")
    jupiter.pencolor("orange")
    jupiter.shapesize(1.2)

    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
