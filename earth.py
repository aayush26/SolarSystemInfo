from Tkinter import *

root = Toplevel()

root.title("Earth")
logo = PhotoImage(file="earth.gif")
w2=  Label(root, image=logo).pack(side="left")
ex1="""Diameter:
Rotation Period with respect to Sun (Length of Day):
Mass:
Rotation Period with respect to stars (Sidereal Day):
Density:
Revolution Period about the Sun (Length of a Year):
Minimum Distance from Sun:
Tilt of Axis:
Maximum Distance from Sun:
Temperature:
Orbital Semimajor Axis:
Average Surface Temperature (K):
Satellites:"""
ex2="""
 12,753 km (7,926 miles)
 24 hrs
 5.98x10^24 kilograms(6.5e21 tons)
 23 hrs 56 min
 5,515 kg/m^3
 365 days 5 hrs
 146 million km (91 million miles)
 23o 27"
 152 million km (94.5 million miles)
 -89o C to 57.7o C (-128o F to 136o F)
 1.0 AU
 287K
 1 (the Moon)
"""
w1 = Label(root, justify=LEFT, padx = 10, text=ex1).pack(side="left")
w3 = Label(root, justify=LEFT, padx = 10, text=ex2).pack(side="right")

root.mainloop()
