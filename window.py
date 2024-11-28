from tkinter import *
from PIL import Image, ImageTk
import time

class MyApp(object):
    def __init__(self, parent):
        self.width = 600
        self.height = 600
        self.parent = parent
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        self.canvas_frame = Frame(self.main_frame)
        self.canvas_frame.pack(side=TOP)
        self.canvas = Canvas(self.main_frame, \
                             width=self.width, height=self.height)
        self.canvas.pack()
        
        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(side=BOTTOM)
        self.drawbutton = Button(self.button_frame, text="Roll", \
                                 command = self.roll)
        self.drawbutton.pack(side=LEFT)
        self.quitbutton = Button(self.button_frame, text="Quit", \
                                 command = self.quit)
        self.quitbutton.pack(side=RIGHT)

    def quit(self):
        self.parent.destroy()
    
    def update_gif(self, frame, img, canvas_img):
        if frame != img.n_frames:
            img.seek(frame)  # Move to the next frame
            update = ImageTk.PhotoImage(img)
            self.canvas.itemconfig(canvas_img, image=update)
            self.canvas.image = update
            self.parent.after(10, self.update_gif, frame+1, img, canvas_img)

    def roll(self):
        self.canvas.delete("all")

        num = 1
        image_path = "./"+str(num)+".gif"
        img = Image.open(image_path)

        img_tk = ImageTk.PhotoImage(img)
        canvas_img = self.canvas.create_image(0, 0, anchor=NW, image=img_tk)
        self.canvas.image = img_tk    

        self.update_gif(0, img, canvas_img)
        
        
### The main code simply creates a canvas and three buttons. 
if __name__ == "__main__":
    root = Tk()
    root.title("GachaSim")
    myapp = MyApp(root)
    root.mainloop()