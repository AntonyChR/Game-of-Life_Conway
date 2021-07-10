import pygame as pg
import numpy as np
from time import sleep
from win32api import GetSystemMetrics

y_resolution = GetSystemMetrics(1)

side_screen      = y_resolution - 100          #px
size             = (side_screen, side_screen)
time_refresh     = 0.05                       #seconds
background_color = (0, 0, 0)                  #rgb
grid_color       = (128, 128, 128)
running          = True

#number and side of cells
num_cells_side   = 50 
side_cell        =int(side_screen / num_cells_side)

#---------------------------------------------------------------------------
#cells_state      = np.random.randint(0, 2,(num_cells_side, num_cells_side))

cells_state       = np.zeros((num_cells_side,num_cells_side))

cells_state[9,10] = 1
cells_state[10,10] = 1
cells_state[11,10] = 1
cells_state[11,11] = 1
cells_state[12,10] = 1


#---------------------------------------------------------------------------

pg.init()
screen = pg.display.set_mode(size)

def draw_grid():
    for i in range(0,side_screen,side_cell):
        pg.draw.line(screen,grid_color, (i,0), (i,side_screen), width = 1)
        pg.draw.line(screen,grid_color, (0,i), (side_screen,i), width = 1)

def def_new_state() -> np.array:
    new_state = np.copy(cells_state)
    for i in range(1, num_cells_side - 1):
        for j in range(1, num_cells_side - 1):
            n_active = np.sum(cells_state[i - 1: i + 2, j - 1 : j + 2]) - cells_state[i, j]
            #rules
            if cells_state[i,j] == 1:
                if n_active > 3 or n_active < 2:
                    new_state[i,j] = 0
            elif n_active == 3:
                    new_state[i,j] = 1
    return new_state

def draw_cells(m: np.array):
    for i in range(num_cells_side):
        for j in range(num_cells_side):
            if m[i, j] == 1:
                pg.draw.rect(screen, 
                			grid_color,
                			(i*side_cell, j*side_cell, side_cell, side_cell))

#main loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    cells_state = def_new_state()
    screen.fill(background_color)
    draw_grid()
    draw_cells(cells_state)
    sleep(time_refresh)
    pg.display.update()

pg.quit()


