from Tkinter import *

root = Toplevel()

root.title("Venus")
logo = PhotoImage(file="venus.gif")
w2=  Label(root, image=logo).pack(side="left")
ex1="""Diameter:
Rotation Period about Axis:
Mass:
Revolution Period about the Sun (Length of a Year):
Density:
Tilt of Axis:
Minimum Distance from Sun:
Surface Gravity:
Maximum Distance from Sun:
Temperature:
Orbital Semimajor Axis:
Average Surface Temperature (K):
Minimum Distance from Earth:
Satellites:"""
ex2="""
 12,104 km (7,522 miles)
 243 days (retrograde)
 4.87x10^24 kilograms (0.82 x Earth's)
 0.62 years
 5,243 kg/m^3
 177-178o
 108 million km (67 million miles)
 8.87 m/s^2 (0.90 x Earth's)
 109 million km (68 million miles)
 457o C (855o F)
 0.72 AU (Earth=1 AU)
 730K
 40 million km (25 million miles)
 0
"""
w1 = Label(root, justify=LEFT, padx = 10, text=ex1).pack(side="left")
w3 = Label(root, justify=LEFT, padx = 10, text=ex2).pack(side="right")

root.mainloop()
