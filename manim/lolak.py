from manimlib.imports import *

class do(Scene):
    def construct(self):
        ball = Circle(radius = 0.5,color = BLUE,fill_opacity=1)
        dori = Line(UP*2,ball.get_center())
        roof = Line(1.5*LEFT,1.5*RIGHT)
        roof.shift(3*UP)
        self.l = dori.get_length()
        xtext = TextMobject("X=")
        ytext= TextMobject("Y=")
        xtext.move_to([3,3,0])
        ytext.next_to(xtext,DOWN)
        self.add(roof,xtext,ytext)
        self.t = 0
        self.ang = 0
        numx = DecimalNumber(0,num_decimal_places=3)
        numy = DecimalNumber(0,                  num_decimal_places=3)
        numx.next_to(xtext,RIGHT)
        numy.next_to(ytext,RIGHT)
        
        def upd(mob,dt):
            
            self.ang = (PI/4)*np.sin(((9.8/self.l)**1/2)*self.t)#equation
            x = self.ang * self.l#to conv spherical to kartesain
            y = -0.3*np.cos((((9.8/     self.l)**1/2)*self.t)/0.5)
            self.t += dt
            mob.move_to([x,y,0])

        ball.add_updater(upd)
        dori.add_updater(lambda v:v.put_start_and_end_on(UP*3,ball.get_center()))
        numx.add_updater(lambda v:v.set_value(ball.get_center()[0]))
        numy.add_updater(lambda v:v.set_value(ball.get_center()[1]))


        self.add(ball,dori,numx,numy)
        self.wait(30)
        ball.clear_updaters()
        dori.clear_updaters()













    
