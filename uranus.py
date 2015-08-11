from Tkinter import *

root = Toplevel()

root.title("Uranus")
logo = PhotoImage(file="uranus.gif")
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
 51,488 km (32,000 miles)
 17.24 hrs (retrograde)
 86.8x10^24 kilograms (14.5 x Earth's)
 84 years
 1,270 kg/m^3
 98o (or 82o)
 2.7 billion km (1.7 billion miles)
 8.69 m/s^2 (0.89 x Earth's)
 3 billion km (1.87 billion miles)
 -200o C ( -328o F)
 19.19 AU (Earth=1 AU)
 73K
 2.57 billion km (1.6 billion miles)
 27 known moons, faint rings
"""
w1 = Label(root, justify=LEFT, padx = 10, text=ex1).pack(side="left")
w3 = Label(root, justify=LEFT, padx = 10, text=ex2).pack(side="right")

root.mainloop()
