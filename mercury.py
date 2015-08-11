from Tkinter import *

root = Toplevel()

root.title("Mercury")
logo = PhotoImage(file="mercury.gif")
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
 4,878 km (3,030 miles)
 58.65 days
 0.33x10^24 kilograms (0.06 x Earth's)
 0.24 years
 5,427 kg/m^3
 0o
 46.0 million km(28.6 million miles)
 3.7 m/s^2 (0.38 x Earth's)
 69.8 million km(43.4 million miles)
 -184o C to 427o C(-300o F to 800o F)
 0.387 AU (Earth=1 AU)
 440K
 77.3 million km (48.0 million miles)
 0
"""
w1 = Label(root, justify=LEFT, padx = 10, text=ex1).pack(side="left")
w3 = Label(root, justify=LEFT, padx = 10, text=ex2).pack(side="right")

root.mainloop()
