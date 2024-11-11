import tkinter as tk
import time,random

class Ball:
    def __init__(self,canvas):
        self.canvas=canvas
        self.id=canvas.create_oval(0,0,25,25,fill="red")
        self.canvas.move(self.id,300,300)
        self.x=2
        self.y=-2
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        post=self.canvas.coords(self.id)
        if post[1]<=0:
            self.y=2
        elif post[3]>=600:
            self.y=-2
        elif post[0]<=0:
            self.x=2
        elif post[2]>=800:
            self.x=-2


class Padl:
    def __init__(self,canvas):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,75,10,fill="greenf")


root = tk.Tk()
root.title("ping pong")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = tk.Canvas(root,width=800,height=600,bd=0,highlightthickness=0)
canvas.pack()

ball=Ball(canvas)

while True:
    ball.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
