from manimlib import constants
from manimlib.mobject import geometry
from manimlib.scene.scene import Scene
#from manimlib.utils import color
import numpy as np
from manimlib.imports import *

class do(Scene):
    def construct(self):
        sun = geometry.Circle(radius = 0.5,color = constants.COLOR_MAP["YELLOW_C"],opacity =1)
        sun.set_fill(color=constants.COLOR_MAP["GREEN_C"],opacity=1)

        x1 = TextMobject("x = ")
        x1.move_to([2,2,0])
        y1 = TextMobject("y = ")
        y1.next_to(x1,DOWN)
        

        
        earth = geometry.Circle(radius=0.21)
        earth.set_fill(color = constants.COLOR_MAP["YELLOW_C"],opacity = 1) 
        earth.move_to(constants.UP * 3)
        self.add(x1,y1)

        

        #earth_vel = np.array([0,3,0])
        self.t = 0
        self.l = 0
        def upd(earth,dt):
            x = np.cos(self.t)
            y = np.sin(self.t)
            pos = [x,y,0]
            self.t += dt
            earth.move_to(pos)
            
        text1 = DecimalNumber(0,num_decimal_places = 3)
        text2 = DecimalNumber(0,                num_decimal_places = 3)


        earth.add_updater(upd)
        text1.next_to(x1,RIGHT)
        text1.add_updater(lambda v:v.set_value(earth.get_center()[0]))
        text2.add_updater(lambda v:v.  set_value(earth.get_center()[1]))
        text2.next_to(y1,RIGHT)
        self.add(text1)
        self.add(text2)
        self.add(sun)
        self.add(earth)

        self.wait(30)
        earth.clear_updaters()
        text1.clear_updaters()
