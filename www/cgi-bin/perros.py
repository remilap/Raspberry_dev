#!/usr/bin/python3

import os

# -*- coding: utf-8 -*- 
print('Content-Type: text/html ; charset=utf-8\n')
print('<!DOCTYPE html>')
print('<html> <head>')
print('  <meta charset="utf-8" />')
print('  <base href="http://176.138.37.39/">')
print('  <title>Perros-Guirec Lapointe</title>')
print('</head>')
print('<body> <h1>Perros-Guirec Lapointe</h1>')

# recherche derniere image de la webcam
d = "/var/lib/motion/"
#d = "maison/"
prev = ""
for name in os.listdir(d):
  if os.path.isfile(os.path.join(d, name)):
    if len(prev) == 0:
      prev = name
    if name > prev:
      prev = name

# affichage de cette image
d = "maison/"
dat = prev[5:].split('_')
print('<p>Le ' + dat[2] + '/' + dat[1] + '/' + dat[0] + ' &agrave; ' + dat[3] + ' h</p>')
print('<p><img src="' + d + prev + '"></p>')

# rechercher derniere temperature
flt = "/home/pi/last_temp"
#os.system('cat ' + flt)
#os.system('ssh rasp02 "python3 /home/pi/EduKit2/Code/TEMP.py"')
f = open(flt, 'r') # Opens the file
lines = f.readlines() # Returns the text
f.close()

line = lines[0].split(',')
dat = line[0]
print('<p>Dans la maison, le ' + dat[6:8] + '/' + dat[4:6] + ' &agrave; ' + dat[8:10] + 'h' + dat[10:12] + ' il fait ')
print(line[1] + ' degr&eacute;s</p>')

print("</body></html>")

