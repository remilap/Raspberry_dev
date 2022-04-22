# Import Libraries
import os, sys

d = os.path.dirname(__file__)
d = d if d else '.'
sys.path.append(d + "/../Lib")

import send_email

send_email.send_email("Température Perros-Guirec", "La température est 20°")

