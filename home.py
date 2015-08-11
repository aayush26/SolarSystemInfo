from Tkinter import *

def mercury():
   import mercury

def venus():
   import venus

def earth():
   import earth

def mars():
   import mars

def jupiter():
   import jupiter

def saturn():
   import saturn

def uranus():
   import uranus
   
def neptune():
   import neptune

root = Tk()
root.title("Solar System: Home")
b1 = Button(root, text="Mercury", padx=70)
b1.configure(command=mercury)
b2 = Button(root, text="Venus", padx=78)
b2.configure(command=venus)
b3 = Button(root, text="Earth", padx=78)
b3.configure(command=earth)
b4 = Button(root, text="Mars", padx=82)
b4.configure(command=mars)
b5 = Button(root, text="Jupiter", padx=74)
b5.configure(command=jupiter)
b6 = Button(root, text="Saturn", padx=75)
b6.configure(command=saturn)
b7 = Button(root, text="Uranus", padx=73)
b7.configure(command=uranus)
b8 = Button(root, text="Neptune", padx=70)
b8.configure(command=neptune)
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=0)
b4.grid(row=1, column=1)
b5.grid(row=2, column=0)
b6.grid(row=2, column=1)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
root.mainloop()
