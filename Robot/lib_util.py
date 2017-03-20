#!/usr/bin/python

# Library: utilities

# debug and trace modes
debug = 0
trace = 0

# Set debug mode
def SetDebug(m):
	debug = 1
	if m == 0:
		debug = 0

# Set trace mode
def SetTrace(t):
	trace = 1
	if t == 0:
		trace = 0
		
# Display message if trace mode is active
def Trace(t):
	if trace == 1:
		print t


