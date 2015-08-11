from Tkinter import *

root = Toplevel()

root.title("Jupiter")
logo = PhotoImage(file="jupiter.gif")
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
 142,800 km (88,736 miles)
 9.8 hours
 1,898 x10^24 kilograms (318 x Earth's)
 12 years
 1,326 kg/m^3
 3.1o
 741 million km (460 million miles)
 23.12 m/s^2 (2.64 x Earth's)
 817 million km (508 million miles)
 -150o C (-101o F)
 5.20 AU (Earth=1 AU)
 123K
 588 million km (365 million miles)
 63 known
"""
w1 = Label(root, justify=LEFT, padx = 10, text=ex1).pack(side="left")
w3 = Label(root, justify=LEFT, padx = 10, text=ex2).pack(side="right")

root.mainloop()
