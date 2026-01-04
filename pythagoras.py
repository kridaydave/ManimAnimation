from manim import *
import numpy as np

class rightangle(MovingCameraScene) :
    def construct(self):
        self.camera.frame.scale(1.4)
        tri = Polygon([0,0,0],[3,0,0],[0,4,0],color=WHITE)
        tri.move_to(LEFT * 1.5 + UP * 0.5)

        #labels
        a_lab = MathTex("3").next_to(tri,DOWN)
        b_lab = MathTex("4").next_to(tri,LEFT)
        c_lab = MathTex("5")
        corners = tri.get_vertices()
        hypo = (corners[1] + corners[2]) / 2
        c_lab.move_to(hypo).shift(UP*0.4 + RIGHT*0.3)

       

        self.add(tri)
        self.wait(1)
        self.play(Write(a_lab),Write(b_lab),Write(c_lab))

        #SQUARES
        sq_a = Square(side_length=3).set_fill(BLUE,opacity=0.5).next_to(tri,DOWN,buff=0)
        sq_b = Square(side_length=4).set_fill(BLUE,opacity=0.5).next_to(tri,LEFT,buff=0)
        sq_c = Square(side_length=5).set_fill(YELLOW,opacity=0.5).rotate(-np.arctan(4/3)).move_to(hypo).shift(RIGHT*2 + UP*1.5)
        
         #BRANCHED NUMBERS
        b_top = MathTex("4").next_to(sq_b,UP)
        b_left = MathTex("4").next_to(sq_b,LEFT)
        b_bottom = MathTex("4").next_to(sq_b,DOWN)

        a_left = MathTex("3").next_to(sq_a,LEFT)
        a_right = MathTex("3").next_to(sq_a,RIGHT)
        a_bottom = MathTex("3").next_to(sq_a,DOWN)
        
        
        
        self.wait(1)
        self.play(Create(sq_a))
        self.play(Create(sq_b))
        self.wait(1)
        self.play(
            TransformFromCopy(b_lab,b_top),
            TransformFromCopy(b_lab,b_left),
            TransformFromCopy(b_lab,b_bottom)
        )
        self.wait(1)
        self.play(
            TransformFromCopy(a_lab,a_bottom),
            TransformFromCopy(a_lab,a_left),
            TransformFromCopy(a_lab,a_right)
            
        )
        self.play(Create(sq_c))
        self.wait(1)
        
        # ... after self.play(Create(sq_c)) ...

        # 4. THE PROOF TEXT (Moved to Top Left Safe Zone)
        # We use a VGroup to organize the lines
        
        # Step A: Create the Equation
        equation = MathTex("3^2", "+", "4^2", "=", "5^2")
        equation.to_corner(UP + LEFT) # Snaps to top-left corner
        equation.shift(RIGHT * 1 + UP * 1.1 ) # Nudge it in slightly so it's not hugging the edge

        # Step B: Create the Calculation
        calculation = MathTex("9", "+", "16", "=", "25")
        calculation.next_to(equation, DOWN, buff=0.5) # Puts it under the equation

        # Step C: Colors
        equation[0].set_color(BLUE)
        equation[2].set_color(BLUE)
        equation[4].set_color(YELLOW)
        
        calculation[0].set_color(BLUE)
        calculation[2].set_color(BLUE)
        calculation[4].set_color(YELLOW)

        # 5. ANIMATE
        self.play(Write(equation))
        self.wait(1)
        
        # Transform: Keep the top line, reveal the bottom line
        self.play(TransformMatchingTex(equation.copy(), calculation))
        self.wait(2)
        
        # 6. FADE OUT (Everything)
        # Note: We added 'equation' and 'calculation' to the cleanup list
        


        final_group = VGroup(
            tri, sq_a, sq_b, sq_c,          # Shapes
            a_lab, b_lab, c_lab,            # Original Labels
            equation, calculation,          # Math Text
            b_top, b_left, b_bottom,           # Branching 4s
            a_left, a_right, a_bottom,         # Branching 3s
        )

        self.play(FadeOut(final_group,shift=DOWN),run_time=1.5)
        self.wait(1)

        credit = Text("Thanks For Watching")
        manim = Text("Made In Manim").next_to(credit,DOWN)

        self.play(Write(credit))
        self.wait(1)
        self.play(Write(manim))
        self.wait(1)
        tgroup = VGroup(credit,manim)
        self.play(FadeOut(tgroup),run_time=1.5)
        self.wait(2)