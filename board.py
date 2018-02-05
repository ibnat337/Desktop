import turtle
import random

#define scale
x_scale = 20
win_max = 500
start_lives = 20 #no on obj made
scale = round(win_max/x_scale)

blocks = [] #list of obj
#win= turtle.TutleWin("Color creator", win_max, win_max)
for cut in range(scale, win_max+1, scale):
    for cut in range(scale, win_max+1, scale):
        point1=turtle.Point(cut, cut2)
        point2=turtle.Point(cut-scale,cut2-scale)
        block=turtle.Rectangle(point1, point2)
        block.draw(win)
        blocks.append(block)


while start_lives > 0:
    mouse = win.getMouse()
    mouse_x = mouse.getX()
    mouse_y = mouse.getY()

    color=turtle.color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    for index in range(0, len(blocks)):
        center = blocks[index].getCenter()
        center_x = center.getX()
        center_y = center.getY()
        if abs(center_x - mouse_x) < scale/2:
            if abs(center_y - mouse_y) <scale/2:
                blocks[index].setFill(color)
                start_lives -=1
                                     
