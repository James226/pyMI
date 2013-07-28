from Tkinter import *
 
class Index(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Multi-Interface Tool")
        self.root.geometry("768x512")
        self.root.resizable(0, 0)

        self.label = Label(self.root, text="")
        self.label.pack(pady=5)
        
        self.Callbacks = {}

        Button(self.root, text="Go!", command=lambda:self.Callback('Submit')).pack(pady=10)

    def SetText(self, val):
        self.label.config(text=val)
        
    def Callback(self, name):
        if name in self.Callbacks:
            self.Callbacks[name]()

    def Render(self):
        self.root.update()
        self.root.mainloop()