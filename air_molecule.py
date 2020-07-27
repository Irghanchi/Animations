from manimlib.imports import *
from numpy import array,arange
from random import choice

class do(Scene):
    def setup(self):
        leftline  = Line(UP*3,DOWN*3).move_to([-5,0,0])
        rightline = Line(UP*3,DOWN*3).move_to([5,0,0])
        roofline  = Line(RIGHT*5,LEFT*5).move_to([0,3,0])
        baseline  = Line(RIGHT*5,LEFT*  5).move_to([0,-3,0])
        self.add(leftline,rightline,roofline,baseline)

    
    def construct(self): 
        
        # some vector properties
        def mag(x):
            return (x[0]**2 + x[1]**2)**0.5
        def dot(a,b):
            x = a[0]*b[0]
            y = a[1]*b[1]
            ans = x + y 
            return ans

        y = arange(-3,3,0.1)         
        x = arange(-5,5,0.1)              
        vx = arange(-1,1,0.15)   
        vy = arange(-1,1,0.15)
        col = [RED,BLUE,ORANGE,PURPLE,GRAY,GREEN,PINK,WHITE]

        # get moblist and its position
        lst = [Circle(radius = 0.1,color = choice(col),fill_opacity = 1,pos = array([choice(x),  choice(y),0]) ,vel= array([choice(vx),choice(vy),0])).move_to([choice(x),choice(y),0]) for i in range(20)]


        #update function
        def upd(mob,dt):
            for i in lst:
                for j in lst:
                    delpos = array(i.pos - j.pos)
                    delv   = array(i.vel - j.vel)
                    cond   = abs(mag(delpos))
                    if cond < 0.2 and cond >0.01 :
                        i.vel -= (dot(delpos,delv)/mag(delpos)**2)*delpos
                        j.vel -= (dot(-delpos,-delv)/mag(-delpos)**2)*-delpos
                    #out of if
                #out of j loop
                i.vel  += array([0,-3,0])*dt
                i.pos += i.vel * dt
                if i.pos[0]-0.1 <-5.0:
                    i.pos[0] += 0.1
                    i.vel[0] = -i.vel[0]
                if i.pos[0]+0.1 > 5.0:
                    i.pos[0] -= 0.1
                    i.vel[0] = -i.vel[0]
                if i.pos[1]-0.1 <  -3.0:
                    i.pos[1] +=0.1
                    i.vel[1] = -i.vel[1]
                if i.pos[1]+0.1 >  3.0:
                    i.pos[1] -= 0.1
                    i.vel[1] = -i.vel[1]
                i.move_to(i.pos)
                self.add(i)


                #out of list of if
            #out of i loop
        #end all loop

    #now start our animation with any mob
        lst[0].add_updater(upd)
        self.wait(60)









   






            
        
        
        
            








