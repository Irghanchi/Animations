from  manimlib.imports import *

class r(Scene):   
    def setup(self):
        path = Line(LEFT*6,RIGHT*6)
        grup = VGroup()
        dt = 1/self.camera.frame_rate
        self.dt = dt
        for i in range(61):
            prop = 1/60
            line = Line(UP*0.2,DOWN*0.2)
            line.move_to(path.point_from_proportion(prop*i))
            grup.add(line)
            if i in [15,30,60]:
                aro = Arrow(UP,DOWN)
                aro.next_to(line,UP)
                grup.add(aro)

        self.add(path)
        self.grup = grup
        self.add(grup)
        dot = Dot(-4.0,color = RED)
        self.dot = dot
        self.add(dot)
class dt1(r):

    def construct(self):
        self.play(FadeIn(self.grup))
        def updater1(mob,dt):
            mob.shift(RIGHT*0.1)
            mob.counter += 1

        dot = self.dot
        dot.counter = 0
        dot.add_updater(updater1)
        self.add(dot)
        self.wait()
        dot.clear_updaters()

        
    
        

        






