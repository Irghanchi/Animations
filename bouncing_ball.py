from manimlib.imports import *

class bounce(Scene):
    def construct(self):
        flor = Line(LEFT*6,RIGHT*4)
        flor.move_to(DOWN*3)
        self.add(flor)
        dot = Circle(radius = 0.3)
        dot.set_fill(RED,opacity = 1)
        dot.move_to(UP*3)
        self.add(dot)
        self.a = -3
        self.v = -0.5
        self.pos = 3
        def upd(mob,dt):
            self.v += 0.6*(self.a *dt)
            self.pos += self.v *dt
            mob.move_to([0,self.pos,0])
            if self.pos < -3:
                self.v = -self.v
            if self.pos > +3:
                self.v = -self.v
                

        dot.add_updater(upd)
        self.add(dot)
        self.wait(20)
        dot.clear_updaters()
