from Tkinter import *

root = Tk()

root.title("Mars")
logo = PhotoImage(file="mars.gif")
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
 6,785 km (4,217 miles)
 24.6 hrs
 0.64x10^24 kilograms (0.11 x Earth's)
 1.88 years
 3,933 kg/m^3
 25o 12"
 205 million km (128 million miles)
 3.7 m/s^2 (0.37 x Earth's)
 249 million km (155 million miles)
 -129o C to 0o C ( -200o F to 32o F)
 1.52 AU (Earth=1 AU)
 218K
 35 million miles
 2
"""
w1 = Label(root, justify=LEFT, padx = 10, text=ex1).pack(side="left")
w3 = Label(root, justify=LEFT, padx = 10, text=ex2).pack(side="right")

root.mainloop()
