#!/usr/bin/python

# Import Libraries
from envirophat import weather


def read_temp():
    t = weather.temperature()
    p = weather.pressure()
    return t



