from manimlib.imports import *


class do(Scene):
    def construct(self):
        nucleus = Circle(radius = 0.1,color = WHITE,fill_opacity = 1).move_to([-2,0,2])

        def mag(x):
            m =( x[0]**2 + x[1]**2)**0.5       
            return m
    
        def calpos(mob,dt):
            dist = mob.get_center()-nucleus.get_center()
            a = dist*1/mag(dist)**3
            mob.vel += a*dt
            mob.pos += mob.vel*dt
            mob.move_to(mob.pos)

        lst = []
        m= 0
        self.add(nucleus)

        while m <5:
            for i in np.arange(-3,4,0.3):
                lst.append(Circle(radius = 0.01,color = BLUE,fill_opacity = 1,pos = [-5-m,i,0],vel = [1.8,0,0]).move_to([-5-m,i,0]))
            m += 1

        for j in lst:
            j.add_updater(calpos)
            self.add(j)
            m += 1
        self.wait(10)
                

    





        
        
   



