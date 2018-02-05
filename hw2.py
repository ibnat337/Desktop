import turtle
import random
class World():
    def __init__(self, mx, my):
            self.maxX = mx
            self.maxY = my
            self.thingList = []
            self.grid = []
            
            for arow in range(self.maxY):
                    row = []
                    for acol in range(self.maxX):
                            row.append(None)
                    self.grid.append(row)
                    
            self.wturtle =  turtle.Turtle()
            self.wscreen = turtle.Screen()
            self.wscreen.setWorldCoordinates(0,0,self.maxX-1,self.maxY-1)
            self.wscreen.addshape("Bear.gif")
            self.wscreen.addshape("Fish.gif")
            self.wturtle.hideturtle()
            
    def draw(self):
            self.wscreen.tracer(0)
            self.wturtle.forward(self.maxX-1)
            self.wturtle.left(90)
            self.wturtle.forward(self.maxY-1)
            self.wturtle.left(90)
            self.wturtle.forward(self.maxX-1)
            self.wturtle.left(90)
            self.wturtle.forward(self.maxY-1)
            self.wturtle.left(90)
            for i in range(self.maxY-1):
                    self.wturtle.forward(self.maxX-1)
                    self.wturtle.backward(self.maxX-1)
                    self.wturtle.left(90)
                    self.wturtle.forward(1)
                    self.wturtle.right(90)
            self.wturtle.forward(1)
            self.wturtle.right(90)
            for i in range(self.maxX-2):
                    self.wturtle.forward(self.maxY-1)
                    self.wturtle.backward(self.maxY-1)
                    self.wturtle.left(90)
                    self.wturtle.forward(1)
                    self.wturtle.right(90)
            self.wscreen.tracker(1)
    
    def freezeWorld(self):
            self.wscreen.exitonclick()
    def addThing(self,athing, x, y):
            athing.setX(x)
            athing.setY(y)
            self.grid[y][x] = athing
            athing.setWorld(self)
            self.thingList.append(athing)
            athing.appear()
    def delThing(self, athing):
            athing.hide()
            self.grid[athing.getY()][athing.getX()] = None
            self.thingList.remove(athing)
    def moveThing(self,oldx, oldy, newx, newy):
            self.grid[newy][newx] = self.grid[oldy][oldx]
            self.grid[oldy][oldx] = None
    
    def getMaxX(self):
            return self.maxX
    def getMaxY(self):
            return self.maxY
            
    def liveALittle(self):
            if self.thingList != []:
                    athing = random.randrange(len(self.thingList))
                    randomthing = self.thingList[athing]
                    randomthing.liveALittle()
    def lookAtLocation(self,x,y):
            return self.grid[y][x]
    def emptyLocation(self,x,y):
            if self.grid[y][x] == None:
                    return True
            else:
                    return False


class Fish:
    def __init__(self):
            self.turtle = turtle.Turtle()
            self.turtle.up()
            self.turtle.hideturtle()
            self.turtle.shape("Fish.gif")
            self.xpos = 0
            self.ypos = 0
            self.world = None
            self.breedTick = 0
    def setX(self,newx):
        pass	    
    def setY(self,newy):
            pass
    def getX(self,newx):
            pass
    def getY(self,newy):
            pass
    def setWorld(self, aworld):
            pass
    def appear(self):
            pass
    def hide(self):
            pass
    def move(self, newy, newx):
            pass
    def liveALittle(self):
            offsetList = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
            adjfish = 0
            for offset in offsetList:
                    newx = self.xpos + offset[0]
                    newy = self.ypos + offset[1]
                    if 0 <= newx < self.world.getMaxX() and 0 <= newy < self.world.getMaxY():
                            if (not self.world.emptyLocation(newx, newy)) and isinstance(self.world.lookAtLocation(newy,newx),Fish):
                                    adjfish += 1
            if adjfish >=2:
                    self.world.delThing(self)
            else:
                    self.world.breedTick += 1
                    if self.breedTick >= 12:
                            self.tryToBreed()
                    self.tryToMove()
    
def mainSimulation():
    numberOfBears = 10
    numberOfFish = 10
    worldLifeTime = 1000
    worldWidth = 50
    worldHeight = 25
    
    myworld = World(worldWidth, worldHeight)
    myworld.draw()
    
    for i in range(numberOfFish):
            newfish = Fish()
            x = random.randrange(myworld, getMaxX())
            y = random.randrange(myworld, getMaxY())
            while not myworld.emptyLocation(x,y):
                    x = random.randrange(myworld, getMaxX())
                    y = random.randrange(myworld, getMaxY())
            myworld.addThing(newfish,x,y)
    for i in range(numberOfBears):
            newbear = Bear()
            x = random.randrange(myworld, getMaxX())
            y = random.randrange(myworld, getMaxY())
            while not myworld.emptyLocation(x,y):
                    x = random.randrange(myworld, getMaxX())
                    y = random.randrange(myworld, getMaxY())
            myworld.addThing(newbear,x,y)
            
    mainSimulation()
