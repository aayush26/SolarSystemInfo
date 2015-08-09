from Tkinter import *

root = Tk()

root.title("Saturn")
logo = PhotoImage(file="saturn.gif")
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
 119,871 km (74,500 miles)
 10.67 hrs
 568.5x10^24 kilograms (95 x Earth's)
 29.5 years
 687 kg/m^3
 26o 42"
 1.35 billion km (840 million miles)
 8.96 m/s^2 (0.92 x Earth's)
 1.5 billion km (938 million miles)
 -170o C (-274o F)
 9.53 AU (Earth=1 AU)
 103K
 1.2 billion km (746 million miles)
 62 known moons, many rings
"""
w1 = Label(root, justify=LEFT, padx = 10, text=ex1).pack(side="left")
w3 = Label(root, justify=LEFT, padx = 10, text=ex2).pack(side="right")

root.mainloop()
