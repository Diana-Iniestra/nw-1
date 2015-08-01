import sys, random
import os
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk as pm
from pymunk import Vec2d

display_size = (1000,700)
##############################################################################
class Circle(object):
    def __init__(self, colour, origin, radius, width=0):
        self.colour = colour
        self.origin = origin
        self.radius = radius
        self.width = width
    def draw(self,image):
        pygame.draw.circle(image,self.colour,self.origin,int(self.radius))
##############################################################################

class Main(object):
    def reset_bodies(self,space):
        for body in space.bodies:
            body.position = Vec2d(body.start_position)
            body.reset_forces()
            body.velocity = 0,0
            body.angular_velocity = 0
        for shape in space.shapes:
            shape.color = THECOLORS["red"]

   ############################################################################## 
def main():
    pygame.init()
    m = Main()
    screen = pygame.display.set_mode(display_size) 
    width, height = screen.get_size()
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 16)

    def to_pygame(p):
        """Small hack to convert pymunk to pygame coordinates"""
        return int(p.x), int(-p.y+height)

    def from_pygame(p):
        return to_pygame(p)
##############################################################################
    ### Physics stuff
    space = pm.Space(iterations = 1)
    space.gravity = (0.0, -1900.0)
    space.damping = 0.8 # to prevent it from blowing up.
    static_body = pm.Body()
    mouse_body = pm.Body()
##############################################################################
    bodies = []
    for x in range(-100,150,50):
        x += width / 2
        offset_y = height/2
        mass = 10
        radius = 25
        moment = pm.moment_for_circle(mass, 0, radius, (0,0))
        body = pm.Body(mass, moment)
        body.position = (x,-125+offset_y)
        body.start_position = Vec2d(body.position)
        shape = pm.Circle(body, radius)
        shape.elasticity = 0.9999999
        shape.friction = 0.5
        space.add(body, shape)
        bodies.append(body)
        pj = pm.PinJoint(static_body, body, (x,125+offset_y), (0,0))
        space.add(pj)
        
    m.reset_bodies(space)
    selected = None
##############################################################################
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.USEREVENT+1:
                r = random.randint(1,4)
                for body in bodies[0:r]:
                    body.apply_impulse((-6000,0))
            if event.type == pygame.USEREVENT+2:
                m.reset_bodies(space)
##############################################################################
            elif event.type == KEYDOWN and event.key == K_r:
                m.reset_bodies(space)
            elif event.type == KEYDOWN and event.key == K_f:
                r = random.randint(1,4)
                for body in bodies[0:r]:
                    body.apply_impulse((-6000,0))
    ##############################################################################
            elif event.type == MOUSEBUTTONDOWN:
                if selected != None:
                    space.remove(selected)
                p = from_pygame(Vec2d(event.pos))
                shape = space.point_query_first(p)
                if shape != None:
                    rest_length = mouse_body.position.get_distance(shape.body.position)
                    ds = pm.DampedSpring(mouse_body, shape.body, (0,0), (0,0), rest_length, 1000, 10)
                    space.add(ds)
                    selected = ds
    ##############################################################################
            elif event.type == MOUSEBUTTONUP:
                if selected != None:
                    space.remove(selected)
                    selected = None
            elif event.type == KEYDOWN:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                running = False
                
        mpos = pygame.mouse.get_pos()
        p = from_pygame( Vec2d(mpos) )
        mouse_body.position = p
##############################################################################
        ### Clear screen
        screen.fill(THECOLORS["black"])
        ### Draw stuff
        for c in space.constraints:
            pv1 = c.a.position + c.anchr1
            pv2 = c.b.position + c.anchr2
            p1 = to_pygame(pv1)
            p2 = to_pygame(pv2)
            pygame.draw.aalines(screen, THECOLORS["yellow"], False, [p1,p2])
##############################################################################
        circles = []
        for ball in space.shapes:
            p = to_pygame(ball.body.position)
            circles.append(Circle(ball.color, p, int(ball.radius), 0))

        for circle in circles:
            circle.draw(screen)
##############################################################################
        fps = 50
        iterations = 25
        dt = 1.0/float(fps)/float(iterations)
        for x in range(iterations): # 10 iterations to get a more stable simulation
            space.step(dt)
##############################################################################
        screen.blit(font.render("fps: " + str(clock.get_fps()), 1, THECOLORS["white"]), (0,0))
        pygame.display.flip()
        clock.tick(fps)

if __name__ == '__main__':
    sys.exit(main())


