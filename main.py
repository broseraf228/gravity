import tkinter
import time
import math


class gravObj:

    def __init__(self, posX, posY, size, mass, canvas: tkinter.Canvas, objList: list, delList: list):

        self.posX = posX
        self.posY = posY
        self.velX = 0
        self.velY = 0
        self.mass = mass

        self.size = size
        self.objList = objList
        self.delList = delList

        self.canvas = canvas
        self.color = "red"

    def update(self):

        forceX = 0
        forceY = 0

        for obj in self.objList:
            if obj == self:
                continue

            distX = self.posX - obj.posX + 0.0001
            distY = self.posY - obj.posY + 0.0001
            dist = (distX**2 + distY**2)**0.5

            if dist < (obj.size + self.size)/2:
                delList.append(self)
                delList.append(obj)
                continue

            forceX += (self.mass * obj.mass) / distX * -abs(distX / dist) * 0.06
            forceY += (self.mass * obj.mass) / distY * -abs(distY / dist) * 0.06

        self.velX += forceX / self.mass
        self.velY += forceY / self.mass

        self.posX += self.velX
        self.posY += self.velY

        self.canvas.create_oval(self.posX + self.size/2, self.posY + self.size/2, self.posX - self.size/2, self.posY - self.size/2, fill=self.color)

def progloop():
    while True:
        global delList
        time_start = time.time()

        canvas.delete("all")
        for obj in objList:
            obj.update()

        for obj in delList:
            try:
                objList.remove(obj)
            except:
                pass
        delList = []

        root.update()

        time_end = time.time()
        time.sleep(0.05-(time_end-time_start))


if __name__ == '__main__':
    objList = []
    delList = []

    #всё для графики
    root = tkinter.Tk()
    root.title("gravity")
    root.geometry("800x600")

    canvas = tkinter.Canvas(bg="white", width=600, height=600)
    canvas.grid(row=0, column=0)

    #-------------------------------
    objList.append(gravObj(100,100,10, 10, canvas, objList, delList))
    objList.append(gravObj(200, 200, 10, 10, canvas, objList, delList))
    objList.append(gravObj(200, 550, 100, 1000, canvas, objList, delList))

    delList.append(gravObj(200, 200, 10, 10, canvas, objList, delList))

    progloop()
