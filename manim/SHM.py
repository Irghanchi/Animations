from manimlib.imports import *

class sh(Scene):
    def construct(self):
        wall = Line(DOWN*0.5,UP*0.5)
        wall.move_to(4*LEFT)
        path = Line(4*LEFT,4*RIGHT)
        path.move_to(DOWN*0.5)
        sq = Square(side_length = 1)
        sq.pos = ORIGIN
        sq.set_fill(color = RED_C,opacity= 1)
        self.add(wall,path)
        d = 0
        self.d = d
        elas = Line(4*LEFT,3*RIGHT)
        def upd(mob,dt):
            sq.pos[0] = 3*np.cos(self.d)
            self.d = dt + self.d
            sq.move_to([sq.pos[0],0,0])
        

        
        sq.add_updater(upd)
        self.add(sq)
        elas.add_updater(lambda a :a.put_start_and_end_on(4*LEFT,
        [sq.pos[0],0,0]))
        self.add(elas)
        self.wait(10)
        sq.clear_updaters()

            
        

