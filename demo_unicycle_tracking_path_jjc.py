import sys
# Add paths
sys.path.insert(1, './GNC')
sys.path.insert(1, './graphics')
sys.path.insert(1, './postproc')
sys.path.insert(1, './vehicles')

import pygame
import matplotlib.pyplot as pl
import drawmisc
import agents as ag
import numpy as np
import logpostpro as lp
import gvf

# setup simulation
WIDTH = 1000
HEIGHT = 1000

CENTERX = WIDTH/2
CENTERY = WIDTH/2

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)

num_of_agents = 4
list_of_agents = []

for i in range(num_of_agents):
    if i == 1:
        color = RED
    elif i == 2:
        color = GREEN
    elif i == 3:
        color = BLUE
    else:
        color = WHITE

    list_of_agents.append(ag.AgentUnicycle(color, i, 1000*np.random.rand(2,1), 50-100*np.ones([2,1])))#*np.random.rand(2,1)))

for agent in list_of_agents:
    agent.traj_draw = True
    if agent.label == 0:
        agent.neighbors.append = list_of_agents[1]        
    elif agent.label == num_of_agents-1:
        agent.neighbors = [num_of_agents-2]
    else:
        agent.neighbors = [agent.label-1,agent.label+1]
     
    

# GVF
ke_circle = 1e-3
kd_circle = 1
t = 100
#circle_path = gvf.Path_gvf_circle(500,500,100)
circle_ctr = np.array([[500],[500])
circle_r = 100
# run simulation
pygame.init()
clock = pygame.time.Clock()
fps = 50
dt = 1.0/fps
time = 0

runsim = True
while(runsim):
    screen.fill(BLACK)

    us = 0 # We keep constant velocity

    for agent in list_of_agents:
        agent.draw(screen)
        agent_rpos = agent.pos - circle_ctr
        agent_ang =  np.arctan2(agent_rpos[1],agent_rpos[0])
        neighbours_ang_diffs = []
        for i in agent.neighborgs:
            
        circle_path = circle_path = gvf.Path_gvf_circle(500,500,100+ )
        ut = gvf.gvf_control_2D_unicycle(agent.pos, agent.vel, ke_circle, kd_circle, circle_path, 1)
        agent.step_dt(us, ut, dt)
    t = t + fps
    circle_path = gvf.Path_gvf_circle(500+1e-3*t,500+1e-3*t,100)
    clock.tick(fps)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endtime = pygame.time.get_ticks()
            pygame.quit()
            runsim = False


# Postprocessing
fig = pl.figure(0)
ax = fig.add_subplot(111)
for agent in list_of_agents:
    lp.plot_position(ax, agent)
    ax.axis("equal")
pl.show()
