import pygame
import time
import random
import sys


# set up pygame window
WIDTH = 800
HEIGHT = 800
FPS = 30

# Define colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)

# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

# setup maze variables
w = 20      # Width of cell
grid = []      
visited = []
stack = []

# draw the grid
def draw_grid(x, y, w):
    for i in range(1, 19):
        x = 20      # Start position
        y += 20     # Start new row
        for j in range(1, 19):
            pygame.draw.line(screen, WHITE, (x, y), (x+w, y))   # Top of cell
            pygame.draw.line(screen, WHITE, (x+w, y), (x+w, y+w))    # Right of cell
            pygame.draw.line(screen, WHITE, (x+w, y+w), (x, y+w))   #   Bottom of cell
            pygame.draw.line(screen, WHITE, (x, y+w), (x, y))   # Left of cell
            grid.append((x, y))
            x += 20     # Moves cell to new position
            pygame.display.update()

def move_up(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y-w+1, 19, 39), 0)
    pygame.display.update()

def move_down(x, y):
    pygame.draw.rect(screen, BLUE, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()


def move_left(x, y):
    pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()


def move_right(x, y):
    pygame.draw.rect(screen, BLUE, (x +1, y +1, 39, 19), 0)
    pygame.display.update()


def single_cell(x, y):
    pygame.draw.rect(screen, YELLOW, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()

def backtracking_cell(x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()

def carve_maze(x, y):
    single_cell(x, y)       # Starting positionm of the maze
    stack.append((x, y))    # Append starting cell to the stack
    visited.append((x, y))  # Append starting cell into visited list
    while len(stack) > 0:
        time.sleep(0.09)
        cell = []
        # Checks for avaiable cells
        if (x, y - w) not in visited and (x, y - w) in grid:    
            cell.append("top")

        if (x + w, y) not in visited and (x + w, y) in grid:
            cell.append("right")

        if(x, y + w) not in visited and (x, y + w) in grid:
            cell.append("bottom")

        if(x - w, y) not in visited and (x - w, y) in grid:
            cell.append("left")
        
        if len(cell) > 0:
            next_cell = random.choice(cell)

            if next_cell == "top":
                move_up(x, y)
                y -= w
                visited.append((x, y))
                stack.append((x, y))

            elif next_cell == "right":
                move_right(x, y)
                x += w
                visited.append((x, y))
                stack.append((x, y))

            elif next_cell == "bottom":
                move_down(x, y)
                y += w
                visited.append((x, y))
                stack.append((x, y))

            elif next_cell == "left":
                move_left(x, y)
                x -= w
                visited.append((x, y))
                stack.append((x, y))
        
        else:
            x, y = stack.pop()      # Pops the latest cell from the stack
            single_cell(x, y)       # Go back to the popped cell
            time.sleep(0.09)
            backtracking_cell(x, y)      
     
x, y = 20, 20 # Starting positiopns of first cell

draw_grid(40, 0, 20)
carve_maze(x, y) 


# Main Loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()