from Tkinter import *

root = Tk()

root.title("Neptune")
logo = PhotoImage(file="neptune.gif")
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
 49,493 km (30,760 miles)
 17.24 hrs
 102.4x10^24 kilograms (17.2 x Earth's)
 165 years
 1,638 kg/m^3
 29o 36"
 4.46 billion km (2.77 billion miles)
 11 m/s^2 (1.12 x Earth's)
 4.54 billion km (2.82 billion miles)
 -210o C ( -346o F)
 30.07 AU (Earth=1 AU)
 63K
 4.3 billion km (2.68 billion miles)
 13 known moons, faint rings
"""
w1 = Label(root, justify=LEFT, padx = 10, text=ex1).pack(side="left")
w3 = Label(root, justify=LEFT, padx = 10, text=ex2).pack(side="right")

root.mainloop()
