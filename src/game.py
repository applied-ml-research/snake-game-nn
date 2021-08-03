import random

WIDTH = 800
HEIGHT = 600
BLOCK_DIM = 5

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

STARTING_DIRECTION = RIGHT

SNAKE_Y = 0
SNAKE_X = 1

class Game:
  def __init__(self, height=HEIGHT//BLOCK_DIM, width=WIDTH//BLOCK_DIM):
    self.height = height
    self.width = width
    self.open = {(y, x) for y in range(height) for x in range(width)}   
    self.snake = [(height//2, width//2)]
    self.direction = STARTING_DIRECTION
    self.alive = True

  def __pick_open_square(self):
    return random.choice(tuple(self.open))

  def set_direction(self, direction):
    self.direction = direction

  def update(self):
    head = self.snake[-1]
    if self.direction == UP:
      new = (head[0] - 1, head[1]) 
    elif self.direction == DOWN:
      new = (head[0] + 1, head[1]) 
    elif self.direction == LEFT:
      new = (head[0], head[1] - 1) 
    elif self.direction == RIGHT:
      new = (head[0], head[1] + 1) 

    if new in self.open:
      self.open.remove(new) 
      self.snake.append(new) 
      self.snake = self.snake[1:]
    else:
      self.alive = False

  def cleanup(self):
    del self.open
    del self.snake
