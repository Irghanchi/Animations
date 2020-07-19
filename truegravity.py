from manimlib.imports import *

def mag(x):
    return (x[0]**2 + x[1]**2)**0.5



class do(Scene):
    def construct(self):
        sun = Circle(radius = 1,color = ORANGE,fill_opacity = 1,mass =50)
        earth = Circle(radius = 0.2,color =         BLUE ,fill_opacity = 1,dist = [3,0,0],vel=[0,2.9,0])
        self.add(sun,earth)
        earth.move_to(earth.dist)




        def upd(mob,dt):
            """ g = m*r(vec)/r^2
            """
            g = -sun.mass * np.asarray(mob.dist) /mag(mob.dist)**3
            #dv = g*dt
            mob.vel += g * dt
            print(mob.vel)
            ds = mob.vel * dt
            #print(ds)
            mob.dist += ds
            mob.move_to(mob.dist)

        earth.add_updater(upd)
        self.add(earth)
        self.wait(30)
        earth.clear_updaters()


            



