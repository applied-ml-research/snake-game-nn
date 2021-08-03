import game

import tkinter

FPS = 30
EVERY = 1000//FPS

BACKGROUND = 'white'
SNAKE_COLOR = 'red'

gm = None
canvas_buffer = []

def main():
  global gm 
  root = tkinter.Tk()
  root.attributes('-type', 'dialog')
  canvas = tkinter.Canvas(root, bg=BACKGROUND, height=game.HEIGHT, width=game.WIDTH)
  canvas.pack()
  gm = game.Game() 
  root.bind('<KeyPress-Up>', lambda _: gm.set_direction(game.UP))
  root.bind('<KeyPress-Down>', lambda _: gm.set_direction(game.DOWN))
  root.bind('<KeyPress-Left>', lambda _: gm.set_direction(game.LEFT))
  root.bind('<KeyPress-Right>', lambda _: gm.set_direction(game.RIGHT))
  update(root, canvas)
  root.mainloop()

def update(root, canvas):
  global gm 
  global canvas_buffer
  gm.update()
  if not gm.alive:
    gm.cleanup()
    gm = game.Game() 

  next_buffer=[]
  for body in gm.snake:
    next_buffer.append(canvas.create_rectangle(body[game.SNAKE_X] * game.BLOCK_DIM, body[game.SNAKE_Y] * game.BLOCK_DIM, (body[game.SNAKE_X] + 1) * game.BLOCK_DIM, (body[game.SNAKE_Y] + 1) * game.BLOCK_DIM, fill=SNAKE_COLOR))
  canvas.delete(*canvas_buffer)
  canvas_buffer = next_buffer
  root.after(EVERY, update, root, canvas) 

if __name__ == '__main__':
  main()
